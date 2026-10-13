import os, json, sys
import pandas as pd
from pdflib import Doc

R = 'run_real/results/'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'relatorio.pdf'
f = lambda v, n=3: '—' if pd.isna(v) else f'{v:.{n}f}'.replace('.', ',')
pct = lambda v: '—' if pd.isna(v) else f'{100*v:.1f}%'.replace('.', ',')

TSM = pd.read_csv(R + 'tabela_SisFall_MobiFall.csv').set_index('Método')
TMS = pd.read_csv(R + 'tabela_MobiFall_SisFall.csv').set_index('Método')
ABL = pd.read_csv(R + 'ablacao_faixa_sisfall.csv')
GRD = pd.read_csv(R + 'limiares_grade_ampliada.csv')
JAN = pd.read_csv(R + 'cnn_metricas_por_janela.csv')
SEM = pd.read_csv(R + 'cnn_variacao_sementes.csv')
SPG = pd.read_csv(R + 'sp_jovem_idoso_MobiFall_SisFall.csv').set_index('metodo')
NAT = pd.read_csv(R + 'taxa_nativa_200hz_sisfall.csv') if os.path.exists(R + 'taxa_nativa_200hz_sisfall.csv') else None

TEXTO_200HZ = ('Reduzir de 200 para 50 Hz quase não muda os limiares: a diferença no F1 é de no máximo 0,03, '
               'com o Kangas um pouco melhor e o Bourke3 um pouco pior a 200 Hz. Portanto, a taxa de 50 Hz usada no estudo não explica '
               'nenhuma das conclusões, nem a distância entre o PIPTO aqui (F1 ≈ 0,81) e a acurácia acima de 97% relatada pelos autores na SisFall.')
d = Doc(OUT, 'Limiar × CNN-LSTM entre bases: relatório do experimento')

# ------------------------------------------------------------------ capa / resumo
d.t('Detecção de quedas com sensores de movimento: limiares × aprendizado de máquina')
d.sub('Quanto cada método perde ao ser levado para outra base de dados (e para o celular no bolso)?<br/>'
      'Relatório do experimento, Projeto Mova (UNAMA), outubro de 2026')
d.sp(0.4)
d.box('<b>Resumo em uma frase.</b> A rede neural (CNN-LSTM, reimplementada de Duan et al. 2026) é a melhor <i>dentro</i> '
      'da base em que foi treinada (F1 de 0,93 a 0,99, com 99,0% de acurácia por janela, igual ao artigo), mas é a que mais '
      'perde ao ir para outra base. Da cintura (SisFall) para o celular no bolso (MobiFall), o F1 caiu para 0,21–0,56. '
      'O melhor algoritmo de limiar (Kangas 2008) quase não perdeu: F1 0,95 → 0,89. Porém, os limiares que dependem de picos '
      'de impacto altos (Bourke3 e PIPTO) desabaram no celular, porque o acelerômetro do celular da MobiFall '
      'satura em ±2 g. Ou seja, a robustez não depende de ser "limiar" ou "IA", e sim de o método depender ou não de '
      'características do sensor (faixa de medida e orientação).')

d.h1('Resumo')
d.p('<b>Pergunta.</b> Quando um detector de quedas é ajustado ou treinado numa base de dados e testado em outra, os '
    'algoritmos de limiar perdem desempenho tanto quanto um modelo leve de aprendizado de máquina (TinyML)?')
d.p('<b>O que foi feito.</b> Implementamos em Python três algoritmos de limiar publicados (Kangas 2008, Bourke 2010 e PIPTO 2023; '
    'o PIPTO roda com o <i>código original dos autores</i>) e reimplementamos a CNN-LSTM de 21.434 parâmetros de Duan et al. (2026). '
    'Todos foram avaliados com o mesmo pré-processamento e a mesma regra de pontuação em duas bases públicas:')
d.ul(['<b>SisFall:</b> sensor na cintura, 38 pessoas (15 idosas), 4.396 tentativas;',
      '<b>MobiFall v2.0:</b> smartphone no bolso da calça, 24 pessoas, 630 tentativas.'])
d.p('Testamos as duas direções (SisFall → MobiFall e MobiFall → SisFall). Em cada uma, o detector é ajustado ou treinado numa base '
    'e aplicado na outra sem nenhum retreino. O processamento levou cerca de 4 horas em CPU.')
d.p('<b>Resultados principais (SisFall → MobiFall, a direção que interessa ao Mova):</b>')
k, kp = TSM.loc['Kangas (publicado)'], TSM.loc['Kangas (ajustado)']
c1, c2, cz, cr = (TSM.loc['CNN-LSTM [z treino] k=1'], TSM.loc['CNN-LSTM [z treino] k=2'],
                  TSM.loc['CNN-LSTM [z por base] k=2'], TSM.loc['CNN-LSTM rot [z treino] k=1'])
