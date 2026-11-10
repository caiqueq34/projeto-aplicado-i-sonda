# Esboço de Data Storytelling

**Público:** turma de Ciência de Dados, professor e leitores com interesse em BI.

**Mensagem central:** no Brasil, a receita da SONDA cresceu em 2025 em relação a 2024, mas a empresa reteve uma parcela menor dessa receita como lucro bruto.

## 1 Contexto

A SONDA atua em serviços e soluções de TI. A equipe responsável por acompanhar o desempenho precisa comparar o Brasil com o grupo consolidado. A Figura 1 mostra os totais anuais em bilhões de pesos chilenos nominais. No Brasil, a receita foi de CLP 411,82 bilhões em 2024 e CLP 418,48 bilhões em 2025, alta de 1,62%.

![Receita anual da SONDA por recorte](resultados/01_receita_anual.png)

## 2 Conflito

A receita isolada deixa uma pergunta em aberto. Quanto dela virou lucro bruto? Em 2025, a operação brasileira registrou CLP 34,70 bilhões de lucro bruto ante CLP 44,75 bilhões em 2024. O volume de receita cresceu, enquanto o lucro bruto caiu.

## 3 Ponto de virada

Revela-se a Figura 2. A margem bruta brasileira recuou de 10,87% para 8,29%, queda de 2,58 pontos percentuais. O grupo consolidado foi de 15,11% para 13,92%, queda de 1,19 ponto percentual. A comparação contextualiza o Brasil, que integra o grupo.

![Margem bruta anual da SONDA por recorte](resultados/02_margem_anual.png)

A Figura 3 prepara a conversa sobre acompanhamento. O quarto trimestre teve a maior mediana de receita no Brasil, CLP 80,64 bilhões, com sete observações para cada posição no calendário. A diferença entre trimestres é um padrão descritivo da amostra.

![Distribuição da receita do Brasil por trimestre](resultados/03_distribuicao_brasil.png)

## 4 Resolução

Propor um painel de BI com receita, lucro bruto e margem bruta para Brasil e consolidado. Exibir cada trimestre ao lado do mesmo trimestre do ano anterior. Destacar os casos em que a receita aumenta e a margem cai, com o comparativo e a edição da fonte visíveis. A queda é um ponto de partida para investigação. Para separar efeitos de câmbio e composição das vendas, a próxima análise dependeria de dados adicionais com recorte compatível.

**Encerramento sugerido.** Em 2025, o Brasil registrou mais receita em CLP e menos lucro bruto. A proposta é acompanhar os dois indicadores juntos a cada trimestre.
