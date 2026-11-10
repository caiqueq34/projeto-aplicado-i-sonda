# Dicionário e procedência dos dados

- **Fonte e responsável pela publicação.** SONDA S.A., [Kit do Investidor](https://www.sonda.com/inversionistas), arquivo [Resumen Financiero (9M26)](https://www.sonda.com/docs/sondanewsitelibraries/inversionistas/informacion-financiera/reportes-trimestrales/2026/3q/web-sonda-c---resumen-financiero-09-2026---esp.xlsx?sfvrsn=e9e3079d_7), aba `Est.Resultado Trim. IFRS`. Acesso em 9 nov. 2026.
- **Cobertura.** Do 1º trimestre de 2019 ao 4º trimestre de 2025, total de 28 observações. A edição da planilha inclui 2026, excluído para comparar anos completos.
- **Formato.** XLSX na origem e CSV UTF-8 na extração. Separador vírgula, decimal com ponto, até seis casas decimais. Cada linha representa um trimestre.
- **Sensibilidade e acesso.** Indicadores corporativos agregados e disponíveis publicamente, sem dados pessoais. A planilha integral permanece no site da fonte. O projeto disponibiliza a tabela derivada para análise acadêmica com atribuição.
- **Validade.** Recorte histórico fixo. Edições futuras ou comunicados publicados em outras datas podem apresentar números diferentes por revisão ou critérios de apresentação. Os valores foram mantidos em CLP nominais, inclusive os da região Brasil.

| Campo | Tipo | Definição | Linha da planilha |
| --- | --- | --- | --- |
| ano | inteiro | Ano civil do trimestre | 6 |
| trimestre | inteiro | Trimestre de 1 a 4 | 6 |
| receita_grupo_clp_mi | decimal | Receita de atividades ordinárias do grupo consolidado, em milhões de CLP | 9 |
| lucro_bruto_grupo_clp_mi | decimal | Lucro bruto consolidado, em milhões de CLP | 11 |
| receita_brasil_clp_mi | decimal | Receita da região Brasil, em milhões de CLP | 74 |
| lucro_bruto_brasil_clp_mi | decimal | Lucro bruto da região Brasil, em milhões de CLP | 79 |

O Brasil integra o consolidado. As duas séries são comparadas como referências de desempenho, sem tratá-las como observações independentes nem somá-las.