b, p_ = TSM.loc['Bourke3 (publicado)'], TSM.loc['PIPTO (publicado)']
d.ol([
    f'<b>Dentro da base, a CNN-LSTM é a melhor.</b> F1 = {f(c1["SisFall F1"])} (regra k=1) e {f(c2["SisFall F1"])} (regra k=2 do artigo) na SisFall. '
    'A acurácia por janela foi de 99,0%, praticamente a mesma do artigo original (99,3% na KFall). A reimplementação reproduz o resultado "de laboratório".',
    f'<b>Fora da base, a CNN-LSTM é a que mais perde.</b> Na MobiFall, o F1 caiu para {f(c1["MobiFall F1"])} (k=1) e {f(c2["MobiFall F1"])} (k=2): '
    f'ΔF1 = {f(c1["ΔF1"],2)} e {f(c2["ΔF1"],2)}. Com a normalização usada no artigo ("z-score por base"), o F1 foi {f(cz["MobiFall F1"])}.',
    f'<b>O melhor limiar quase não perde.</b> Kangas com os parâmetros publicados: F1 {f(k["SisFall F1"])} → {f(k["MobiFall F1"])} '
    f'(ΔF1 = {f(k["ΔF1"],3)}, IC 95% {f(k["ΔF1 IC95% inf"],3)} a {f(k["ΔF1 IC95% sup"],3)}). Reajustado na SisFall: '
    f'{f(kp["SisFall F1"])} → {f(kp["MobiFall F1"])}. Os intervalos de confiança do Kangas e da CNN-LSTM não se sobrepõem.',
    f'<b>Mas nem todo limiar é robusto.</b> Bourke3 (F1 {f(b["SisFall F1"])} → {f(b["MobiFall F1"])}) e PIPTO ({f(p_["SisFall F1"])} → {f(p_["MobiFall F1"])}) '
    'desabaram no celular. A causa foi isolada experimentalmente: o acelerômetro do Galaxy S3 usado na MobiFall satura em ±2 g, então quase nenhum pico de '
    'queda passa dos limiares de impacto deles (2,8 g e ≈3,06 g). Ao simular essa saturação na própria SisFall, a sensibilidade do PIPTO caiu de 81% para 36% '
    'e a do Bourke3 de 61% para 47%. A do Kangas ficou em 93%.',
    f'<b>Parte da perda da CNN vem da orientação do sensor.</b> A gravidade aparece no eixo y com sinal oposto nas duas bases. '
    f'Treinar a CNN com rotações 3D aleatórias reduziu a perda pela metade (ΔF1 {f(c1["ΔF1"],2)} → {f(cr["ΔF1"],2)}), mas não eliminou.',
    f'<b>A direção inversa confirma.</b> Da MobiFall para a SisFall, a CNN-LSTM (k=1) caiu de {f(TMS.loc["CNN-LSTM [z treino] k=1","MobiFall F1"])} '
    f'para {f(TMS.loc["CNN-LSTM [z treino] k=1","SisFall F1"])}, com {f(TMS.loc["CNN-LSTM [z treino] k=1","SisFall FA/h"],0)} alarmes falsos por hora. '
    f'O Kangas reajustado na MobiFall foi de {f(TMS.loc["Kangas (ajustado)","MobiFall F1"])} para {f(TMS.loc["Kangas (ajustado)","SisFall F1"])}, ou seja, não piorou.',
])
d.p('<b>Resposta à pergunta.</b> Para o melhor algoritmo de limiar (Kangas), a hipótese H1 se confirma: o modelo de aprendizado de máquina perde '
    '<b>muito mais</b> ao trocar de base. Isso <b>não</b> vale para "limiares em geral". Algoritmos que dependem de picos altos de impacto '
    'são tão ou mais frágeis que a rede neural quando o sensor muda. O resultado também contradiz, nas nossas condições, a perda de apenas ~1% '
    'relatada por Duan et al. (2026) na transferência KFall → SisFall. A diferença provável é que a nossa troca de base envolve mudança de '
    '<i>posição</i> e de <i>aparelho</i> (cintura → bolso), e não apenas de pessoas.')
d.box('<b>Roteiro de 1 minuto para explicar ao professor.</b> (1) <i>Pergunta:</i> algoritmos de limiar perdem tanto quanto IA ao mudar de base? '
      '(2) <i>Por que esses algoritmos:</i> Kangas e Bourke3 são os únicos limiares já reavaliados de forma independente em quedas reais (Bagalà 2012); '
      'o PIPTO é o limiar recente (2023) com código público; a CNN-LSTM é o TinyML mais recente (2026), que afirma generalizar bem. '
      '(3) <i>Por que essas bases:</i> são públicas; a SisFall é a mais usada da área e tem idosos; a MobiFall é celular real no bolso, o caso do Mova. '
      '(4) <i>Como medimos:</i> ajusta ou treina numa base e testa na outra sem mexer em nada; mesma pontuação para todos; separação por pessoa; '
      'intervalos de confiança por bootstrap. (5) <i>Resultado:</i> a IA é a melhor dentro da base e a que mais perde fora dela; o limiar certo (Kangas) '
      'quase não perde; limiares que dependem de picos altos quebram com o sensor do celular. (6) <i>Por que importa:</i> mostra que validar só na '
      'mesma base engana, e indica o que o Mova deve usar como linha de base.')

# ------------------------------------------------------------------ 1 contexto
d.h1('1. Contexto e pergunta de pesquisa')
d.p('O Mova é um aplicativo (Expo / React Native) que usa o acelerômetro do celular para detectar quedas de idosos e avisar cuidadores. '
    'O detector caseiro da primeira versão errava muito. Em vez de inventar um modelo novo, a equipe decidiu agir como pesquisadora: '
    'pegar algoritmos já publicados e medir, de forma controlada, se eles continuam funcionando fora das condições em que foram criados.')
d.p('A literatura mostra que isso é um problema real. Bagalà et al. (2012) testaram 13 algoritmos publicados em quedas reais de idosos: '
    'a sensibilidade média foi de 57% e houve de 3 a 85 alarmes falsos por dia, muito pior do que os artigos originais diziam. '
    'Revisões recentes (2024–2026) apontam que quase todos os estudos usam quedas simuladas e testam na mesma base em que treinaram. '
    'O artigo TinyML de Duan et al. (2026) afirma que algoritmos de limiar "generalizam mal", mas não testa nenhum limiar no seu protocolo. '
    'Este experimento faz esse teste.')
