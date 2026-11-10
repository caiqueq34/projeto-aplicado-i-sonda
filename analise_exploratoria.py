"""Valida e explora os resultados trimestrais públicos da SONDA."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "dados" / "sonda_trimestral.csv"
OUT = ROOT / "resultados"
CHAVES = ["ano", "trimestre"]
METRICAS = [
    "receita_grupo_clp_mi", "lucro_bruto_grupo_clp_mi",
    "receita_brasil_clp_mi", "lucro_bruto_brasil_clp_mi",
]
GRUPO, LUCRO_GRUPO, BRASIL, LUCRO_BRASIL = METRICAS
MG, MB = "margem_bruta_grupo_pct", "margem_bruta_brasil_pct"


def validar(df):
    if df.columns.tolist() != CHAVES + METRICAS:
        raise ValueError("Colunas diferentes do dicionário de dados.")
    quality = {
        "linhas": len(df),
        "colunas_originais": len(df.columns),
        "celulas_ausentes": int(df.isna().sum().sum()),
        "linhas_duplicadas": int(df.duplicated().sum()),
        "periodos_duplicados": int(df.duplicated(CHAVES).sum()),
        "receitas_nao_positivas": int(df[[GRUPO, BRASIL]].le(0).sum().sum()),
        "valores_infinitos": int(df.isin([float("inf"), float("-inf")]).sum().sum()),
    }
    expected = {(year, q) for year in range(2019, 2026) for q in range(1, 5)}
    periods = set(df[CHAVES].itertuples(index=False, name=None))
    quality["periodos_ausentes"] = len(expected - periods)
    quality["periodos_inesperados"] = len(periods - expected)
    if any(list(quality.values())[2:]):
        raise ValueError(f"Falha na validação: {quality}")
    return quality


def margens(df):
    df[MG] = df[LUCRO_GRUPO] / df[GRUPO] * 100
    df[MB] = df[LUCRO_BRASIL] / df[BRASIL] * 100


def pt(value, digits=0):
    return f"{value:,.{digits}f}".replace(",", "_").replace(".", ",").replace("_", ".")


def graficos(df, anual):
    cores = {"grupo": "#153D67", "brasil": "#12766B"}
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(8, 3.7), layout="constrained")
    ax.plot(anual.index, anual[GRUPO] / 1000, marker="o", color=cores["grupo"], label="Grupo consolidado")
    ax.plot(anual.index, anual[BRASIL] / 1000, marker="o", color=cores["brasil"], label="Brasil")
    ax.set(title="Receita anual da SONDA", ylabel="Bilhões de CLP", ylim=(0, None))
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=.25)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: pt(x)))
    fig.savefig(OUT / "01_receita_anual.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 3.7), layout="constrained")
    ax.plot(anual.index, anual[MG], marker="o", color=cores["grupo"], label="Grupo consolidado")
    ax.plot(anual.index, anual[MB], marker="o", color=cores["brasil"], label="Brasil")
    for col, key in [(MG, "grupo"), (MB, "brasil")]:
        for year in (2024, 2025):
            value = anual.loc[year, col]
            ax.annotate(f"{pt(value, 1)}%", (year, value), xytext=(0, 8),
                        textcoords="offset points", ha="center", color=cores[key])
    ax.set(title="Margem bruta anual da SONDA", ylabel="Margem bruta (%)", xlim=(2018.7, 2025.4))
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=.25)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: pt(x)))
    fig.savefig(OUT / "02_margem_anual.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 3.7), layout="constrained")
    by_quarter = [df.loc[df["trimestre"].eq(q), BRASIL] / 1000 for q in range(1, 5)]
    ax.boxplot(by_quarter, tick_labels=["1º tri", "2º tri", "3º tri", "4º tri"],
               patch_artist=True, boxprops={"facecolor": "#B8DFD8"})
    ax.set(title="Distribuição da receita do Brasil por trimestre", ylabel="Bilhões de CLP")
    ax.grid(axis="y", alpha=.25)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: pt(x)))
    fig.savefig(OUT / "03_distribuicao_brasil.png", dpi=160)
    plt.close(fig)


def main():
    df = pd.read_csv(DATA)
    quality = validar(df)
    df = df.sort_values(CHAVES)
    margens(df)
    anual = df.groupby("ano")[METRICAS].sum()
    margens(anual)
    for col in (GRUPO, BRASIL):
        anual[f"{col}_var_anual_pct"] = anual[col].pct_change() * 100

    numericas = METRICAS + [MG, MB]
    descritiva = df[numericas].describe().T
    descritiva["amplitude"] = descritiva["max"] - descritiva["min"]
    df["periodo"] = df["ano"].astype(str) + "T" + df["trimestre"].astype(str)
    quartis = df[numericas].quantile([.25, .75])
    iqr = quartis.loc[.75] - quartis.loc[.25]
    flags = df[numericas].lt(quartis.loc[.25] - 1.5 * iqr) | df[numericas].gt(quartis.loc[.75] + 1.5 * iqr)
    flags.index = df["periodo"]
    flags.index.name = "periodo"
    outliers = flags.loc[flags.any(axis=1)]

    OUT.mkdir(exist_ok=True)
    pd.Series(quality, name="valor").rename_axis("verificacao").to_csv(OUT / "qualidade.csv")
    anual.to_csv(OUT / "resumo_anual.csv", float_format="%.6f")
    descritiva.to_csv(OUT / "estatistica_descritiva.csv", float_format="%.6f")
    df.groupby("trimestre")[BRASIL].agg(["size", "median", "mean", "min", "max"]).to_csv(
        OUT / "receita_brasil_por_trimestre.csv", float_format="%.6f"
    )
    df[numericas].corr().to_csv(OUT / "correlacoes_pearson.csv", float_format="%.6f")
    outliers.to_csv(OUT / "pontos_atipicos_iqr.csv")
    graficos(df, anual)
    print(pd.Series(quality).to_string())
    print(anual.round(2).to_string())
    print(f"Trimestres com ao menos um ponto atípico: {len(outliers)}")


if __name__ == "__main__":
    main()
