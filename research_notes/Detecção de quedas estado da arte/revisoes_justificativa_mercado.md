# Systematic reviews (2021–2026) on wearable/smartphone fall detection: arguments to justify a student replication study

Method note: WebFetch failed with DNS errors for who.int, scielo.br and frontiersin.org in this environment, and pmc/mdpi/doi are blocked. **All findings below come from search-engine snippets or summaries, not full-text reading**, unless stated otherwise. Confidence: HIGH = consistent across several snippets/indexes (PubMed, PMC, DOAJ); MEDIUM = one snippet, plausible; LOW = secondary or commercial source, or my own recall. Verify exact numbers in the PDFs before citing them in the paper.

## Q1. Recent systematic, scoping and umbrella reviews (2021–2026): who, where, and what they conclude

### Takeaway
Reviews from 2021 to 2026 agree that wearable/IMU fall detection is technically mature in the lab but largely unvalidated in real life. Between 50% and 98.5% of studies use simulated falls, only a handful use real falls of older adults, and every review asks for real-world validation and more standardized evaluation.

### Cited Findings
- **Warrington, Shortis & Whittaker (2021), "Are wearable devices effective for preventing and detecting falls: an umbrella review (a review of systematic reviews)", *BMC Public Health*, DOI 10.1186/s12889-021-12169-7.** The umbrella review pooled 7 systematic reviews. Heterogeneity in methods and reporting ruled out a meta-analysis. Three of the reviews reported mean sensitivity ≥93.1% and specificity ≥86.4%. Trunk, foot or leg placement gave the highest accuracy, and most devices used accelerometers, often with gyroscopes. Conclusion: "further high-quality research is needed to confirm accuracy in frail older people in real-world settings." (HIGH) — [PMC8591794](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8591794/); [Springer](https://link.springer.com/article/10.1186/s12889-021-12169-7)
- **"Fall detection using accelerometer-based smartphones: Where do we go from here?" (2022), *Frontiers in Public Health*, DOI 10.3389/fpubh.2022.996021.** This systematic review covers smartphone-only fall detection. It screened 267 studies and kept 15 smartphone-accelerometer apps: 6 threshold-based and 9 ML. Reported sensitivities ranged from 60.4% to 99.3%. The authors flag restricted ADL scope, young fallers, and limitations in experimental set-ups. (HIGH for the numbers. Authors not shown in the snippets; I recall Stampfler, Elgendi, Fletcher & Menon, LOW confidence, so verify.) — [Frontiers](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.996021/full); [PMC9618891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9618891/)
- **Chen & Yao (2026), "Fall detection and pre-impact prediction technologies in older adults: a scoping review of translational maturity and public health integration", *Frontiers in Public Health*, DOI 10.3389/fpubh.2026.1737644 (PRISMA-ScR; PubMed, WoS, Scopus and IEEE Xplore, Jan 2005–Sep 2025; 243 studies).**
  - More than half of the studies relied mainly on simulated falls in the laboratory.
  - Only 21 studies met the criteria for real-world use with older adults.
  - Wearable IMU post-fall detection has the strongest technical validation, but evidence on adherence, workflow fit and sustained real-world use is thin.
  - Real-world validation often showed lower specificity, because false positives rose during abrupt non-fall activities such as rapid sitting or dropping objects.
  - Conclusion: translational maturity is uneven, and real-world validation is needed. (HIGH)
  - Sources: [PubMed 41960380](https://pubmed.ncbi.nlm.nih.gov/41960380/); [PMC13056853](https://pmc.ncbi.nlm.nih.gov/articles/PMC13056853/); [Frontiers](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2026.1737644/full)
- **Ishaq, Guastella, Sutera & Muscato (2026), "A Systematic Review of Fall Detection and Prediction Technologies for Older Adults: An Analysis of Sensor Modalities and Computational Models", *Applied Sciences* 16(4):1929, DOI 10.3390/app16041929 (covers 2008–2025).**
  - 128 of the detection studies (98.5%) validated on simulated falls or public datasets. Only 2 (1.5%) validated against naturally occurring, unanticipated falls.
  - Wearable IMU accuracy was reported at 90.3–99.9%, but only under controlled conditions.
  - Recommendations: real-world validation, attention to energy efficiency and user acceptance, and multimodal systems. (MEDIUM-HIGH. The venue comes from the DOI prefix and a university repository record.)
  - Sources: [DOI](https://doi.org/10.3390/app16041929); [IRIS Unict](https://www.iris.unict.it/handle/20.500.11769/705569)
- **"Enhancing Real-World Fall Detection Using Commodity Devices: A Systematic Study" (2025, PMC12431052 / PubMed 40942679).** This is an empirical study, not a review, but it fits the student project closely.
  - Existing systems still struggle to detect soft falls in real-world settings, and performance drops notably when models trained offline are deployed in real conditions.
  - One cited device study fell from F1 0.87 to 0.73 in real-world testing.
  - Retraining with feedback from 10 participants reached F1 0.92 and reduced false positives.
  - The authors note that smartwatch and smartphone IMUs are not clinical-grade. (MEDIUM)
  - Source: [PMC12431052](https://pmc.ncbi.nlm.nih.gov/articles/PMC12431052/)
- **Other reviews surfaced, details not verified:**
  - "Fall Detection and Prevention Technologies for Older Adults: A Scoping Review" — [PMC12761284](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12761284/)
  - "Digital Healthcare Approaches for Fall Detection and Prediction in Older Adults: A Systematic Review of Evidence from Hospital and Long-Term Care Settings" (*Medicina* 2025; 33 studies: 20 detection systems and 13 prediction models) — [PMC12654721](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12654721/)
  - "A review of wearable sensors based fall-related recognition systems" (*Eng. Appl. of AI*, 2023) — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S095219762300177X)
  - Gorce & Jacquier-Bret (2025), on AAL/smart-home detection performance. Its ANOVA ranked wearables worst and deep learning best, which conflicts with the Ishaq et al. ranking, probably because inclusion criteria differ — [PMC12609574](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12609574/)
- **Pre-2021 background still widely cited:**
  - The scoping review on real-world evaluation methods (2018) — [PMC6068511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068511/)
  - The earlier systematic review of fall detection devices with older adults (PubMed 24406708), which found that only 7.1% of projects monitored older adults in real-world settings and called for standardized evaluation — [PubMed](https://pubmed.ncbi.nlm.nih.gov/24406708/)

### Inferences
- The most useful reviews to cite for the "gap" are Warrington 2021 (umbrella), Frontiers 2022 (smartphone-specific), Chen & Yao 2026 and Ishaq et al. 2026. Together they show that the real-world-validation gap has persisted from 2021 to 2026.
- Fall-*risk prediction* reviews, such as the 2025 meta-analysis on wearables predicting falls (pooled sensitivity 0.55, specificity 0.89; [PubMed 41889634](https://pubmed.ncbi.nlm.nih.gov/41889634/)), answer a different question. Do not mix them up with *detection* reviews in the paper.

### Gaps
- I could not open full texts, so the exact author lists, quotes and inclusion counts need checking in the PDFs.
- I found no 2021–2026 Cochrane or JMIR systematic review specific to smartphone-only fall detection beyond the Frontiers 2022 review.

## Q2. Threshold-based vs ML vs deep learning (accuracy, generalization, energy, explainability) and why threshold baselines are defensible

### Takeaway
Reviews describe threshold methods as cheap, simple and transparent, but they say accuracy depends heavily on the chosen thresholds. ML and deep learning reach higher accuracy within a dataset but lose performance across datasets and in real life. Bagalà et al. (2012) showed that 13 published, mostly threshold-based, algorithms dropped sharply on real falls. That combination makes threshold algorithms reasonable, well-understood baselines for a replication on commodity phones.

### Cited Findings
- **Frontiers 2022 smartphone review:** 6 of 15 apps were threshold-based and 9 used ML. Sensitivities ranged from 60.4% to 99.3%. (HIGH) — [Frontiers](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.996021/full)
- **Smartphone review in *Ingénierie des Systèmes d'Information* (IIETA, 2019, pre-period):** "TBA based techniques require less computation power in comparison to ML based techniques, the latter provides better accuracy"; "accuracy of the system largely depends on predefined threshold values." (MEDIUM) — [IIETA](https://www.iieta.org/journals/isi/paper/10.18280/isi.240602)
- **Bagalà et al. (2012), "Evaluation of Accelerometer-Based Fall Detection Algorithms on Real-World Falls", *PLoS ONE* 7(5):e37062:**
  - 13 published algorithms were tested on 29 real falls from high-risk patients (SensAction-AAL).
  - Specificity was 83.0% ± 30.3% (max 98%). Sensitivity was 57.0% ± 27.3% (max 82.8%), "much lower than the values obtained on simulated falls."
  - Over 1 day of monitoring 3 fallers, the algorithms produced 3 to 85 false alarms.
  - The authors conclude that testing in real-life conditions is needed.
  - Confidence: HIGH.
  - Sources: [PMC3353905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353905/); [EPFL Infoscience](https://infoscience.epfl.ch/record/177274)
- **Scoping review on real-world evaluation (2018):** 13 published approaches fell from sensitivity 0.91 and specificity 0.99 on simulations to 0.57 and 0.83 on real-world data. Poor external validity was attributed to "laboratory simulated falls conducted by young healthy adults." (HIGH) — [PMC6068511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068511/)
- **Cross-dataset generalization:**
  - A 2025 smartphone feature-engineering study (KNN/SVM) reached 99.89% within MobiAct. Cross-dataset it reached 96.41%, and on the real-fall FARSEEING data it reached 95.35% sensitivity and 98.12% specificity. (MEDIUM) — [PMC12568134](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568134/)
  - Combining three datasets with cost-sensitive ML improved generalization, but robustness was "still dataset-dependent." (MEDIUM) — same source
  - A 2024 *Measurement* paper runs a cross-dataset evaluation using real falls and long-term daily-life monitoring. (Exists; results not retrieved.) — [ScienceDirect S0263224124008777](https://www.sciencedirect.com/science/article/pii/S0263224124008777)
- **Hybrid approach:** A 2024 paper fuses threshold and ML methods, which shows thresholds are still used as pre-filters or components. (LOW, title only) — [SciTePress 2024](https://www.scitepress.org/Papers/2024/122505/122505.pdf)
- **Explainability:** A systematic review on interpretable and explainable AI for wearable *fall-risk* assessment exists, which suggests explainability is a recognized concern for ML models in this area. (MEDIUM, title only) — [PMC13408035](https://pmc.ncbi.nlm.nih.gov/articles/PMC13408035/)
- **Energy:** Ishaq et al. (2026) list energy efficiency among the practical implementation challenges. (MEDIUM) — [DOI](https://doi.org/10.3390/app16041929)

### Inferences
- Arguments the team can use for threshold baselines in 2026:
  1. They need no training data and avoid train/test leakage.
  2. They are fully interpretable, with each threshold having a physical meaning such as g peaks or orientation change.
  3. They are cheap in CPU and battery, which matters for phones running continuous background sensing.
  4. They are the most cited historical baselines (Bagalà's 13 algorithms), so results are comparable with the literature.
  5. Bagalà showed they degrade on real falls, so re-measuring that degradation on today's commodity phones is a meaningful, falsifiable question.
- Because ML gains shrink across datasets, a simple and well-documented baseline is scientifically useful for anchoring comparisons. This is my inference, consistent with the cross-dataset findings above.

### Gaps
- I found no 2021–2026 review that directly measures energy use of threshold vs ML vs DL on smartphones.
- I found no review-level quantitative comparison of explainability.

## Q3. False alarms in real life and the simulated-vs-real-fall gap

### Takeaway
This is the most consistent criticism across the literature. Simulated falls by young volunteers differ physically from real falls of older people, and lab sensitivity and specificity overstate real-world performance. False alarms from everyday abrupt movements are the main practical barrier.

### Cited Findings
- **Casilari & Silva (2022), "An analytical comparison of datasets of real-world and simulated falls intended for the evaluation of wearable fall alerting systems", *Measurement* 202:111843.**
  - They compared 2 real-fall repositories with 18 simulated datasets and found "noteworthy discrepancies between real-world and mimicked falls."
  - They also state that clinical tests in continuous monitoring "unanimously show a clear underperformance" relative to lab-trained algorithms.
  - Confidence: HIGH.
  - Sources: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0263224122010429); [RIUMA PDF](https://riuma.uma.es/xmlui/bitstream/10630/24944/1/1-s2.0-S0263224122010429-main.pdf)
- **Why simulated falls differ:** Simulated falls are deliberate and done in safe settings, so protective reflexes are likely suppressed. (HIGH) — [PMC6068511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068511/)
- **Young volunteers in datasets:** The KFall dataset paper acknowledges it "only contains simulated falls from young male adults due to safety concerns and practical convenience." (MEDIUM) — [Frontiers Aging Neurosci 2021](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2021.692865/pdf)
- **Share of studies using simulated falls:**
  - 98.5% in Ishaq et al. 2026 — [DOI](https://doi.org/10.3390/app16041929)
  - More than half of 243 studies in Chen & Yao 2026 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/41960380/)
- **False positives in real deployments:** Specificity drops in real-world validation because of rapid sitting, dropped objects and similar movements. (HIGH) — [PMC13056853](https://pmc.ncbi.nlm.nih.gov/articles/PMC13056853/)
- **Bagalà 2012:** 3 to 85 false alarms per day per algorithm. (HIGH) — [PMC3353905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353905/)
- **Dataset heterogeneity:** One of the main problems of public datasets is their "lack of homogeneity" in length, sampling, fall types and subjects. (MEDIUM; cited via a paper citing Casilari's survey) — [arXiv 1811.06672](https://arxiv.org/pdf/1811.06672)

### Inferences
- A replication on commodity phones should report false alarms per hour or per day of ADL recording, not only sensitivity and specificity on simulated trials. It should state the young-volunteer and simulated-fall limitation openly, since every review flags it.

### Gaps
- FARSEEING remains the main real-fall database. I could not confirm its current access terms.

## Q4. Do reviews call for reproducibility, open code, standardized evaluation, or real-world validation?

### Takeaway
Calls for **real-world validation** and **standardized evaluation** are explicit and repeated from 2014 to 2026. Calls for **open data** appear in some reviews. An explicit audit of **open code or replication** of published wearable algorithms was **not found** in 2021–2026 reviews. That is an under-addressed gap the student study can claim, as long as it is worded carefully.

### Cited Findings
- **Real-world validation is the main recommendation in recent reviews:**
  - Warrington 2021 — [PMC8591794](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8591794/)
  - Chen & Yao 2026 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/41960380/)
  - Ishaq et al. 2026 — [DOI](https://doi.org/10.3390/app16041929)
- **Standardization:**
  - The earlier systematic review called for standardized evaluation of these devices — [PubMed 24406708](https://pubmed.ncbi.nlm.nih.gov/24406708/)
  - Warrington 2021 could not run a meta-analysis because methods and reporting were heterogeneous — [PMC8591794](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8591794/)
  - A related fall-prediction meta-analysis notes that methodological inconsistencies, scarce real fall data and non-uniform fall definitions still hinder comparability — [Frontiers 2026](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2026.1778750/full)
- **Open datasets and reproducibility:** A 2024 review of vision-based deep learning for elderly fall detection encourages authors to make custom datasets public "to enhance reproducibility." It covers the vision domain, not wearables. (MEDIUM) — [arXiv 2401.11790](https://arxiv.org/pdf/2401.11790)
- **Hardware validation:** A review of real-time vision systems found most models lack validation on physical hardware and do not report inference time. Only 11 of 588 records met all inclusion criteria. (MEDIUM, vision domain) — [PMC13517638](https://pmc.ncbi.nlm.nih.gov/articles/PMC13517638/)
- **Precedent for re-implementing published algorithms:** Re-implementing published algorithms and testing them on new data is an accepted method, as Bagalà 2012 did with 13 algorithms and the 2018 scoping review did with 13 approaches. (HIGH) — [PMC3353905](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353905/); [PMC6068511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068511/)
- **Commodity devices:** Variability across commodity devices is documented.
  - Built-in phone and watch IMUs are not clinical-grade — [PMC12431052](https://pmc.ncbi.nlm.nih.gov/articles/PMC12431052/)
  - A JMIR study found a non-significant trend that some smartwatches and operating systems had better sensitivity than others — [JMIR Form Res 2022](https://formative.jmir.org/2022/3/e30121)

### Inferences
- Suggested framing for the paper: "Recent reviews (Warrington et al., 2021; Chen & Yao, 2026; Ishaq et al., 2026) consistently call for real-world and standardized evaluation. Algorithm replication on today's heterogeneous commodity smartphones has been tested only rarely since Bagalà et al. (2012)." Use "rarely" or "few", not "never", because a full audit was not done.

### Gaps
- I found no review that counts how many fall-detection papers release code. A claim that "most papers don't release code" would need its own evidence, such as a GitHub search or a sample audit.

## Q5. Epidemiology: WHO figures, the long lie, and Brazil

### Takeaway
WHO estimates 684,000 fall deaths per year, falls are the second leading cause of unintentional injury death, and death rates are highest above age 60. In Brazil about 1 in 4 urban older adults fell in the past year (ELSI-Brasil), and SUS hospitalizations and deaths from falls have risen steadily. A "long lie" of one hour or more is common among the oldest old and carries serious complications, which motivates automatic detection.

### Cited Findings
- **WHO fact sheet "Falls" (26 April 2021):**
  - About 684,000 fatal falls per year, the second leading cause of unintentional injury death after road traffic injuries.
  - Death rates are highest among adults over 60 in all regions.
  - About 37.3 million falls per year are severe enough to need medical attention.
  - More than 80% of fall deaths occur in low- and middle-income countries.
  - Confidence: HIGH from snippets; the page itself could not be fetched. Older versions said 424,000 deaths, which is outdated.
  - Sources: [WHO](https://www.who.int/news-room/fact-sheets/detail/falls); [NDSC summary](https://www.ndsc.org/cs-resources/key-issues-statistics/falls/)
- **Disability:** An IOF summary of a WHO report says falls cause disability for about 172 million people per year and fall deaths have risen faster than other injury types. (MEDIUM, secondary) — [IOF](https://osteoporosis.foundation/news/step-safely-strategies-preventing-and-managing-falls-across-life-course-20210531-0829)
- **Long lie:**
  - Fleming & Brayne (2008), *BMJ* 337:a2227. Prospective cohort of people over 90 in Cambridge, followed for 1 year. It describes the incidence of lying on the floor for a long time and the low use of call alarms. (HIGH for the design; the specific percentages were not verified.) — [BMJ](https://www.bmj.com/content/337/bmj.a2227.abstract)
  - A long lie is generally defined as more than 1 hour on the floor — [NIHR Open Research](https://openresearch.nihr.ac.uk/articles/6-19)
  - The NIHR/Sheffield "Long Lies Study" protocol says about 1 in 3 people over 65 fall each year and about 1 in 5 of them stay on the floor for over an hour. (MEDIUM) — [NIHR](https://openresearch.nihr.ac.uk/articles/6-19); [Sheffield](https://sheffield.ac.uk/cure/current-trials/long-lies-study)
  - Complications: hypothermia, dehydration, pressure injuries, muscle damage (rhabdomyolysis), delayed care and psychological harm. (MEDIUM) — [NHS Scotland care-home guidance](https://rightdecisions.scot.nhs.uk/media/5jbdqvih/care-of-residents-within-a-care-home-setting-who-are-at-risk-of-long-lie.pdf)
- **Brazil:**
  - **ELSI-Brasil (2019–2021):** Fall prevalence in the previous 12 months was 25% among urban older adults. Associated factors include female sex, age ≥75, fear of falling, arthritis, diabetes and depression. (HIGH) — [Ministério da Saúde, jun/2023](https://www.gov.br/saude/pt-br/assuntos/noticias/2023/junho/no-brasil-prevalencia-de-quedas-entre-idosos-em-areas-urbanas-e-de-25)
  - **ELSI baseline (n=4,174):** 25.1% fell. 1.8% of falls caused hip or femur fracture, and 31.8% of those needed a prosthesis. 7.8% needed to seek a health service. (MEDIUM, from a UnB thesis) — [Repositório UnB](https://repositorio.unb.br/handle/10482/39282)
  - **Novaes et al. (2023), *Ciência & Saúde Coletiva* 28(11):3101–3110**, "Acidentes por quedas na população idosa: análise de tendência temporal de 2000 a 2020 e o impacto econômico estimado no sistema de saúde brasileiro em 2025." Deaths rose continuously from 2000 to 2020, with a 6.4% annual variation. (MEDIUM; the authors' full names and the 2025 cost projection were not retrieved.) — [SciELO](https://www.scielo.br/j/csc/a/y3H93qVXYZHtfjpRnm4ykdd/?format=html&lang=pt); [SciELO SP PDF](https://scielosp.org/pdf/csc/2023.v28n11/3101-3110/pt)
  - **Lima et al. (2022), *Epidemiologia e Serviços de Saúde*:** 1,746,097 SUS admissions for falls among older adults, costing R$ 2,315,395,702.75, with mean stay of 5.2–7.5 days. (MEDIUM; check the period covered.) — [SciELO SP](https://scielosp.org/pdf/ress/2022.v31n1/e2021603/pt)
  - **SUS hospitalizations 2000–2018:** about 1.48 million fall hospitalizations of older adults, a rate of 38.6 per 10,000. (MEDIUM) — [Scientia Medica PUCRS](https://revistaseletronicas.pucrs.br/scientiamedica/article/view/36751)
  - **Southeast region (SIM/DATASUS, 2012–2023):** 62,910 fall deaths among older adults; 54.5% were aged ≥80. (MEDIUM) — [Revista Saúde Coletiva](https://revistasaudecoletiva.com.br/index.php/saudecoletiva/article/view/3286)
  - **INTO estimate:** fall prevalence of about 40% among people over 80. (LOW, press release) — [Sírio-Libanês](https://hospitalsiriolibanes.org.br/imprensa/quedas-idosos-80-anos-ministerio-da-saude)

### Inferences
- In the paper, ELSI prevalence (self-report) and DATASUS counts (administrative records) should be presented as different measures, not compared directly.

### Gaps
- I did not retrieve Pará/Belém-specific or North-region data. If the team needs local context, DATASUS TabNet (SIH/SIM, ICD-10 W00–W19, age 60+) would have to be queried directly.
- The Fleming & Brayne percentages (for example, the "30% lay >1h" figure often quoted) were not verified.

## Q6. Commercial context: what products exist and what is known about their accuracy and false alarms

### Takeaway
Fall detection now ships as a standard feature on mainstream smartwatches (Apple, Google Pixel, Samsung), alongside medical-alert pendants. Vendors disclose no accuracy figures and state that not all falls are detected. Independent peer-reviewed validation of these built-in features in older adults is scarce. The few data points include a very low sensitivity for wheelchair users and false emergency calls from Apple's related Crash Detection feature.

### Cited Findings
- **Apple Watch (SE and Series 4 or later):**
  - Fall detection turns on automatically if the user is 55 or older. Users aged 18–54 must enable it.
  - Modes are "Always on" or "Only on during workouts."
  - Apple warns that physically active users are more likely to trigger it through high-impact activity, and that "Apple Watch cannot detect all falls."
  - Confidence: HIGH.
  - Sources: [Apple Support 108896](https://support.apple.com/ml-in/108896); [Apple Watch User Guide](https://support.apple.com/en-is/guide/watch/apd34c409704/watchos)
- **Google Pixel Watch:** Fall detection launched in February 2023. It uses motion sensors with on-device machine learning and auto-calls emergency services if the user doesn't respond. Google says it "may not detect all falls," and it is not available in all countries. (HIGH) — [Google blog](https://blog.google/products/pixel/fall-detection-on-pixel-watch/)
- **Samsung Galaxy Watch:** "Hard fall detection" is off by default and enabled through the Galaxy Wearable app (SOS settings). It sends an SOS to emergency contacts rather than calling emergency services directly. (MEDIUM, tech press) — [9to5Google](https://9to5google.com/2023/03/21/galaxy-watch-5-fall/)
- **Independent accuracy evidence:**
  - **Brew et al. (2022), *JMIR Formative Research* 6(3):e30121.** A third-party threshold-based smartwatch app (not Apple's feature) was tested with 22 healthy adults and video as ground truth. Sensitivity was about 77% and specificity about 99% for induced falls. There was a non-significant trend for some devices and operating systems to perform better. (HIGH) — [JMIR](https://formative.jmir.org/2022/3/e30121); [PMC8981002](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8981002/)
  - **Wheelchair users:** A University of Illinois study reportedly found Apple Watch detected 14 of 300 fall trials, a sensitivity of 4.7%. (LOW-MEDIUM; reported via a consumer site, original not located) — [Smartwatch Insight](https://smartwatchinsight.com/smartwatch-fall-detection-accuracy/); [MedicalAlertBuyersGuide](https://www.medicalalertbuyersguide.org/smartwatch-medical-alert-system/apple-watch-medical-alert-review/)
  - **Crash Detection false calls:** Apple's related feature caused many false 911 calls from skiers. In Japan's Hida Mountains, 134 false calls were logged in about 5 weeks, more than 14% of emergency calls. This concerns Crash Detection, not fall detection. (MEDIUM, Wikipedia citing press) — [Wikipedia](https://en.wikipedia.org/wiki/Crash_Detection)
  - Claims that a September 2023 watchOS update increased false alarms come only from consumer review sites. (LOW) — [RetirementLiving](https://www.retirementliving.com/reviews/apple-watch-fall-detection)
- **Medical-alert pendants and phone apps:** No reliable 2021–2026 accuracy data was found in this search.

### Inferences
- Market framing: big-tech wearables validate the need, but they are proprietary and not reproducible, they cost far more than a phone the person already owns (watch plus iPhone), and they publish no accuracy metrics. A transparent, open baseline on commodity Android or iOS smartphones complements them, which is relevant in Brazil, where smartwatch ownership among older adults is likely low. (The ownership claim is unsourced, so the team should find IBGE/TIC data before using it.)

### Gaps
- I found no peer-reviewed validation of Apple, Pixel or Samsung built-in fall detection in community-dwelling older adults.
- I found no data on false-alarm rates of medical-alert pendants such as Philips Lifeline or MobileHelp.
- Brazilian market data (smartwatch or smartphone ownership among older adults, TIC Domicílios or IBGE PNAD) was not searched.