d.h2('Hipóteses')
d.ul(['<b>H1:</b> o aprendizado de máquina vai melhor dentro da base de treino, mas perde mais desempenho ao mudar de base; os limiares são mais estáveis.',
      '<b>H0:</b> a perda (Δ) é igual nos dois tipos de método.',
      '<b>H1-alternativa:</b> o aprendizado de máquina continua melhor e perde pouco (o que Duan et al. afirmam: ≈1%).'])

d.h1('2. O que mudou em relação ao plano, e por quê')
d.tab(['Plano original', 'O que foi feito', 'Motivo'],
      [['Treinar na KFall e testar na SisFall (protocolo de Duan et al.)',
        'Treinar na SisFall e testar na MobiFall, e o inverso',
        'A KFall exige pedido de acesso e o site dela estava bloqueado no ambiente de execução. A MobiFall (celular real no bolso) estava '
        'acessível e é <b>mais relevante para o Mova</b>, porque testa a ida da cintura para o celular.'],
       ['LOSO (deixar 1 sujeito de fora, 32 vezes)', 'Validação cruzada por sujeito em 5 partes',
        'O LOSO completo multiplicaria o tempo de treino por 7 a 8 (estimativa de mais de 12 horas em CPU). Os 5 folds por sujeito mantêm a regra essencial (nenhum sujeito no treino e no teste ao mesmo tempo).'],
       ['Só limiares com parâmetros publicados', 'Também limiares reajustados na base de treino',
        'A CNN é treinada na base de treino. Para a comparação ser justa, os limiares também foram reajustados nela.'],
       ['—', 'Experimentos de controle: saturação do sensor, rotação 3D, faixa ampliada de limiares, taxa de 200 Hz',
        'Para explicar por que cada método caiu, e não só medir quanto caiu.']],
      larg=[0.27, 0.27, 0.46])

# ------------------------------------------------------------------ 3 materiais
d.h1('3. Materiais')
d.h2('3.1 Bases de dados')
d.tab(['', 'SisFall', 'MobiFall v2.0'],
      [['Referência', 'Sucerquia, López & Vargas-Bonilla, <i>Sensors</i> 17(1):198, 2017', 'Vavoulas et al., IJMSTR 2014 (BMI Lab, Creta)'],
       ['Sensor e posição', 'dispositivo próprio (ADXL345, ±16 g) preso na <b>cintura</b>', '<b>smartphone</b> Samsung Galaxy S3 no <b>bolso da calça</b> (acelerômetro ±2 g)'],
       ['Taxa original', '200 Hz, regular', '≈90 Hz, irregular (com carimbo de tempo em ns)'],
       ['Pessoas', '23 jovens (19–30 anos) + 15 idosos (60–75); só 1 idoso (SE06) fez quedas', '24 adultos de 22 a 47 anos; ADLs de 9 deles'],
       ['Tentativas usadas', '4.396 (1.744 quedas; 2.652 ADLs; 14,2 h de ADL)', '630 (288 quedas; 342 ADLs; 2,5 h de ADL)'],
       ['Tipos', '15 quedas (F01–F15), 19 ADLs (D01–D19)', '4 quedas (FOL, FKL, BSC, SDL), 9 ADLs'],
       ['Onde obtivemos', 'espelho no GitHub (krishna-karthikk/SisFall-Dataset; 4.398 dos 4.505 arquivos)', 'espelho no GitHub (yehowlong/MobiAct_Dataset_v2.0-MobiFall_Dataset_v2.0)']],
      larg=[0.18, 0.41, 0.41])
d.p('"ADL" (<i>activities of daily living</i>) são as atividades normais: andar, sentar, subir escada, pular etc. Elas servem para medir os <b>falsos positivos</b>.')

d.h2('3.2 Como os algoritmos funcionam (o sinal não é "um número só")')
d.p('O acelerômetro mede a aceleração nos 3 eixos (x, y, z) dezenas de vezes por segundo. Neste estudo usamos 50 vezes por segundo, então cada tentativa '
    'de 15 s vira uma série de 750 × 3 valores. Os três algoritmos de limiar procuram o <b>formato</b> típico de uma queda nessa série:')
d.ol(['<b>Queda livre:</b> a aceleração total |a| = √(x²+y²+z²) cai bem abaixo de 1 g por uma fração de segundo;',
      '<b>Impacto:</b> logo depois aparece um pico alto;',
      '<b>Pós-queda:</b> a pessoa fica deitada (a gravidade passa a apontar para o lado do corpo) ou parada.'])
d.p('A magnitude |a| junta os 3 eixos num número por instante, mas a dimensão do tempo continua. A etapa de postura usa o vetor 3D da gravidade.')
d.tab(['Algoritmo', 'Regra (parâmetros publicados)', 'Fonte da implementação'],
      [['<b>Kangas et al. 2008</b> (variante 2)',
        'Queda livre: |a| < 0,6 g. Impacto em até 1 s, se <i>qualquer</i> um destes for verdadeiro: |a| ≥ 2,0 g; |a sem gravidade| ≥ 1,7 g; '
        'variação em 0,1 s ≥ 2,0 g; aceleração vertical estimada ≥ 1,5 g. Postura 2 s depois: componente vertical ≤ 0,5 g (deitado).',
        'Bagalà et al. 2012 (texto completo) e o porte aberto "Guardian" (licença MIT)'],
       ['<b>Bourke et al. 2010</b> ("Bourke3")',
        'Limiar inferior 0,65 g e de impacto 2,8 g. Tempo de descida ≤ 600 ms e de subida ≤ 350 ms. Velocidade vertical ≤ −0,7 m/s. '
        'Postura entre 1 e 3 s depois: inclinação > 60° em mais de 75% do tempo.',
        'Bagalà et al. 2012 (texto completo)'],
       ['<b>PIPTO</b> (Moutsis et al. 2023)',
        'Pares "baixo" (|a| < 6,5 m/s²) → "alto" (|a| > máx(média, 20) + 10 m/s², ou seja ≥ ≈3,06 g) em até 1,05 s, com até 0,85 s de duração. '
        'Depois, o sinal precisa ficar perto de 1 g e parado.',
        '<b>Código original dos autores</b> (GitHub), chamado sem modificação']],
      larg=[0.17, 0.58, 0.25])

