# Limiares ou TinyML: quem resiste à troca de base?

**Resposta curta:** a literatura de 2023 a 2026 sustenta a nova pergunta da equipe e deixa uma lacuna aberta para ela. Os trabalhos recentes concordam que detectores treinados em quedas simuladas **pioram muito quando mudam de base de dados ou passam para a vida real** ([Silva et al. 2024](https://www.sciencedirect.com/science/article/pii/S0263224124008777); [Casilari & Silva 2022](https://www.sciencedirect.com/science/article/pii/S0263224122010429)). As revisões de 2026 mostram que **98,5% dos estudos validam com quedas simuladas ou bases públicas** ([Ishaq et al. 2026](https://doi.org/10.3390/app16041929)). Mesmo assim, as buscas **não encontraram nenhum estudo de 2023 a 2026 que compare algoritmos de limiar e modelos leves de ML/DL sob o mesmo protocolo entre bases**. O artigo-alvo, Duan et al. 2026, afirma que limiares "generalizam mal", mas não mede limiares com o protocolo dele ([Duan et al. 2026](https://doi.org/10.14716/ijtech.v17i3.8445)). A queda de só ~1% que esse artigo relata entre KFall e SisFall contrasta com a degradação "notável" descrita no resto da literatura. Isso torna a pergunta testável e com chance real de um resultado surpreendente. Para o artigo da UNAMA, o desenho mais forte é **offline e só com bases públicas**: ajustar e treinar na KFall, testar na SisFall (separando o subconjunto de ADLs de idosos), e opcionalmente estender para celular no bolso (UMAFall ou MobiAct) e para alarmes falsos por dia na LTMM. Os três limiares entram com parâmetros publicados e com parâmetros ajustados na KFall. Também entra uma CNN-LSTM de ~21 mil parâmetros, reimplementada a partir do texto de Duan et al. A justificativa epidemiológica é sólida. A OMS estima **684 mil mortes por queda por ano** ([OMS](https://www.who.int/news-room/fact-sheets/detail/falls)). **1 em cada 4 idosos urbanos brasileiros caiu no último ano** ([Ministério da Saúde/ELSI-Brasil](https://www.gov.br/saude/pt-br/assuntos/noticias/2023/junho/no-brasil-prevalencia-de-quedas-entre-idosos-em-areas-urbanas-e-de-25)). Ficar mais de uma hora no chão ("long lie") traz complicações graves. Muitos números abaixo vieram apenas de trechos de busca (snippets), não da leitura do PDF. Eles estão marcados e listados na tabela de conferência ao final.

> **Como ler as marcas de confiança.** **[A]** = alta: fonte primária lida ou várias fontes concordantes. **[M]** = média: um único trecho de fonte primária. **[B]** = baixa: fonte secundária ou memória do pesquisador. **(snippet)** = o número veio do resumo do buscador e **precisa ser conferido no PDF antes de entrar no artigo**. Os fatos sobre Duan et al. 2026 foram **lidos diretamente no PDF** pelo coordenador e por isso recebem [A].

## O campo migrou para ML/DL, mas a validação continua presa ao laboratório

### O que saiu de 2023 a 2026

**Algoritmos de limiar.** O **PIPTO** (Moutsis, Tsintotas & Gasteratos, *Sensors* 2023) parece ser o pipeline de limiar mais recente com revisão por pares e código público.
- Desempenho relatado: sensibilidade de **90,40% na MMsys e 91,56% na KFall**, especificidade de **93,96% e 85,90%** [A, snippet] ([PMC10534597](https://pmc.ncbi.nlm.nih.gov/articles/PMC10534597/)).
- Os próprios autores admitem que o método **não supera as linhas de base de regressão logística e CNN** com que se compara. Admitem também que ele perde desempenho com o sensor na coxa em vez do peito (snippet) ([PMC10534597](https://pmc.ncbi.nlm.nih.gov/articles/PMC10534597/)).
- O código está no GitHub em Python e C++, sem licença visível [A, página aberta] ([GitHub smoutsis](https://github.com/smoutsis/fall_detection_through_acceleration_data)).

Não apareceu nenhum algoritmo de limiar novo para smartphone com código aberto e revisão por pares.

**ML leve.** O destaque é o **3s2sub** de Guo & Nakayama (*Sensors* 25(20):6500, 2025) [A/M, snippet] ([PMC12568134](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568134/)).
- Usa só o acelerômetro do celular. Uma janela de 3 s é dividida em duas subjanelas, de onde saem **44 atributos estatísticos**, classificados com kNN ou SVM.
- Resultados: **98,45% com LOSO na UniMiB SHAR**, **96,41% entre bases na MobiAct**, e **95,35% de sensibilidade e 98,12% de especificidade em quedas reais da FARSEEING**.
- Nenhum repositório de código foi encontrado.

**Séries temporais com código público.** Aderinola et al. (AALTD 2024) usaram classificadores de séries temporais da família ROCKET/Hydra. O nome da família veio só do snippet [M].
- Resultado: **F1 médio de 90,7% em quedas reais da FARSEEING**, com alarmes falsos estimados em cerca de 1 a cada 3 dias. É uma estimativa feita com o modelo, não medida em uso real.
- O código está em [mlgig/ts_fall_detection](https://github.com/mlgig/ts_fall_detection), com SisFall e FallAllD pré-processadas [A para o repositório] ([Springer](https://link.springer.com/chapter/10.1007/978-3-031-77066-1_4)).

**Deep learning.**
- Bartczak et al. (*Appl. Sci.* 2025) publicaram RNNs do tipo GRU com dados de celular da UniMiB-SHAR e pesos Keras ([MDPI](https://www.mdpi.com/2076-3417/15/12/6688); [GitHub](https://github.com/rsusik/fall_detection_rnn)).
- Um CNN-Transformer relata **99,95% de acurácia na SisFall**. Só reporta acurácia, o modelo é pesado e não há código (snippet) ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1746809424004701)).

**TinyML.** A maior parte mira pulseiras ou microcontroladores, como a MicroFallNet ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1574119225000355)). Há também vários repositórios amadores para ESP32 sem revisão por pares [B].

### O artigo-alvo: Duan et al. 2026

O artigo de Duan, Minh, Dung & Linh 2026 (*International Journal of Technology* 17(3):919–935) se encaixa nesse movimento. Os fatos abaixo foram lidos no PDF [A] ([doi:10.14716/ijtech.v17i3.8445](https://doi.org/10.14716/ijtech.v17i3.8445)).

| Aspecto | O que o artigo informa |
|---|---|
| Modelo | CNN-LSTM com **21.434 parâmetros** |
| Entrada | Janelas de 4 s a 50 Hz com 4 canais (ax, ay, az, RMS), passo de 2 s, z-score por base |
| Treino | KFall com LOSO, 32 sujeitos jovens |
| Resultado na KFall | Média por sujeito: **99,3% de acurácia e F1 de 98,97%** |
| Transferência para a SisFall (zero-shot) | **98,3% de acurácia e F1 de 97,9%** |
| Regra por tentativa na SisFall | Queda se ≥ 2 janelas consecutivas forem classificadas como queda |
| Embarcado | ESP32-S3: **113,6 ms por inferência e 5,78 mA** |
| Código | Não foi publicado |

O artigo é um bom "adversário" para a pergunta da equipe. É recente, leve, embarcável, e afirma ter generalização entre bases quase perfeita.

### O que as revisões dizem

As revisões recentes mostram que o gargalo não é algoritmo novo, e sim validação.
- **Warrington et al. 2021** (revisão guarda-chuva): ainda é preciso "pesquisa de alta qualidade para confirmar a acurácia em idosos frágeis em condições reais" [A] ([PMC8591794](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8591794/)).
- **Revisão de 2022 sobre smartphones** (*Frontiers in Public Health*): de 15 apps, 6 usavam limiar e 9 usavam ML, com sensibilidades entre **60,4% e 99,3%**. As quedas foram feitas apenas por jovens [A] ([Frontiers](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.996021/full)). A autoria não apareceu nos snippets, então conferir antes de citar.
- **Chen & Yao 2026** (revisão de escopo, 243 estudos): só **21 estudos** atendiam a critérios de uso real com idosos. A especificidade cai em campo por causa de movimentos bruscos que não são queda, como sentar rápido ou deixar objetos caírem [A, snippet] ([PubMed 41960380](https://pubmed.ncbi.nlm.nih.gov/41960380/)).
- **Ishaq et al. 2026**: **98,5% dos 128 estudos** usaram quedas simuladas ou bases públicas, e **só 2 (1,5%)** validaram com quedas reais e não planejadas [M-A, snippet] ([DOI](https://doi.org/10.3390/app16041929)).

Uma ressalva: Gorce & Jacquier-Bret 2025 ordenaram os vestíveis como os piores e o deep learning como o melhor. Isso conflita com outras revisões, provavelmente por critérios de inclusão diferentes ([PMC12609574](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12609574/)). O consenso não é total.

### Produtos comerciais

O mercado confirma a demanda, mas não traz evidência utilizável.
- **Apple Watch:** a detecção de quedas liga automaticamente para quem tem 55 anos ou mais. A Apple avisa que o relógio "não detecta todas as quedas" e que atividades de alto impacto podem disparar alarmes [A] ([Apple](https://support.apple.com/ml-in/108896)).
- **Google Pixel Watch:** a função foi lançada em 2023 com ML no próprio aparelho, e o Google também diz que ela "pode não detectar todas as quedas" [A] ([Google](https://blog.google/products/pixel/fall-detection-on-pixel-watch/)).
- **Samsung Galaxy Watch:** a detecção de "queda forte" vem desligada por padrão [M] ([9to5Google](https://9to5google.com/2023/03/21/galaxy-watch-5-fall/)).
- Nenhum fabricante publica sensibilidade nem taxa de alarmes falsos.
- A validação independente é escassa. Um app de terceiros para smartwatch, baseado em limiar, teve **~77% de sensibilidade e ~99% de especificidade** em quedas induzidas em 22 adultos saudáveis [A] ([Brew et al. 2022, JMIR](https://formative.jmir.org/2022/3/e30121)).

Conclusão de mercado: soluções fechadas e caras não substituem uma linha de base aberta e reproduzível.

### O que vale acrescentar ao estudo

1. **Citar o preprint "Beyond Simulated Benchmarks" (2026)** como a evidência mais direta a favor da H1. Ele relata que os métodos que vão melhor com dados simulados são os que mais degradam com mudança de domínio. Também relata que representações baseadas em grandezas físicas invariantes entre bases transferem melhor [M, snippet; é preprint, conferir] ([arXiv 2608.13197](https://arxiv.org/pdf/2608.13197)).
2. **Usar Silva et al. 2024 e Palmerini et al. 2020 como modelos de métricas.** Ambos usam alarmes falsos por hora ([Silva 2024](https://www.sciencedirect.com/science/article/pii/S0263224124008777); [Palmerini 2020](https://www.mdpi.com/1424-8220/20/22/6479)).
3. **Opcional: um terceiro braço de ML clássico** no estilo 3s2sub (atributos estatísticos + kNN/SVM). Isso permitiria separar "aprendizado" de "profundidade". Só vale a pena se os 44 atributos estiverem totalmente especificados no texto, o que ainda precisa ser conferido.

Não recomendamos acrescentar CSI de WiFi, Transformers pesados nem projetos TinyML amadores.

## Como justificar os três limiares, as três bases e a relevância clínica

### Por que esses três limiares

**Kangas 2008 (variante 2) e Bourke 2010 ("Bourke3")** se justificam por serem as referências clássicas que já foram **reavaliadas de forma independente em quedas reais** por Bagalà et al. 2012. Esse estudo reimplementou 13 algoritmos publicados e os testou em 29 quedas reais de pacientes de alto risco [A] ([PMC3353905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353905/)).
- **Resultado geral:** sensibilidade média de **57,0% ± 27,3%** e especificidade de **83,0% ± 30,3%**, "muito abaixo dos valores obtidos em quedas simuladas", com **3 a 85 alarmes falsos por dia**.
- **Kangas:** menos de 9 alarmes falsos, mas sensibilidade abaixo de 55% (snippet).
- **Bourke3:** foi o algoritmo de melhor equilíbrio, segundo o documento de pipeline da equipe (SE 82,8%, SP 96,7%). Esses números vieram de fonte secundária e devem ser conferidos no texto do Bagalà.

Uma revisão de escopo de 2018 resume a mesma queda: de **SE 0,91 e SP 0,99 em simulação para 0,57 e 0,83 em dados reais** [A] ([PMC6068511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068511/)).

Isso dá à equipe um **ponto de ancoragem externo** que nenhum modelo novo tem. Já se sabe quanto esses limiares degradam quando saem do laboratório. O **PIPTO** complementa esse par como representante moderno (2023), com código oficial ([GitHub](https://github.com/smoutsis/fall_detection_through_acceleration_data)).

Os argumentos a favor de limiares como linha de base são coerentes com as revisões:
- **não precisam de treino**, então não há vazamento entre treino e teste nos parâmetros publicados;
- cada limiar tem significado físico (g de pico, ângulo);
- o custo computacional é baixo;
- e "a acurácia depende muito dos limiares pré-definidos", enquanto o ML costuma ser mais preciso dentro da base [M] ([IIETA 2019](https://www.iieta.org/journals/isi/paper/10.18280/isi.240602)).

Os três algoritmos compartilham uma **estrutura multifase inspirada na física da queda**: queda livre, depois impacto, depois postura deitada. Isso torna a comparação com a CNN-LSTM uma comparação entre "conhecimento físico explícito" e "padrão aprendido". É exatamente o contraste que o preprint de 2026 aponta como decisivo para a transferência.

### Por que essas três bases

**SisFall** é aberta, tem 38 sujeitos (23 jovens e 15 idosos) e foi gravada a 200 Hz com sensor na cintura. É descrita como "benchmark bem conhecido" [M] ([PMC5298771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/)). Ela tem uma característica rara e valiosa para a pergunta: **os idosos fizeram apenas ADLs**, porque "não fizeram quedas por recomendação médica" (snippet). Os próprios autores mostraram que, como os movimentos dos idosos têm amplitude menor, **limiares treinados com jovens ficam enviesados para cima** e o desempenho cai ao validar com idosos [M, snippet] ([PMC5298771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/)). Por isso o subconjunto de ADLs de idosos deve ser analisado separadamente.

**KFall** (Yu, Jang & Xiong, KAIST, 2021) tem IMU de 9 eixos na lombar a 100 Hz, 32 jovens, 21 tipos de ADL e 15 tipos de queda, somando cerca de 5.075 tentativas, com rótulos de início e impacto sincronizados com vídeo [A] ([PMC8322729](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8322729/)). É a base de treino de Duan et al. e uma das bases de validação do PIPTO. Por isso é a escolha natural para "ajustar e treinar". Os autores admitem que ela contém apenas quedas simuladas por jovens do sexo masculino [M] ([Frontiers](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2021.692865/pdf)).

**LTMM** (PhysioNet) tem gravações de 3 dias com acelerômetro na lombar de **71 idosos da comunidade**, de 65 a 87 anos, e **não tem quedas** [A] ([PhysioNet](https://physionet.org/content/ltmm/)). Isso a torna adequada para uma única métrica: **alarmes falsos por dia na vida real**. Essa métrica é reconhecida na literatura: Bagalà usou alarmes por dia, Palmerini 2020 usou **0,56 alarme falso por hora** com SVM em 143 quedas reais [A] ([PMC7697900](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7697900/)), e Silva 2024 usou "taxa horária de alarmes falsos".

A coerência de posição é um argumento a favor do desenho principal: **KFall, SisFall e LTMM são todas de cintura ou lombar**. Assim, KFall→SisFall isola a mudança de sujeitos, protocolo e hardware, sem misturar a mudança de posição. O passo "rumo ao celular" exige outra base. As candidatas públicas com celular no bolso da calça são **UMAFall** (smartphone a 100 Hz; 7 dos 19 sujeitos não fizeram quedas) e **MobiAct** (57 sujeitos, ~87 Hz) [M] ([Casilari & Silva 2022](https://www.sciencedirect.com/science/article/pii/S0263224122010429); [UMAFall](https://www.researchgate.net/publication/318385531_UMAFall_A_Multisensor_Dataset_for_the_Research_on_Automatic_Fall_Detection)). O documento de pipeline da equipe registra que a MobiAct exige pedido de acesso, enquanto a UMAFall está no figshare. Portanto a **UMAFall é a opção de menor atrito**.

### Relevância epidemiológica

- **Mundo (OMS):** cerca de **684 mil quedas fatais por ano**. As quedas são a **segunda causa de morte por lesão não intencional**, e as maiores taxas estão acima dos 60 anos. **Mais de 80%** das mortes ocorrem em países de baixa e média renda [A, snippet; página da OMS não aberta] ([OMS](https://www.who.int/news-room/fact-sheets/detail/falls)). Atenção: o número antigo de 424 mil está desatualizado.
- **Long lie:** costuma ser definido como **mais de 1 hora no chão**. O protocolo do estudo britânico "Long Lies" estima que cerca de 1 em 3 pessoas acima de 65 anos cai por ano e que cerca de **1 em 5 dessas fica mais de uma hora no chão** [M] ([NIHR Open Research](https://openresearch.nihr.ac.uk/articles/6-19)). As complicações incluem hipotermia, desidratação, lesões por pressão e rabdomiólise [M] ([NHS Scotland](https://rightdecisions.scot.nhs.uk/media/5jbdqvih/care-of-residents-within-a-care-home-setting-who-are-at-risk-of-long-lie.pdf)). A referência clássica é Fleming & Brayne 2008 (*BMJ*), uma coorte de pessoas com mais de 90 anos ([BMJ](https://www.bmj.com/content/337/bmj.a2227.abstract)). **Não usar o "30% ficaram mais de 1 h" sem conferir no PDF.**
- **Brasil:**
  - A **ELSI-Brasil** registrou **25% de prevalência de quedas em 12 meses** entre idosos urbanos [A] ([Ministério da Saúde](https://www.gov.br/saude/pt-br/assuntos/noticias/2023/junho/no-brasil-prevalencia-de-quedas-entre-idosos-em-areas-urbanas-e-de-25)).
  - **Novaes et al. 2023** (*Ciência & Saúde Coletiva*) mostram crescimento contínuo das mortes por queda de 2000 a 2020 [M] ([SciELO](https://www.scielo.br/j/csc/a/y3H93qVXYZHtfjpRnm4ykdd/?format=html&lang=pt)).
  - **Lima et al. 2022** contaram **1.746.097 internações no SUS**, com custo de **R$ 2,3 bilhões** [M; conferir o período] ([SciELO SP](https://scielosp.org/pdf/ress/2022.v31n1/e2021603/pt)).
  - A prevalência da ELSI vem de autorrelato e os números do DATASUS são registros administrativos. São medidas diferentes e não devem ser comparadas diretamente.
  - Não foram levantados dados do Pará ou de Belém. Se necessário, consultar o TabNet (SIH/SIM, CID-10 W00–W19, 60 anos ou mais).

## A pergunta nova tem apoio indireto forte e uma lacuna direta

### O que a literatura já mostra

A literatura de 2022 a 2026 é consistente: **quem vai bem numa base simulada vai pior fora dela**.
- **Silva, Casilari & García-Bermúdez 2024** (*Measurement* 235:114992) treinaram 13 detectores de IA em até 11 bases de laboratório e os testaram em quedas reais e em monitoramento de longo prazo. Encontraram "degradação notável em todas as métricas", com os modelos tendendo a "sobreajustar os padrões das quedas emuladas". O trecho de busca fala em ~0,61 a 2,74 falsos positivos por hora para LSTM/CNN [M, snippet; números a conferir] ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0263224124008777); [RIUMA](https://riuma.uma.es/entities/publication/044b23da-8d37-4245-9392-20de3918fc18)).
- O estudo do grupo Casilari na **ACM PETRA 2022** mostrou que uma CNN que vai bem numa base frequentemente não mantém o desempenho em outra [M] ([ACM](https://dl.acm.org/doi/10.1145/3529190.3529191)).
- **Fula & Moreno 2024** relatam uma acurácia entre bases de **78,51 ± 4,06%** em pulso e alertam que treinar e testar em escopo pequeno gera taxas otimistas demais [M, snippet] ([PubMed 38475215](https://pubmed.ncbi.nlm.nih.gov/38475215)).
- Um estudo de 2025 com aparelhos comuns encontrou **F1 offline de 0,99**, mas alarmes falsos subiram em casa, ligados à marcha individual [M, snippet] ([PMC12431052](https://pmc.ncbi.nlm.nih.gov/articles/PMC12431052/)).
- Nos limiares, a evidência de degradação é a do Bagalà 2012, mas para quedas reais, não para troca de base simulada.

### A lacuna

A busca não encontrou nenhum estudo que **meça limiares e ML/DL leve sob o mesmo protocolo de transferência entre bases**.
- A comparação do próprio PIPTO com LR e CNN é interna, sem transferência ([PMC10534597](https://pmc.ncbi.nlm.nih.gov/articles/PMC10534597/)).
- O Silva 2024 avalia só detectores de IA.
- O Duan 2026 afirma, citando Yu et al. 2023, que limiares "sofrem com alta taxa de falsos positivos e baixa generalização", mas **não roda nenhum limiar** com o seu protocolo LOSO e zero-shot.
- Não foi encontrada nenhuma reavaliação de PIPTO, Kangas ou Bourke3 publicada entre 2023 e 2026. Os artigos que citam esses trabalhos no Google Scholar não foram verificados, então ainda pode existir alguma.

A formulação correta no artigo é **"não encontramos"**, e não "não existe".

### Por que a queda de ~1% de Duan não encerra a questão

A queda de ~1% de Duan et al. (de 99,3% para 98,3% de acurácia) não refuta a H1. Ela **define o desafio**. Há quatro razões plausíveis para a transferência ter sido tão boa, e todas são testáveis:

1. **O par KFall→SisFall é "fácil":** as duas bases são de cintura ou lombar, com quedas simuladas por jovens em laboratório.
2. **A regra de ≥ 2 janelas consecutivas** muda o ponto de operação em relação à avaliação por janela.
3. **O z-score calculado por base usa estatísticas da base de destino.** É uma forma branda de adaptação ao domínio de teste, que não existiria num celular recebendo um sinal novo.
4. **Acurácia e F1 dependem do equilíbrio de classes da SisFall** e escondem os falsos positivos por tipo de ADL. O próprio artigo lista **ADLs D10 e D17 classificadas como queda** e **quedas F11 e F15 perdidas**.

Por isso, o resultado "o ML degradou pouco" seria cientificamente interessante, desde que acompanhado da mesma análise para os limiares e da extensão para o bolso. A posição muda tudo para os limiares com regra de postura. Os autores do PIPTO já relatam perda com o sensor na coxa (snippet). Com o celular no bolso da calça, a coxa fica horizontal ao sentar, o que imita "deitado". É aí que a hipótese pode se inverter.

### Pergunta e hipóteses propostas

**Pergunta de pesquisa.** Quando transferidos de uma base de quedas simuladas para outra (KFall → SisFall) e para o celular no bolso (→ UMAFall ou MobiAct), os algoritmos de limiar (Kangas-2, Bourke3, PIPTO) degradam tanto quanto uma CNN-LSTM leve (Duan et al. 2026) avaliada sob o mesmo protocolo?

- **H1 (principal):** a CNN-LSTM tem desempenho maior dentro da base (KFall, LOSO), mas sofre uma **degradação Δ = desempenho na própria base − desempenho em outra base** maior que a dos limiares com parâmetros publicados. A especificidade nas ADLs de idosos da SisFall é o ponto em que essa diferença deve aparecer.
- **H0:** não há diferença entre limiares e CNN-LSTM no Δ. O intervalo de confiança de 95% da diferença de Δ inclui zero.
- **H1-alternativa:** os limiares degradam mais. É o que Duan et al. afirmam sem medir.
- **H2 (opcional, posição):** a passagem da cintura para o bolso degrada mais os algoritmos com regra de postura (Kangas e Bourke3) do que a CNN-LSTM.
- **H3 (opcional, vida real):** na LTMM, os limiares com parâmetros publicados geram menos alarmes falsos por dia do que a CNN-LSTM e do que as versões ajustadas na KFall.

Qualquer resultado é publicável, porque cada um responde a uma afirmação existente na literatura.

## Desenho experimental offline com regras de comparação justa

### Etapas

O professor recomendou não construir o app e fazer os testes ao mesmo tempo. O desenho abaixo segue essa orientação: **é inteiramente offline, só com bases públicas, sem voluntários e sem app**. As etapas de app e de teste com voluntários do documento de pipeline viram trabalho futuro.

| Etapa | Treino ou ajuste | Teste | Métrica principal | Obrigatória? |
|---|---|---|---|---|
| E1. Dentro da base | KFall (LOSO, 32 folds) | Sujeito deixado de fora na KFall | SE, SP, F1 por tentativa | Sim |
| E2. Entre bases | KFall inteira | SisFall inteira, separando jovens (SA) e idosos (SE) | SE e SP; Δ = E1 − E2 | Sim |
| E3. Rumo ao celular | KFall | UMAFall (celular no bolso) ou MobiAct | SE e SP; Δ | Opcional, recomendada |
| E4. Vida real | KFall | LTMM (sem quedas) | Alarmes falsos por dia efetivamente usado | Opcional |

### As quatro condições comparadas

- **(a) Limiares com parâmetros publicados.** Kangas-2, Bourke3 e PIPTO exatamente como especificados. Não há treino, e o "dentro da base" é simplesmente o desempenho na KFall.
- **(b) Limiares ajustados na KFall.** Busca em grade dos limiares principais, como 0,6 g e 2,0 g do Kangas e LFT 0,65 g e UFT 2,8 g do Bourke3, feita **dentro dos folds de treino do LOSO**. Assim o ajuste tem a mesma chance de sobreajuste que o ML. Reportar à parte como "versão ajustada", nunca como o algoritmo original.
- **(c) CNN-LSTM reimplementada.** Seguir o texto: janelas de 200×4, passo de 2 s, Adam com lr 0,001, 25 épocas, pesos de classe 0,8 para ADL e 0,2 para queda. É o inverso do usual, mas é intencional: o PDF (p. 924–925) explica que dar mais peso à queda aumentou muito os falsos positivos nos testes preliminares. Treinar com **5 sementes** e reportar média ± desvio.
- **(d) Opcional:** um kNN/SVM com atributos estatísticos, no estilo 3s2sub.

### Regras de comparação justa

1. **Mesma reamostragem.** Tudo vai para **50 Hz**, com filtro anti-aliasing antes de decimar: SisFall de 200 para 50 Hz, KFall de 100 para 50 Hz, LTMM e UMAFall também para 50 Hz. As unidades vão para g com gravidade. O sinal é saturado em ±8 g para simular o celular, com uma análise de sensibilidade sem saturação.
   - **Exceção:** o Bourke3 pode rodar também a 100 Hz como análise de sensibilidade.
   - Os coeficientes do filtro do Kangas valem apenas para 50 Hz.
2. **Mesma pontuação por tentativa.**
   - Uma tentativa de queda é **VP** se houver pelo menos um alarme. Uma tentativa de ADL é **FP** se houver qualquer alarme.
   - A CNN é reportada com a regra de Duan (≥ 2 janelas consecutivas) **e** com a regra de ≥ 1 janela, para que a regra não seja confundida com o modelo.
3. **Mesma normalização sem espiar o teste.** O z-score da CNN usa estatísticas da KFall de treino. A versão "z-score por base", como em Duan, é reportada apenas como análise secundária, explicitando que ela usa a base de destino.
4. **LOSO por sujeito.** Isso vale para a CNN e para o ajuste dos limiares.
5. **A degradação Δ como métrica principal.** Δ = desempenho na própria base − desempenho em outra base, para sensibilidade, especificidade e F1. Os intervalos de confiança são calculados por **bootstrap por sujeito**. Proporções usam IC de Wilson. Diferenças pareadas entre algoritmos nas mesmas tentativas são testadas com McNemar.
6. **Falsos positivos por código de ADL** (D01 a D19 na SisFall) e **quedas perdidas por tipo** (F01 a F15). Isso permite verificar se D10, D17, F11 e F15 se repetem.
7. **O subconjunto de idosos da SisFall separado.** São as ADLs de SE01 a SE15. O documento de pipeline indica que **SE06 tem quedas**; conferir e tratar esse sujeito à parte. Nesse subconjunto só se mede especificidade.
8. **Alarmes falsos por dia ou por hora** quando houver gravação contínua (LTMM). O denominador são as horas em que o sensor esteve de fato no corpo.
9. **Funil por estágio** dos limiares: queda livre → impacto → postura. Ele mostra qual etapa segura ou deixa passar os falsos positivos.

### Ameaças à validade

**Validade interna.**
- A CNN-LSTM é uma **reimplementação sem código**, então a primeira tarefa é tentar reproduzir os ~99% na KFall com LOSO. Se não conseguir, a equipe deve declarar isso.
- A **Eq. 4 de Duan define recall como TP/(TP+TN)**, o que é um erro tipográfico. Usar TP/(TP+FN) e não copiar a fórmula.
- Os parâmetros do Kangas e do Bourke3 vêm em parte de fontes secundárias (Bagalà, o porte Guardian). O mapeamento das variantes 2a e 2b do Kangas não foi confirmado.
- No PIPTO, a unidade de tempo dos limites internos é ambígua. É preciso rodar o Python original antes de portar o código.

**Independência dos dados.**
- O **PIPTO foi desenvolvido e avaliado com a KFall pelos próprios autores**. Logo, os parâmetros publicados dele não são independentes da KFall.
- O documento de pipeline também cita, por fonte secundária, uma acurácia acima de 97% do PIPTO na SisFall. Se isso se confirmar, a SisFall também não é totalmente "nova" para ele. É preciso declarar isso.

**Validade de construto.**
- A KFall rotula início e impacto, enquanto a SisFall só tem o rótulo por arquivo.
- As tentativas de ADL longas têm mais janelas e por isso mais chances de falso positivo para a CNN.
- Acurácia e F1 dependem da proporção de classes, então é preciso priorizar sensibilidade, especificidade e alarmes por dia.

**Validade externa.** É a mais séria.
- **Todas as quedas são simuladas por jovens**. A KFall tem só homens jovens.
- Na SisFall, os idosos não caíram.
- A LTMM não tem quedas.
- A cintura não é o bolso.
- Os sensores da SisFall (ADXL345 ±16 g) não são o IMU de um celular.

Nenhum resultado diz qual algoritmo detecta melhor quedas reais de idosos. O estudo responde "qual degrada menos sob mudança de domínio". Para quedas reais, a única via seria pedir acesso à FARSEEING, que continua disponível só sob solicitação ([Klenk et al. 2016](https://link.springer.com/article/10.1186/s11556-016-0168-9)).

### Como os algoritmos "veem" o sinal

Esta seção ajuda a explicar os algoritmos no texto do artigo. Nenhum dos métodos usa "um valor só".

**A entrada.** Todos recebem uma **série temporal do acelerômetro de 3 eixos** (ax, ay, az, em g, com gravidade), amostrada de 50 a 200 vezes por segundo.

**A magnitude.** A magnitude SV = √(ax² + ay² + az²) é calculada **a cada amostra**.
- Ela **descarta a direção** (junta os três eixos num número), mas **preserva o tempo**.
- Em repouso SV ≈ 1 g.
- Na queda livre SV cai abaixo de ~0,6 g.
- No impacto SV sobe acima de ~2 a 3 g.

**Os limiares** são regras sobre a **sequência temporal** dessa magnitude. Por exemplo: "SV caiu abaixo de 0,6 g e, em até 1 s, passou de 2 g".

**A postura** usa o **vetor de gravidade em 3D**. É obtido com um filtro passa-baixa ou uma média móvel de 0,4 a 0,5 s sobre os três eixos. O algoritmo mede o ângulo entre esse vetor e a referência "em pé". Se o ângulo passar de 60° durante 1 a 3 s após o impacto, a pessoa é considerada deitada. Aqui a direção importa, e é por isso que a posição do aparelho (cintura ou bolso) afeta tanto Kangas e Bourke3.

**A CNN-LSTM** recebe a mesma série recortada em janelas de 4 s (200 amostras × 4 canais: os três eixos mais a magnitude RMS). Em vez de limiares escritos à mão, ela aprende filtros (CNN) e dependências temporais (LSTM). Por isso pode capturar padrões que os limiares ignoram, e também pode decorar padrões específicos da base de treino.

## Como explicar ao professor

**O que mudou.** A equipe deixou de "construir o app e testar ao mesmo tempo" e passou a fazer **um estudo comparativo offline, reprodutível e só com bases públicas**.

**Por que isso não é menos ciência.** O estudo de referência da área, Bagalà 2012, fez exatamente isto: reimplementou algoritmos publicados e os testou em dados que os autores não usaram ([PMC3353905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353905/)).

**A pergunta é falsificável.** Um artigo de 2026 afirma que limiares generalizam mal e que a sua CNN-LSTM perde só ~1% ao trocar de base, mas nunca testou os limiares sob o mesmo protocolo. A equipe vai medir as duas coisas nas mesmas tentativas, com as mesmas regras.

**Qualquer resultado é publicável:**
- se o ML degradar mais, isso contradiz a afirmação do artigo;
- se degradar menos, isso confirma a afirmação com uma evidência que hoje falta;
- se houver empate, os limiares, sem treino e interpretáveis, passam a ser uma alternativa defensável.

**Riscos.**
- **Ética:** não há coleta com seres humanos. Bases públicas e anonimizadas provavelmente dispensam o CEP, mas a equipe deve confirmar com o orientador.
- **Prazo:** o mínimo viável é E1 + E2. E3 e E4 entram se sobrar tempo.

**O que o app vira.** Trabalho futuro, construído em cima do algoritmo que se mostrar mais robusto. A arquitetura de "detector em TypeScript puro" do pipeline permite reaproveitar o mesmo código depois.

### Tabela de conferência antes de citar

| Afirmação | Fonte | Status |
|---|---|---|
| PIPTO: SE 90,40 / 91,56%; SP 93,96 / 85,90%; fraco na coxa | [PMC10534597](https://pmc.ncbi.nlm.nih.gov/articles/PMC10534597/) | snippet; conferir tabelas |
| Bagalà: SE 57,0 ± 27,3%; SP 83,0 ± 30,3%; 3 a 85 alarmes falsos por dia; Bourke3 com SE 82,8% e SP 96,7% | [PMC3353905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353905/) | médias [A]; números do Bourke3 de fonte secundária |
| Silva 2024: 0,61 a 2,74 falsos positivos por hora | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0263224124008777) | snippet |
| Ishaq 2026: 98,5% simuladas, 2 estudos com quedas reais | [DOI](https://doi.org/10.3390/app16041929) | snippet |
| Chen & Yao 2026: 243 estudos, 21 com uso real | [PubMed](https://pubmed.ncbi.nlm.nih.gov/41960380/) | snippet |
| "Beyond Simulated Benchmarks" (preprint) | [arXiv](https://arxiv.org/pdf/2608.13197) | snippet; é preprint |
| Guo & Nakayama 2025: números e lista dos 44 atributos | [PMC12568134](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568134/) | snippet |
| SisFall: viés de limiar em idosos; idosos sem quedas; SE06 | [PMC5298771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/) | snippet; SE06 vem do documento de pipeline |
| Taxa de amostragem e horas de uso da LTMM | [PhysioNet](https://physionet.org/content/ltmm/) | 100 Hz pelo documento de pipeline; conferir no cabeçalho |
| OMS: 684 mil mortes por ano; mais de 80% em países de baixa e média renda | [OMS](https://www.who.int/news-room/fact-sheets/detail/falls) | snippet; a página não abriu |
| "1 em 5 fica mais de 1 h no chão"; percentuais de Fleming & Brayne | [NIHR](https://openresearch.nihr.ac.uk/articles/6-19); [BMJ](https://www.bmj.com/content/337/bmj.a2227.abstract) | [M]; Fleming & Brayne não conferido |
| Período coberto por Lima et al. 2022 (R$ 2,3 bilhões) | [SciELO SP](https://scielosp.org/pdf/ress/2022.v31n1/e2021603/pt) | conferir |
| Autoria da revisão Frontiers 2022 | [Frontiers](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.996021/full) | autores não confirmados |
| Yu et al. 2023, citado por Duan | referência no PDF de Duan | não localizado nesta pesquisa; ler antes de citar |
| Pesos de classe de Duan (0,8 ADL / 0,2 queda) | [Duan 2026](https://doi.org/10.14716/ijtech.v17i3.8445) | lido no PDF; confirmar a qual classe se refere |

## Conclusão

A contribuição do estudo é colocar limiares e deep learning leve **no mesmo protocolo de transferência**, coisa que a literatura recente pressupõe mas não mede. O resultado de Duan et al. funciona menos como prova e mais como hipótese a testar: uma transferência de 99% para 98% entre duas bases de cintura com quedas simuladas por jovens pode refletir a semelhança entre as bases, e não a robustez do modelo. A mudança de posição para o bolso e a especificidade nas ADLs de idosos são os testes que podem separar as duas explicações. Também é onde os limiares, por dependerem de uma regra explícita de postura, têm mais a perder e mais a revelar.

Há uma implicação prática para o Mova. Se os limiares com parâmetros publicados degradarem menos que suas versões ajustadas na KFall e que a CNN, o "ajuste fino em base simulada" passa a ser um risco, e não um ganho. Nesse caso, o app futuro deveria priorizar regras físicas transparentes, com filtragem posterior de falsos positivos aprendida no uso real. Se o ML vencer também fora da base, o embarque de modelos de ~21 mil parâmetros, já demonstrado em ESP32, torna viável colocá-lo no celular. Em qualquer um dos casos, o estudo offline responde a pergunta antes de se gastar tempo construindo o app.
