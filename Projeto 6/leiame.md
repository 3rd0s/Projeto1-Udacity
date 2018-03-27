# Resumo

O Myers Briggs Type Indicator(MBTI) é um sistema de tipologia de personalidade no qual há 16 tipos possiveis de personalidade vindos de 4 características cada uma com 2 possibilidade:

    Introversion (I) – Extroversion (E)
    Intuition (N) – Sensing (S)
    Thinking (T) – Feeling (F)
    Judging (J) – Perceiving (P)

Se por exemplo uma pessoa tiver as características introversão, intuição, pensamento e percepção era será do tipo INTP Também foi usado uma divisão por classes do site 16personalites a qual agrupa as personalidades em 4 classes(Exploradores, Analistas, Sentinelas e Diplomatas). Os dados foram trabalhados utilizando-se de python e foi calculado o número médio de palavras por comentário, esse número foi normalizado para ficar centralizado em zero e em unidades de desvio padrão.

O gráfico propõe notar padrões no quanto a pessoa fala por post no PersonalityCafe e sua personalidade. O DataSet foi baixado no Kaggle.

Cada personalidade utiliza um número diferente de palavras por post, com o grupo dos diplomatas sendo os mais falantes e os exploradores são os que falam menos, o que pode ser explicado pela teoria do MBTI aonde os diplomatas são mais falantes e os Exploradores estariam explorando o mundo offiline.

# Design

Foi escolhido o gráfico de barras por mostrar bem a relação entre categorias No eixo X foram colocados os tipos e no y a quantidade normalizada de palavras por post, para melhor visualização das classes elas foram codificadas por cores sendo colocado uma legenda para explicitar isso mais rapidamente. Foram retirados as gridlines e os ticks para poder se deixar o gráfico mais clean.

Foi alterado o tamanho dos títulos de cada eixo e dos labels dos ticks e colocado um título engajante para motivar o leitor do gráfico a lê-lo. As cores foram escolhidas de modo que destacasse bem as diferentes classes, para isso foi escolhido um esquema de cores qualitativo, pois não há uma gradação de valores entre as classes.


# Feedback
Foi notado no primeiro feedback que a dropline que aparecia quando passa o mouse por cima não funcionava direito quando o valor de y era negativo. Como não a considerei importante para a visualização a retirei do gráfico.


Já o segundo Feedback. Ele considerou que a desproporcionalidade dos ESFP fazia o gráfico ficar feio. Porém não vi forma de solucionar isso sem aumentar o lie factor. Como prezo pela precisão dos dados deixei sem alterar.

No terceiro feedback foi proposto deixar os gráficos todos positivos. Como isso permitiria voltar com a animação resolvi aceitar a ideia e fiz mais um teste que acabei acatando como o final. Para a última visualização também modifiquei no tamanho das colunas e deixei o gráfico mais alinhado.

Depois do feedback do avaliador da Udacity decidi voltar a normalização pois considerei que o que quero demonstrar é a diferença em desvios padrões.

Um último feedback, a pessoa considerou que eu deveria colocar os tipos em ordem crescente de palavras por post. Mas preferi deixar do jeito que está. Mas adicionei conforme o feedback do avaliador um texto explicativo

# Recursos

Foram consultadas bastante as documentações oficiais do Dimple.js e do D3.js além site stackoverflow.com.