d.h2('3.3 A rede neural: CNN-LSTM de Duan et al. (2026)')
d.p('A entrada são janelas de 4 s (200 amostras a 50 Hz) com 4 canais: ax, ay, az e a magnitude. Cada canal passa por uma convolução própria. '
    'Os resultados são combinados por outra convolução e depois por duas camadas LSTM (memória de curto e longo prazo) e três camadas densas. '
    'O total é de 21.434 parâmetros, conferido no código.')
d.box('<b>Correção encontrada no artigo.</b> A Tabela 1 de Duan et al. informa núcleo (8,1) na primeira convolução. Com esse núcleo, não dá para '
      'obter ao mesmo tempo a saída (24,1,16) e os 544 parâmetros que a própria tabela informa. O núcleo <b>(33,1) com passo 7</b> reproduz exatamente '
      'as dimensões, os parâmetros de cada camada e o total de 21.434. Usamos essa versão e recomendamos declarar isso no artigo.')
d.p('Treino como no artigo:')
d.ul(['otimizador Adam com taxa de aprendizado 0,001, 25 épocas;',
      'pesos de classe 0,8 para ADL e 0,2 para queda (escolha intencional dos autores para reduzir falsos positivos);',
      'normalização z-score;',
      'janela rotulada como queda se cobre ≥ 50% do intervalo da queda.'])
d.p('Duas suposições nossas, porque o artigo não informa: lote de 64 e ativação ReLU. Uma tentativa é classificada como queda se houver '
    '≥ k janelas positivas seguidas: k = 2 (regra do artigo) ou k = 1.')

# ------------------------------------------------------------------ 4 métodos
d.h1('4. Métodos (o processo científico passo a passo)')
d.h2('4.1 Pré-processamento, igual para todos')
d.ol(['Converter tudo para g com a gravidade incluída, e conferir que |a| ≈ 1 g com a pessoa parada: deu 0,997 g na SisFall e 1,009 g na MobiFall.',
      'Reamostrar para 50 Hz com filtro anti-<i>aliasing</i>. A MobiFall, que é irregular, foi antes interpolada numa grade de 100 Hz.',
      'Saturar em ±8 g, para simular um celular atual. Isso não altera nenhuma decisão, como mostra o controle da Seção 5.4.',
      '<b>Intervalo da queda</b>, usado só para rotular as janelas de treino da CNN: [pico − 1,0 s, pico + 0,5 s]. '
      'A SisFall e a MobiFall não marcam o instante da queda.',
      '<b>Referência de "em pé"</b> para a postura, por sujeito: a mediana da direção da gravidade no 1º segundo das tentativas.'])
d.h2('4.2 "Antes do treino" e "depois do treino"')
d.ul(['<b>Limiares publicados = antes de qualquer treino.</b> Usam os números dos artigos e são aplicados direto nas duas bases. '
      'Mostram o desempenho "de prateleira".',
      '<b>Limiares ajustados:</b> uma grade de valores (35 combinações no Kangas e 21 no Bourke3) é testada na base de treino, e fica a de maior F1. '
      'O desempenho "dentro da base" vem de validação cruzada por sujeito.',
      '<b>CNN-LSTM:</b> o desempenho "dentro da base" vem de validação cruzada por sujeito em 5 partes. Cada pessoa é testada por um modelo que nunca a viu. '
      'O desempenho "entre bases" vem de 3 modelos treinados com <i>toda</i> a base de treino (sementes diferentes), aplicados à outra base sem retreino. '
      'Vale a decisão da maioria das 3 sementes.'])
d.h2('4.3 Pontuação e métricas')
d.ul(['<b>Por tentativa (arquivo):</b> tentativa de queda com ≥ 1 alarme = acerto (verdadeiro positivo); tentativa de ADL com ≥ 1 alarme = falso positivo. '
      'É a mesma regra para todos, e a única possível na SisFall, que não marca o instante da queda.',
      '<b>Sensibilidade (SE):</b> fração das quedas detectadas. <b>Especificidade (SP):</b> fração das ADLs sem alarme. '
      '<b>F1:</b> média harmônica entre precisão e sensibilidade. <b>FA/h:</b> alarmes falsos por hora de atividade normal.',
      '<b>Δ (perda ao trocar de base)</b> = métrica na base de treino − métrica na outra base. Δ maior significa pior generalização.',
      '<b>Intervalo de confiança de 95% do Δ:</b> <i>bootstrap</i> de sujeitos. As pessoas são sorteadas com reposição 1.000 vezes, '
      'separadamente em cada base. Se o IC de um método não se sobrepõe ao de outro, a diferença entre eles é estatisticamente clara.'])
