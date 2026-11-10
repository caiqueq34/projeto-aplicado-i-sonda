"""Converte as linhas selecionadas da planilha pública da SONDA em CSV."""
import argparse
import csv
from math import isfinite
from pathlib import Path
import re

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent
SHEET = "Est.Resultado Trim. IFRS"
CAMPOS = {
    "receita_grupo_clp_mi": (9, "Ingresos de Actividades Ordinarias"),
    "lucro_bruto_grupo_clp_mi": (11, "Ganancia Bruta"),
    "receita_brasil_clp_mi": (74, "Ingresos"),
    "lucro_bruto_brasil_clp_mi": (79, "Ganancia Bruta"),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("planilha", type=Path, help="Arquivo XLSX do RI da SONDA")
    args = parser.parse_args()
    workbook = load_workbook(args.planilha, read_only=True, data_only=True)
    try:
        rows = list(workbook[SHEET].values)
    finally:
        workbook.close()
    if str(rows[72][0]).strip().upper() != "BRASIL":
        raise ValueError("A seção Brasil mudou de posição na planilha.")
    for row, label in CAMPOS.values():
        if str(rows[row - 1][0]).strip() != label:
            raise ValueError(f"Rótulo inesperado na linha {row}: esperado {label}.")

    records = {}
    for column, header in enumerate(rows[5]):
        match = re.fullmatch(r"([1-4])T(\d{2})", str(header).strip())
        if not match:
            continue
        quarter, year_suffix = map(int, match.groups())
        year = 2000 + year_suffix
        if 2019 <= year <= 2025:
            key = (year, quarter)
            if key in records:
                raise ValueError(f"Trimestre duplicado: {year}T{quarter}.")
            values = [rows[row - 1][column] for row, _ in CAMPOS.values()]
            if any(type(value) not in (int, float) or not isfinite(value) for value in values):
                raise ValueError(f"Dado ausente ou inválido em {year}T{quarter}.")
            records[key] = [round(value, 6) for value in values]

    expected = {(year, q) for year in range(2019, 2026) for q in range(1, 5)}
    if records.keys() != expected:
        raise ValueError(f"Trimestres ausentes: {sorted(expected - records.keys())}.")

    path = ROOT / "dados" / "sonda_trimestral.csv"
    path.parent.mkdir(exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["ano", "trimestre", *CAMPOS])
        for (year, quarter), values in sorted(records.items()):
            writer.writerow([year, quarter, *values])
    print(f"{len(records)} trimestres exportados para {path}.")


if __name__ == "__main__":
    main()
