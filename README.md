# Projeto Aplicado I — SONDA

**Etapa 3 — Esboço de Data Storytelling e scripts da Análise Exploratória de Dados.**

## Pergunta de pesquisa

Entre 2019 e 2025, como evoluíram a receita e a margem bruta da operação brasileira da SONDA em comparação com o grupo consolidado?

De 2024 para 2025, a receita brasileira aumentou 1,62% em pesos chilenos nominais. No mesmo período, a margem bruta brasileira passou de 10,87% para 8,29%. A margem consolidada também caiu, de 15,11% para 13,92%.

## Arquivos

| Arquivo ou pasta | Conteúdo |
| --- | --- |
| [Projeto_Aplicado_I_SONDA.docx](Projeto_Aplicado_I_SONDA.docx) | Documento editável da Etapa 3 com metodologia e resultados |
| [storytelling.md](storytelling.md) | Esboço narrativo com três figuras |
| [extrair_dados.py](extrair_dados.py) | Extrai os valores trimestrais da planilha original |
| [analise_exploratoria.py](analise_exploratoria.py) | Valida o CSV e gera tabelas e gráficos |
| [dados](dados/) | CSV de entrada e dicionário de dados |
| [resultados](resultados/) | Tabelas e gráficos reproduzíveis |

## Como executar

Na pasta do projeto, com Python 3.10 ou superior:

```bash
python -m pip install -r requirements.txt
python analise_exploratoria.py
```

O CSV acompanha o projeto. Para refazer a extração, baixe o arquivo **Resumen Financiero (9M26)** indicado em [dados/README.md](dados/README.md) e execute `python extrair_dados.py caminho-da-planilha.xlsx`. Em seguida, rode novamente a análise. Os scripts usam caminhos relativos à própria pasta, independentemente do diretório de execução.

## Fontes e recorte

A base é uma extração de indicadores agregados publicados pela [SONDA no Kit do Investidor](https://www.sonda.com/inversionistas). Os 28 trimestres correspondem a 2019–2025. Os valores estão em milhões de pesos chilenos nominais, inclusive para o Brasil. O resumo anual soma os quatro trimestres da mesma edição da planilha. A margem anual é o lucro bruto anual dividido pela receita anual. Comparações são descritivas e podem refletir efeitos de câmbio, composição dos negócios e revisões contábeis.