d.h2('4.4 Experimentos de controle (para explicar as quedas de desempenho)')
d.ul(['<b>Saturação do sensor:</b> limiares publicados na SisFall com o sinal cortado em ±16 (original), ±8, ±4, ±3 e ±2 g por eixo.',
      '<b>Rotação 3D:</b> a CNN treinada com cópias das janelas giradas aleatoriamente em 3D, para ficar insensível à orientação do sensor.',
      '<b>z-score "por base" × "do treino":</b> o artigo normaliza cada base com as próprias estatísticas; a forma justa usa só as do treino.',
      '<b>Faixa ampliada de limiares:</b> alguns parâmetros escolhidos ficaram na borda da grade. Repetimos o ajuste com uma faixa maior (84 e 60 combinações).',
      '<b>Taxa original de 200 Hz:</b> limiares publicados na SisFall sem reamostrar, para medir o efeito da redução para 50 Hz.'])
d.h2('4.5 Ambiente')
d.p('Python 3.13, NumPy, SciPy, pandas, TensorFlow 2.21 (CPU), 4 núcleos, 16 GB de RAM. O experimento principal levou 3 h 17 min. '
    'Todo o código está no notebook <font face="DVM">notebooks/estudo_limiar_vs_ml.ipynb</font>, que roda do início ao fim com um botão.')

d.br()
# ------------------------------------------------------------------ 5 resultados
d.h1('5. Resultados')
d.h2('5.1 Limiares "de prateleira" (sem treino) nas duas bases')
rows = []
for m in ('Kangas (publicado)', 'Bourke3 (publicado)', 'PIPTO (publicado)'):
    r = TSM.loc[m]
    rows.append([m.replace(' (publicado)', ''), pct(r['SisFall SE']), pct(r['SisFall SP']), f(r['SisFall F1']), f(r['SisFall FA/h'], 1),
                 pct(r['MobiFall SE']), pct(r['MobiFall SP']), f(r['MobiFall F1']), f(r['MobiFall FA/h'], 1)])
d.tab(['Algoritmo', 'SisFall SE', 'SisFall SP', 'SisFall F1', 'SisFall FA/h', 'MobiFall SE', 'MobiFall SP', 'MobiFall F1', 'MobiFall FA/h'], rows,
      larg=[0.16] + [0.105] * 8)
d.p('Na cintura (SisFall), o Kangas já é o melhor: SE 93,5%, SP 97,4% e 4,8 alarmes falsos por hora. O PIPTO detecta bem (81%), mas dispara muito: '
    '22 alarmes por hora, principalmente em pulos (D19) e tropeços (D18). No celular no bolso (MobiFall), só o Kangas continua funcionando. '
    'O Bourke3 detecta 9% das quedas e o PIPTO 4,5%.')

d.h2('5.2 Da cintura para o bolso: SisFall → MobiFall')
d.img('figs/f1_sis_mobi.png', 1.0, 'Figura 1. F1 por tentativa dentro da SisFall (azul; validação por sujeito) e na MobiFall sem retreino (laranja). '
      'À direita, a perda ΔF1 com IC 95% (bootstrap de sujeitos). Pontos azuis são limiares; pontos cinza escuro são variantes da CNN-LSTM.')
cols = ['Método', 'SisFall SE', 'SisFall SP', 'SisFall F1', 'MobiFall SE', 'MobiFall SP', 'MobiFall F1', 'MobiFall FA/h', 'ΔF1 [IC 95%]']
def linhas(T, a, bb):
    out = []
    for m, r in T.iterrows():
        out.append([m, pct(r[f'{a} SE']), pct(r[f'{a} SP']), f(r[f'{a} F1']), pct(r[f'{bb} SE']), pct(r[f'{bb} SP']), f(r[f'{bb} F1']),
                    f(r[f'{bb} FA/h'], 1), f'{f(r["ΔF1"],2)} [{f(r["ΔF1 IC95% inf"],2)}; {f(r["ΔF1 IC95% sup"],2)}]'])
    return out
d.tab(cols, linhas(TSM, 'SisFall', 'MobiFall'), larg=[0.25, 0.08, 0.08, 0.075, 0.085, 0.085, 0.08, 0.085, 0.16], fonte=6.6, destaque=[0, 3, 6])
d.cap('Tabela: SisFall → MobiFall. "z treino": normalização com as estatísticas da base de treino (justa). "z por base": cada base normalizada com as '
      'próprias estatísticas (protocolo do artigo). "rot": treinada com rotações 3D. k: nº de janelas positivas seguidas para declarar queda.')

d.h2('5.3 Do bolso para a cintura: MobiFall → SisFall')
d.img('figs/f1_mobi_sis.png', 1.0, 'Figura 2. O mesmo que a Figura 1, na direção inversa. Δ negativo significa que o método foi melhor na base nova do que na de treino.')
d.tab(cols[:1] + ['MobiFall SE', 'MobiFall SP', 'MobiFall F1', 'SisFall SE', 'SisFall SP', 'SisFall F1', 'SisFall FA/h', 'ΔF1 [IC 95%]'],
      linhas(TMS, 'MobiFall', 'SisFall'), larg=[0.25, 0.08, 0.08, 0.075, 0.085, 0.085, 0.08, 0.085, 0.16], fonte=6.6, destaque=[0, 3, 6])
d.p(f'Nesta direção, a CNN-LSTM treinada no bolso (k=1) mantém a sensibilidade na SisFall ({pct(TMS.loc["CNN-LSTM [z treino] k=1","SisFall SE"])}), '
    f'mas a especificidade despenca para {pct(TMS.loc["CNN-LSTM [z treino] k=1","SisFall SP"])}: são '
    f'{f(TMS.loc["CNN-LSTM [z treino] k=1","SisFall FA/h"],0)} alarmes falsos por hora. Andar, correr e subir escada viram "queda". '
    f'O Kangas reajustado no bolso funciona ainda melhor na cintura: F1 {f(TMS.loc["Kangas (ajustado)","SisFall F1"])}.')

d.h2('5.4 Por que Bourke3 e PIPTO caíram no celular: a faixa do sensor')
d.img('figs/picos.png', 0.78, 'Figura 3. Pico de |a| em cada tentativa de queda. Na MobiFall, nenhuma queda passa de 3,35 g, porque o acelerômetro do Galaxy S3 '
      'satura em ±2 g por eixo (máximo de 19,6 m/s² medido nos arquivos brutos). Na SisFall, o pico mediano das quedas é de 5,3 g.')
d.img('figs/ablacao_faixa.png', 0.7, 'Figura 4. Controle: sensibilidade dos limiares publicados na própria SisFall, cortando o sinal em faixas cada vez menores. '
      'Kangas, que não depende de um pico alto, não muda. PIPTO e Bourke3 caem quando a faixa chega a ±2 g.')
rows = []
for fx in ['sem limite (±16 g do sensor)', '±8 g', '±4 g', '±3 g', '±2 g']:
    s = ABL[ABL.faixa_g == fx].set_index('metodo')
    rows.append([fx] + [f'{pct(s.loc[m,"SE"])} / {pct(s.loc[m,"SP"])}' for m in ('Kangas', 'Bourke3', 'PIPTO')])
d.tab(['Faixa simulada', 'Kangas SE / SP', 'Bourke3 SE / SP', 'PIPTO SE / SP'], rows, larg=[0.31, 0.23, 0.23, 0.23])
d.p('A saturação explica boa parte, mas não tudo. Na MobiFall a queda foi maior que na SisFall saturada (PIPTO: 4,5% contra 36%). O resto vem da '
    '<b>posição</b>: no bolso o impacto chega amortecido pela coxa, e as quedas da MobiFall foram feitas com o celular no bolso do lado oposto ao da queda.')

d.h2('5.5 Por que a CNN-LSTM caiu: orientação, normalização e instabilidade')
d.ul(['<b>Orientação.</b> Com a pessoa em pé, a gravidade aparece em −y na SisFall e em +y na MobiFall: o sensor está "de cabeça para baixo" '
      'de uma base para outra. A CNN usa ax, ay e az crus e nunca viu sinais assim no treino. '
      f'Treinar com rotações 3D aleatórias reduziu a perda de {f(c1["ΔF1"],2)} para {f(cr["ΔF1"],2)} (k=1) e '
      f'subiu a especificidade na MobiFall de {pct(c1["MobiFall SP"])} para {pct(cr["MobiFall SP"])}.',
      '<b>Normalização do artigo ("z por base").</b> Normalizar cada base com as próprias estatísticas, como fez Duan et al., piorou a transferência '
      f'(F1 na MobiFall de {f(cz["MobiFall F1"])}). Isso mostra que o resultado de ≈1% de perda do artigo depende de as duas bases serem parecidas.',
      '<b>Instabilidade entre sementes.</b> Treinando a mesma rede 3 vezes, só mudando a semente aleatória, o F1 na MobiFall (k=1) variou de 0,44 a 0,77. '
      'Dentro da base essa variação é mínima (desvio da acurácia por janela de 0,3%). Um único treino pode dar uma impressão muito otimista ou pessimista.',
      '<b>Regra k=2 do artigo.</b> Exigir 2 janelas positivas seguidas reduz alarmes falsos dentro da base, mas fora dela derruba a sensibilidade '
      f'(MobiFall: {pct(c2["MobiFall SE"])}).'])
rows = []
for dirc in ('SisFall→MobiFall', 'MobiFall→SisFall'):
    for v in ('CNN-LSTM', 'CNN-LSTM rot'):
        a = JAN[(JAN.direcao == dirc) & (JAN.variante == v)]
        bz = JAN[(JAN.direcao == dirc) & (JAN.variante == f'{v} [z treino]')]
        rows.append([dirc, v, f'{pct(a.acc.mean())} ± {pct(a.acc.std())}', f'{pct(a.rec.mean())}', f'{pct(bz.acc.mean())}', f'{pct(bz.rec.mean())}', f'{pct(bz.prec.mean())}'])
d.tab(['Direção', 'Variante', 'Acurácia por janela, dentro', 'Recall por janela, dentro', 'Acurácia por janela, outra base',
       'Recall, outra base', 'Precisão, outra base'], rows, larg=[0.17, 0.13, 0.16, 0.13, 0.16, 0.12, 0.13])
d.cap('Métricas por janela, como as do artigo. Dentro da SisFall, a acurácia por janela (99,0%) reproduz os 99,3% de Duan et al. na KFall.')

d.h2('5.6 Onde cada método erra')
d.img('figs/fp_SisFall_MobiFall.png', 0.85, 'Figura 5. Fração das tentativas de cada ADL da MobiFall com alarme falso (detectores ajustados ou treinados na SisFall). '
      'O Kangas erra em correr (JOG) e pular (JUM). A CNN sem rotação erra em quase tudo que envolve movimento: andar, escada, correr, pular.')
d.img('figs/fp_MobiFall_SisFall.png', 0.85, 'Figura 6. O mesmo na SisFall, com detectores ajustados ou treinados na MobiFall. As quase-quedas D11 (desaba na cadeira) e '
      'D18 (tropeço) enganam o PIPTO; correr (D03–D04) engana o Kangas.')
rows = [[m, pct(SPG.loc[m, 'jovem']), pct(SPG.loc[m, 'idoso'])] for m in ('Kangas (publicado)', 'Kangas (ajustado)', 'Bourke3 (publicado)',
        'PIPTO (publicado)', 'CNN-LSTM [z treino] k=1', 'CNN-LSTM rot [z treino] k=1')]
d.tab(['Método (ajustado/treinado na MobiFall)', 'SP na SisFall, jovens', 'SP na SisFall, idosos'], rows, larg=[0.5, 0.25, 0.25])
d.p('Para Kangas e Bourke3, a especificidade com idosos e com jovens foi praticamente igual (diferença de até 1,5 ponto percentual). '
    'Para PIPTO e CNN, as atividades dos idosos geraram <i>menos</i> alarmes falsos, o que é coerente com movimentos mais lentos. '
    'Lembrete: na SisFall os idosos não caíram, então não dá para medir a sensibilidade em idosos.')

d.h2('5.7 Checagens de validade')
rows = []
for _, r in GRD.iterrows():
    m = r['Método']; dirc = r['direcao']; ba, bb = dirc.split('→')
    orig = (TSM if ba == 'SisFall' else TMS).loc[m]
    rows.append([dirc, m, f(orig[f'{ba} F1']), f(r[f'{ba} F1']), f(orig[f'{bb} F1']), f(r[f'{bb} F1'])])
d.tab(['Direção', 'Método', 'F1 treino (grade original)', 'F1 treino (grade ampliada)', 'F1 outra base (original)', 'F1 outra base (ampliada)'], rows,
      larg=[0.17, 0.2, 0.16, 0.16, 0.155, 0.155])
d.p('Ampliar a grade de limiares não muda nenhuma conclusão: as diferenças são de no máximo 0,03 no F1.')
if NAT is not None:
    rows = []
    for m in ('Kangas', 'Bourke3', 'PIPTO'):
        n = NAT[NAT.metodo == m].iloc[0]; a = ABL[(ABL.metodo == m) & (ABL.faixa_g.str.startswith('sem'))].iloc[0]
        rows.append([m, f'{pct(a.SE)} / {pct(a.SP)} / {f(a.F1)}', f'{pct(n.SE)} / {pct(n.SP)} / {f(n.F1)}'])
    d.tab(['Algoritmo (SisFall, publicado)', 'a 50 Hz: SE / SP / F1', 'a 200 Hz (original): SE / SP / F1'], rows, larg=[0.34, 0.33, 0.33])
    d.p(TEXTO_200HZ if 'TEXTO_200HZ' in globals() else '')
d.ul(['<b>Reprodução da CNN:</b> acurácia por janela de 99,0% dentro da SisFall, contra 99,3% de Duan et al. na KFall. A reimplementação se comporta como a original dentro da base.',
      '<b>Unidades:</b> |a| ≈ 1 g em repouso nas duas bases. O pico do rótulo e o pico do sinal foram conferidos no modo de teste do notebook.',
      '<b>Código do PIPTO:</b> roda sem modificação e sem erros internos em 5.026 tentativas.'])

d.br()
# ------------------------------------------------------------------ 6 discussão
d.h1('6. Discussão')
d.h2('6.1 O que os resultados dizem sobre as hipóteses')
d.ul(['<b>H1 é confirmada para o Kangas.</b> A CNN-LSTM perde de 0,43 a 0,72 de F1 da cintura para o bolso, e o Kangas perde 0,04 a 0,06. '
      'Os intervalos de confiança não se sobrepõem.',
      '<b>H1 é refutada para Bourke3 e PIPTO.</b> Eles perdem tanto ou mais que a CNN (ΔF1 de 0,59 e 0,73). A regra de decisão deles depende de um pico de impacto '
      'alto, e esse pico é uma característica do <i>sensor</i> (faixa, posição), não da queda em si.',
      '<b>A H1-alternativa (perda de ≈1%, Duan et al.) não se reproduz</b> quando a troca de base envolve mudar a posição e o aparelho. Não dá para afirmar o mesmo para '
      'KFall → SisFall, em que as duas bases são de cintura ou lombar e com quedas parecidas. Esse teste exige obter a KFall.'])
d.h2('6.2 Interpretação')
d.p('Um algoritmo de detecção de quedas generaliza bem quando a regra de decisão se apoia em características da <b>queda</b> e não do <b>sensor</b>. '
    'O Kangas combina quatro sinais diferentes de impacto (basta um) com a queda livre e a postura, e por isso sobrevive à saturação e à troca de posição. '
    'A CNN aprende detalhes da base de treino: orientação dos eixos, intensidade típica dos movimentos, até o jeito de cada voluntário cair. '
    'Esses detalhes não se transferem. Treinar com rotações ajuda, mas não resolve.')
d.p('Para o Mova, isso tem duas consequências práticas. (1) Um modelo de IA treinado numa base pública <b>não deve</b> ser levado direto para o app sem dados do próprio '
    'celular e posição; ele pode gerar dezenas de alarmes falsos por hora. (2) Um limiar simples e bem escolhido, como o Kangas, é uma linha de base forte, mas ainda gera '
    '5 a 15 alarmes falsos por hora em atividades como correr e pular. Para idosos, que raramente correm, esse número deve ser menor, mas isso precisa ser medido.')
d.h2('6.3 Comparação com a literatura')
d.ul(['Bagalà et al. (2012) mostraram que limiares perdem muito em quedas <i>reais</i> (SE média de 57%). Aqui mostramos que a troca de base com quedas <i>simuladas</i> '
      'já separa os métodos robustos dos frágeis.',
      'O PIPTO relata acurácia acima de 97% na SisFall (dado visto só em resumo de busca, a conferir). Aqui ele teve 85,5% de acurácia na SisFall a 50 Hz. '
      'A diferença pode vir da regra de pontuação, da forma de separar as tentativas (a taxa de amostragem foi descartada como causa na Seção 5.7) e de o PIPTO ter sido desenvolvido com a KFall e a MMsys.',
      'Revisões de 2024–2026 apontam a validação "na mesma base" como o principal problema da área. Este estudo mede esse problema de forma direta e reprodutível.'])

d.h1('7. Limitações e ameaças à validade')
d.ul(['<b>Quedas simuladas por adultos jovens</b> nas duas bases. Não há quedas reais de idosos; a SisFall tem só ADLs de idosos.',
      '<b>A KFall não foi usada</b>, então a comparação direta com o protocolo de Duan et al. (KFall → SisFall) continua pendente.',
      '<b>Bases obtidas por espelhos sem licença declarada.</b> O espelho da SisFall tem 4.398 dos 4.505 arquivos. Citem os artigos originais.',
      '<b>A MobiFall tem poucos sujeitos com ADL</b> (9) e o celular dela é antigo (±2 g). Celulares atuais costumam medir ±8 g ou mais, e o resultado do Bourke3 e do PIPTO deve '
      'melhorar com eles. Isso precisa de dados novos.',
      '<b>Intervalo da queda aproximado pelo pico</b> (pico − 1 s, pico + 0,5 s) para treinar a CNN, porque SisFall e MobiFall não marcam o instante da queda.',
      '<b>Validação cruzada em 5 partes em vez de LOSO</b>, por tempo de processamento. A regra de separar sujeitos foi mantida.',
      '<b>Parâmetros de Kangas e Bourke3</b> vieram do Bagalà 2012 e do código "Guardian", não dos PDFs originais. Conferir antes de publicar.',
      '<b>CNN reimplementada sem o código dos autores.</b> Lote e ativação são suposições, e o núcleo da 1ª convolução foi corrigido.',
      '<b>Pontuação por tentativa:</b> um alarme em qualquer ponto de uma tentativa de queda conta como acerto, mesmo fora do momento exato da queda.'])

d.h1('8. Decisões que a equipe precisa tomar')
d.ol(['<b>Título e recorte do artigo.</b> Sugestão: "Limiares ou aprendizado de máquina? Generalização entre bases na detecção de quedas com sensores inerciais, da cintura ao smartphone".',
      '<b>Pedir acesso à KFall</b> e rodar a direção KFall → SisFall. Basta acrescentar a direção no notebook, cerca de 4 h de CPU ou bem menos com GPU no Colab.',
      '<b>Conferir no PDF</b> os parâmetros de Kangas (Gait & Posture 2008) e Bourke3 (J. Biomech. 2010) e os números do PIPTO.',
      '<b>Opcional, para o app:</b> medir a faixa do acelerômetro dos celulares da equipe (expo-sensors) e gravar algumas ADLs no bolso para estimar alarmes falsos por hora.'])

d.h1('9. Reprodutibilidade')
d.ul(['Notebook: <font face="DVM">notebooks/estudo_limiar_vs_ml.ipynb</font>. Com <font face="DVM">MODO_DEMO = True</font>, roda em ≈5 min com dados sintéticos; '
      'com <font face="DVM">MODO_DEMO = False</font>, usa as bases reais (Seção 2 do notebook).',
      'Resultados brutos (CSV): <font face="DVM">docs/resultados_experimento/</font>. Inclui previsões por tentativa de todos os métodos, tabelas, erros por atividade, '
      'controles de saturação e de grade e a variação entre sementes.',
      'Sementes fixas (42) e versões das bibliotecas registradas. Mesmo assim, os resultados da CNN variam com a semente, como mostra a Seção 5.5.'])

d.h1('Referências')
for r in ['Bagalà F. et al. Evaluation of accelerometer-based fall detection algorithms on real-world falls. PLoS ONE 7(5):e37062, 2012.',
          'Bourke A. K. et al. Evaluation of waist-mounted tri-axial accelerometer based fall-detection algorithms during scripted and continuous unscripted activities. J. Biomechanics 43(15):3051–3057, 2010.',
          'Duan L.-C., Minh N.-N., Dung T.-C., Linh T.-T.-T. Energy-efficient TinyML approach for wearable fall detection on edge devices using spatial-temporal deep learning. Int. J. Technology 17(3):919–935, 2026. doi:10.14716/ijtech.v17i3.8445.',
          'Kangas M. et al. Comparison of low-complexity fall detection algorithms for body attached accelerometers. Gait & Posture 28(2):285–291, 2008.',
          'Moutsis S. N., Tsintotas K. A., Gasteratos A. PIPTO: Precise inertial-based pipeline for threshold-based fall detection using three-axis accelerometers. Sensors 23(18):7951, 2023.',
          'Sucerquia A., López J. D., Vargas-Bonilla J. F. SisFall: a fall and movement dataset. Sensors 17(1):198, 2017.',
          'Vavoulas G. et al. The MobiFall dataset: fall detection and classification with a smartphone. Int. J. Monitoring and Surveillance Technologies Research 2(1), 2014.',
          'Yu X., Jang J., Xiong S. A large-scale open motion dataset (KFall) and benchmark algorithms for detecting pre-impact fall of the elderly using wearable inertial sensors. Front. Aging Neurosci. 13:692865, 2021.']:
    d.p(r)
d.build()
print('ok', OUT)
