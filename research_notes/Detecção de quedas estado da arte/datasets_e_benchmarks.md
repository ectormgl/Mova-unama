# Public datasets and benchmark / cross-dataset / replication studies for inertial fall detection (emphasis 2022–2026)

Method note: research was done on 2026-10-13 with WebSearch (standard and extended) plus one successful WebFetch (GitHub WEDA-FALL README). WebFetch to PMC, PLOS, ncbi and riuma.uma.es failed (DNS blocked), so most facts below come from **search-engine snippets or summaries of the abstract**, not full texts. Confidence tags: [H] high (primary page or several consistent sources), [M] medium (single snippet from a primary source), [L] low (secondary source or my background knowledge, not verified in this session).

## 1. What public fall datasets exist, and which are newest (2020–2026)?

### Takeaway
Many public inertial fall datasets exist, but almost all contain **falls simulated in a lab by young adults**. The newest relevant additions are KFall (2021, lower back, pre-impact labels) and WEDA-FALL (2023, Fitbit wrist, includes elders aged 77–95 doing ADLs only). Searches did not find a 2023–2026 public dataset of **real** falls of older adults with smartphone-in-pocket data. FARSEEING, the main source of real falls, is still only available on request (a 20-fall subset was shared; the extended 143-fall set was "not publicly available" as of 2022). LTMM remains the open free-living older-adult recording, but it has no falls.

### Cited Findings
**Dataset table** (source for each row is given; "sim" = simulated falls)

| Dataset | Device / placement | Rate | Subjects | Falls / ADLs | Real or sim | Access |
|---|---|---|---|---|---|---|
| SisFall (2017) | Custom device at the waist: 2 accelerometers + gyroscope | 200 Hz | 38: 23 young + 15 elderly | Falls by young subjects; the elderly did ADLs only (on a physician's advice) | sim | Open |

SisFall sources: [Search summary of SisFall paper, PMC5298771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/) [M]; [DOI](https://doi.org/10.3390/s17010198). "Elderly people did not perform falls and some activities due to recommendations of the physician specialized in sports" (snippet) [M]. From memory and not verified here: one 60-year-old judo practitioner did perform the falls [L].

- **KFall (2021, Frontiers in Aging Neuroscience; Yu, Jang, Xiong, KAIST)** [H]
  - Sensor: one 9-axis IMU on the lower back (accelerometer, gyroscope and Euler angles) at 100 Hz.
  - Subjects: 32 Korean participants (young adults).
  - Content: 21 ADL types and 15 simulated fall types, about 5,075 trials (2,729 ADL and 2,346 falls).
  - Labels: video-synchronized onset and impact labels, which the authors call the first public dataset suitable for **pre-impact** detection. The authors also published threshold, SVM and deep-learning benchmark algorithms.
  - Sources: [PMC8322729](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8322729/), [Frontiers](https://www.frontiersin.org/articles/10.3389/fnagi.2021.692865/full), [PreFallKD (gives the trial counts)](https://arxiv.org/pdf/2303.03634).
- **WEDA-FALL (Wrist Elderly Daily Activity and Fall Dataset, Marques and Moreno, about 2023)** [H, fetched README]
  - Device: Fitbit Sense smartwatch on the wrist, recording accelerometer, gyroscope and orientation at 50 Hz. Downsampled versions at 40, 25, 10 and 5 Hz are included.
  - Subjects: 25 participants aged 20–95. The 14 young subjects (IDs 1–14, mostly aged 20–23, one aged 46) performed 8 fall types onto a mattress. The 11 elders (aged 77–95) did ADLs only.
  - Counts: about 350 fall signals and 619 ADL signals; the README implies 157 of the ADL signals are from elders. Fall-phase timestamps and videos are provided.
  - License: not stated.
  - Sources: [GitHub joaojtmarques/WEDA-FALL](https://github.com/joaojtmarques/WEDA-FALL); [Sensors 23(3):1146](https://www.mdpi.com/1424-8220/23/3/1146) [M].
- **FallAllD** [M]
  - 15 subjects with an IMU at the waist, wrist, and chest or neck (sources differ on the placement).
  - About 238 Hz, according to the 2022 comparison table.
  - Source: [Casilari and Silva 2022, Measurement](https://www.sciencedirect.com/science/article/pii/S0263224122010429).
- **MobiAct** [M]
  - 57 subjects with a smartphone in the trouser pocket (thigh).
  - Accelerometer at about 87 Hz; gyroscope and orientation at 100 Hz.
  - Simulated falls; same source as FallAllD.
- **tFall** [M]
  - 10 subjects with a smartphone in a thigh pocket or handbag, at about 45–50 Hz (sources differ).
  - Source: same 2022 comparison, plus the [ScienceDirect snippet](https://www.sciencedirect.com/science/article/pii/S0263224122010429).
  - From memory (Medrano et al. 2014) [L]: tFall's ADLs were recorded during the subjects' real daily life over several days and its falls were simulated. If true, tFall is one of the few datasets that lets you estimate false alarms on smartphone free-living data. This needs verification.
- **UMAFall** [M]
  - 19 subjects; a smartphone plus IMUs at the ankle, chest, thigh, waist and wrist.
  - Smartphone at 100 Hz, IMUs at 20 Hz. Seven subjects did not perform falls.
  - Sources: [ResearchGate](https://www.researchgate.net/publication/318385531_UMAFall_A_Multisensor_Dataset_for_the_Research_on_Automatic_Fall_Detection) and the 2022 comparison.
- **UP-Fall (2019)** [M]
  - Multimodal: wearable IMUs, EEG, ambient sensors and cameras.
  - About 17 young healthy subjects (sources say 17 or 24). The consolidated data was homogenized to about 18 Hz.
  - Source: [PMC6539235](https://pmc.ncbi.nlm.nih.gov/articles/PMC6539235/).
- **MobiFall** [M]
  - 24 participants aged 22–47 with a smartphone in the trouser pocket.
  - **UniMiB SHAR** [M]: 30 subjects aged 18–60 with a phone in the pocket.
  - Source: [search summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/).
- **Nandi et al. 2023 (Data in Brief), wrist dataset** [M]
  - Custom wrist device with an IMU and a heart-rate sensor.
  - 41 volunteers performing 16 ADLs and 8 fall types, each repeated 5 times.
  - Source: [PMC10709028](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10709028/).
- **FARSEEING real-world fall repository (Klenk et al. 2016)** [H]
  - Content: a meta-database of real falls recorded 2012–2015, with 208 verified falls by the end of 2015. All signals include an accelerometer, mostly on the lower back or thigh.
  - Access: "shared on request"; a subset of **20 fall events** was available on request through the project site.
  - The extended 143-fall version used by Palmerini 2020 was "not publicly available" as of 2022.
  - Sources: [Springer EURAPA 2016](https://link.springer.com/article/10.1186/s11556-016-0168-9), [ISPGR summary](https://ispgr.org/the-farseeing-real-world-fall-repository/), [Manchester figshare record](https://research.manchester.ac.uk/en/datasets/the-farseeing-real-world-fall-repository-a-large-scale-collaborat/), [Casilari and Silva 2022](https://www.sciencedirect.com/science/article/pii/S0263224122010429).
- **LTMM (PhysioNet Long Term Movement Monitoring)** [H]
  - 3-day 3D accelerometer recordings on the lower back of **71 community-dwelling older adults**, mean age about 78 (range 65–87).
  - Fallers are defined as people with 2 or more self-reported falls in the previous year; the dataset contains **no falls**.
  - Open access. Data paper: Weiss et al. 2013.
  - Sources: [PhysioNet ltmm](https://physionet.org/content/ltmm/), [archive](https://archive.physionet.org/pn6/ltmm/).
- **Real-fall data in Casilari and Silva 2022:** the authors compared 2 real-fall repositories against 18 simulated-fall datasets.
  - One real-fall set came from 5 elderly subjects monitored for 833 hours in their homes with a custom vest.
  - The authors say these are the only publicly available datasets with actual falls.
  - Source: [UMA repository PDF, snippet only](https://riuma.uma.es/xmlui/bitstream/10630/24944/1/1-s2.0-S0263224122010429-main.pdf) [M].
- **FFFStudy repository:** the 2024 Silva, Casilari and García-Bermúdez study used it for real falls plus long-term daily-life monitoring.
  - Source: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0263224124008777) [M].
  - I could not confirm its size, placement or access status.
- **Search for 2024–2026 datasets:** a search for new public smartphone or older-adult fall datasets returned no new dataset of real falls by older adults.
  - Smartphone-review snippets confirm that "the recorded falls were performed exclusively by young subjects".
  - Sources: [Frontiers Public Health 2022 search result](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.996021/full), [ResearchGate review "Fall detection using accelerometer-based smartphones: where do we go from here?"](https://www.researchgate.net/publication/364405446_Fall_detection_using_accelerometer-based_smartphones_Where_do_we_go_from_here) [M].
  - A 2025 low-cost IMU (waist and thigh) older-adult ADL and fall dataset was mentioned in a snippet, but its venue and access could not be confirmed. Source: [Frontiers in AI 2026 result](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1734096/full) [L].
- **Kaggle "Elderly Fall Detection IoT Dataset":** its provenance is unclear, and I do not recommend using it as a benchmark. Source: [Kaggle](https://www.kaggle.com/datasets/ziya07/elderly-fall-detection-iot-dataset) [L].

### Inferences
- For a smartphone-in-pocket study, the closest public matches in placement are **MobiAct, tFall, UMAFall (thigh phone) and UniMiB SHAR**, not SisFall (waist).
- Using SisFall together with **one pocket-phone dataset** (MobiAct or tFall) would directly address the placement mismatch.
- **KFall** is a good second waist or lower-back dataset for checking whether thresholds transfer, and it shares placement with LTMM and FARSEEING (lower back).
- The team could request the FARSEEING 20-fall subset (or the extended set) to test sensitivity on real falls. Access status in 2026 is unverified.

### Gaps
- I could not verify any FARSEEING open release after 2016, or the current request procedure.
- tFall's free-living ADL protocol is from my memory only.
- I could not retrieve full-text tables (subject ages, trial counts) for FallAllD, MobiAct or UMAFall; the 2022 comparison table is the only source used.
- I did not find a confirmed new (2024–2026) public dataset of real falls of older adults, or a long free-living smartphone dataset of older adults.

## 2. Why is SisFall the most-used benchmark, and what are its limitations?

### Takeaway
SisFall is popular because it is open, large (38 subjects), sampled at a high rate (200 Hz), and includes elderly participants and a broad ADL and fall protocol. However, its falls are simulated almost entirely by young people. Its own authors showed that thresholds tuned on young subjects are biased upward and perform worse on elderly movements. I found no source that quantitatively ranks it as "the most used" dataset.

### Cited Findings
- SisFall is described as "a well-known benchmark for fall detection using accelerometer and gyroscope data". Source: [search snippet](https://www.researchgate.net/figure/Comparison-of-fall-detection-methods-on-the-SisFall-dataset-regarding-accuracy_tbl4_371884391) [M].
- **Elderly subjects did not perform falls.** "Elderly people did not perform falls and some activities due to recommendations of the physician". Source: [SisFall, PMC5298771](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/) [M, snippet].
- **Young and elderly falls differ.** "Young people simulating falls tend to do it faster without trying to avoid the impact, while the elderly participant always tried to cushion the hits". Source: [SisFall](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/) [M, snippet].
- **Threshold bias.** Elderly ADLs and falls were smaller in amplitude, so "algorithms trained with data from young people tended to bias the thresholds upwards". Validation with elderly subjects "significantly reduced the fall detection performance". Source: [SisFall](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/) [M, snippet].
- **ADL error rate.** In the original threshold tests, a failure rate of nearly 50/50 on ADLs was described as prohibitive for real-life use. Source: [SisFall](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5298771/) [M, snippet, exact context unverified].
- **Post-fall only.** The KFall paper says SisFall and similar datasets suit only post-fall detection, not pre-impact detection. Source: [KFall, Frontiers 2021](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2021.692865/full) [M].
- **Small elderly sample.** One review notes SisFall's reliance on a small group of elderly subjects "may not fully capture the diversity of fall scenarios". Source: [Sensors 2025 decade review, PMC11991334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11991334/) [M].
- **Sampling rate.** FallAllD and SisFall are the datasets with accelerometers at 200 Hz or more. Source: [arXiv 2012.03426](https://arxiv.org/pdf/2012.03426) [M]. Most smartphone datasets are at about 45–100 Hz (see the table in section 1).

### Inferences
- The SisFall choice is defensible as the **primary offline benchmark** because it is comparable with hundreds of papers.
- To replicate faithfully on a smartphone, the team should resample SisFall to the phone rate (for example 50–100 Hz) and convert units to g. They should report results separately for the elderly ADL subset, because that subset is where false positives on older-adult motion can be measured.
- The "waist vs pocket" and "custom device vs phone IMU" mismatches should be stated explicitly as threats to validity.

### Gaps
- There is no bibliometric count proving SisFall is the most used. A 2025 decade review exists (Sensors 25:2205, [DOI](https://doi.org/10.3390/s25072205)) but I could not open it to check its dataset-usage ranking.

## 3. What do cross-dataset and real-fall studies conclude?

### Takeaway
There is a consistent conclusion from 2022 to 2026. Detectors trained and tested within one simulated dataset generalize poorly. When tested across datasets, and especially on real falls or long daily-life recordings, sensitivity, specificity **and the hourly false-alarm rate** all degrade sharply. The best ML result on real FARSEEING falls was about 80% sensitivity with 0.56 false alarms per hour (Palmerini 2020).

### Cited Findings
- **Silva, Casilari and García-Bermúdez 2024 (Measurement 235:114992).**
  - Design: 13 AI detectors on waist accelerometer data, trained on up to 11 lab datasets and tested on real falls and long-term daily-life data (FFFStudy).
  - Result: "remarkable degradation in all performance metrics (sensitivity, specificity and false alarm hourly rate)". The algorithms "tend to overfit the patterns of emulated falls".
  - The paper also argues that "even a low number of false alarms may give the impression of an unreliable system".
  - Sources: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0263224124008777), [ResearchGate](https://www.researchgate.net/publication/380883370_Cross-dataset_evaluation_of_wearable_fall_detection_systems_using_data_from_real_falls_and_long-term_monitoring_of_daily_life) [M, abstract snippets; numeric results not retrieved].
- **"A Cross-dataset Evaluation of Wearable Fall Detection Systems" (ACM PETRA 2022, Casilari group).**
  - A CNN tested across 4 datasets: results on one dataset often did not carry over to another.
  - The authors attribute this to models overlearning the specific movement types, sensors and subjects.
  - Source: [ACM DL](https://dl.acm.org/doi/10.1145/3529190.3529191) [M].
- **Casilari and Silva 2022 (Measurement 202:111843).**
  - Method: compared 2 real-fall repositories with 18 simulated-fall datasets using 15 accelerometer statistics.
  - Motivation: clinical trials show that detectors perform worse in real settings.
  - Source: [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0263224122010429) [M; detailed conclusions not retrieved].
- **Wrist-based generalization across datasets (about 2024).** Generalization depended on the training dataset and the algorithm. Source: [ResearchGate](https://www.researchgate.net/publication/378760322_Wrist-Based_Fall_Detection_Towards_Generalization_across_Datasets) [M].
- **Palmerini et al. 2020 (Sensors 20(22):6479).**
  - Data: 143 real falls from FARSEEING, recorded by a lower-back sensor in people at moderate-to-high fall risk.
  - Best method: SVM with multiphase fall-model features, giving sensitivity above 80%, **0.56 false alarms/hour** and an F-measure of 64.6%.
  - The paper also proposes metrics for characterizing real-world detectors.
  - Sources: [PMC7697900](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7697900/), [MDPI](https://www.mdpi.com/1424-8220/20/22/6479) [H].
- **Aderinola, Palmerini, D'Ascanio, Chiari, Klenk, Becker, Caulfield and Ifrim 2024.**
  - Paper: "Accurate and Efficient Real-World Fall Detection Using Time Series Techniques", AALTD workshop, Springer LNCS, pp. 52–79. Uses FARSEEING real falls.
  - Follow-up (2025 arXiv preprint): more than 60 hours of FARSEEING IMU data, streaming evaluation, and cost-sensitive threshold tuning to reduce missed falls.
  - Sources: [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-031-77066-1_4), [arXiv 2509.11789](https://arxiv.org/abs/2509.11789v1) [M; numeric results not retrieved].
- **"Beyond Simulated Benchmarks: Evaluating Motion Representations for Fall Detection Under Real-World Data Scarcity" (2026 preprint).**
  - Methods that perform best on simulated data degrade most under domain shift.
  - Representations based on dataset-invariant physical quantities transfer better.
  - Source: [arXiv 2608.13197](https://arxiv.org/pdf/2608.13197) [M, snippet only].
- **Combined training data.** One 2024 study built a combined training set of more than 1,300 falls and about 28K non-fall samples to counter placement and sampling-rate domain shift. Source: [ResearchGate](https://www.researchgate.net/publication/380883370_Cross-dataset_evaluation_of_wearable_fall_detection_systems_using_data_from_real_falls_and_long-term_monitoring_of_daily_life) [L: the snippet attribution is ambiguous].
- **Share of studies using simulated falls.** One review is reported to state that 98.5% of studies use simulated falls, with only 2 validating on real unanticipated falls in the target population. Source: secondary snippet, [SisFall search results](https://www.researchgate.net/publication/312669325_SisFall_A_Fall_and_Movement_Dataset) [L, primary source not identified].
- **Bagalà et al. 2012 (PLoS ONE 7(5):e37062).** 13 algorithms were re-tested on real falls, giving a mean sensitivity of 57% and 3–85 false alarms/day (figures as the team states them). Source: [PLOS](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0037062) [figures not re-verified here: fetch blocked].

### Inferences
- The literature since 2022 **supports the team's Bagalà-style design**: re-testing published thresholds across datasets is exactly the "cross-dataset" problem the field now highlights.
- Expect large drops from SisFall-reported numbers.
- Reporting an hourly or daily false-alarm rate is now standard in the cross-dataset papers (Silva 2024, Palmerini 2020).

### Gaps
- Exact numeric outcomes of Silva 2024, Casilari 2022 and Aderinola 2024 were not retrieved (paywalled or fetch blocked).
- I did not verify whether any cross-dataset study used LTMM specifically.

## 4. Is "false alarms per day on free-living older-adult data" a recognized metric, and which datasets enable it?

### Takeaway
Yes. False alarms per hour or per day is an established real-world metric. It is used by Bagalà 2012 (FA/day), Palmerini 2020 (FA/hour), Silva 2024 ("false alarm hourly rate") and prospective smartphone studies (for example, one false alarm every 46 days). Reviews explicitly recommend it over specificity. Datasets that enable it are LTMM (open, no falls), FARSEEING (falls plus surrounding data, on request), the FFFStudy / UMA real-fall long-term recordings (833 h, 5 elders), and possibly tFall (real-life ADLs from a smartphone).

### Cited Findings
- A review notes that a specificity of 99.99% can still mean about **8 false positives per day**, and recommends reporting false positives per day or per hour. Source: snippet in a [search result list](https://pmc.ncbi.nlm.nih.gov/articles/PMC12431052/) [L: exact source paper uncertain].
- **Prospective smartphone study (J NeuroEng Rehabil 2021).**
  - Detected 27 of 37 real falls in at-risk users (sensitivity 73.0%), with **one false alarm every 46 days**.
  - 42.2% of the false events were confirmed stumbles.
  - Source: [JNER s12984-021-00918-z](https://jneuroengrehab.biomedcentral.com/articles/10.1186/s12984-021-00918-z) [M].
- **Commodity phone and smartwatch study (about 2025).**
  - Offline F1 was 0.99, but in-home false positives rose. These were linked to individual gait and motion signatures.
  - After retraining, the system reached about 2–4 false alarms per day in older adults.
  - Source: [PMC12431052](https://pmc.ncbi.nlm.nih.gov/articles/PMC12431052/) [M, snippet].
- **Smartwatch pilot.** 3 seniors over about 1 month: 83 false positives and no falls, or 1.153 per person per day. Source: snippet in the [same search](https://pmc.ncbi.nlm.nih.gov/articles/PMC12431052/) [L: original paper not identified].
- **Bourke algorithm on real-world data.**
  - Bourke's VELOCITY+IMPACT+POSTURE algorithm reportedly achieved about 0.6 false positives per day on a real-world database after 100% sensitivity and specificity on simulated falls.
  - Source: snippet; attribution not confirmed, likely [Bagalà 2012 PLOS](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0037062) context or Aziz 2017, [PLOS ONE 0180318](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0180318) [L].
- **Aziz et al. 2017** (SVM, real-world falls and non-fall data): 0 to 0.3 false alarms per hour in older adults. Source: [IDEAS/RePEc](https://ideas.repec.org/a/plo/pone00/0180318.html) [M].
- **Sensitivity and false-alarm rate of a commercial fall sensor in long-term elderly use.** Source: [PubMed 25138139](https://pubmed.ncbi.nlm.nih.gov/25138139/) [M: title only].
- **LTMM is open, has no falls, is on the lower back, and runs 3 days × 71 older adults.** It is therefore suitable for false alarms per day as long as placement (lower back vs phone in pocket) is acknowledged. Source: [PhysioNet](https://physionet.org/content/ltmm/) [H].

### Inferences
- Measuring false alarms per day on LTMM is methodologically aligned with Bagalà 2012, Palmerini 2020 and Silva 2024. It is a recognized metric, not an ad-hoc one.
- Caveats for using LTMM:
  - The sensor is on the lower back and samples at 100 Hz (from my memory [L]; check the PhysioNet header).
  - The device is removed at night, during showers and so on, so normalize by actual worn hours.
  - The data contains no confirmed falls, so every alarm is treated as false.
- Pairing LTMM false alarms per day with FARSEEING sensitivity (if access is granted) would reproduce the Bagalà design on a much larger scale.

### Gaps
- I did not verify the LTMM sampling rate or total wear hours.
- The FFFStudy download location was not confirmed.

## 5. Recent replication / reproducibility studies on smartphones, and is this a stated research gap?

### Takeaway
Luque et al. 2014 is the canonical smartphone re-implementation study. It found that accuracy depends strongly on fall type, that threshold choice is a hard trade-off, and that battery cost is non-negligible. Searches found **no recent (2022–2026) replication that re-implements classic threshold algorithms on current smartphones and tests them on real or free-living data**. Reviews repeatedly name the lab-to-real gap and the young-subject bias. However, no source explicitly framing "smartphone replication" as a named research gap was retrieved.

### Cited Findings
- **Luque, Casilari, Morón and Redondo 2014 (Sensors 14:18543).**
  - An Android testbed comparing accelerometer-only threshold algorithms.
  - Finding: accuracy "depends strongly on the fall pattern", and thresholds trade missed falls against false alarms.
  - Finding: "the extra power consumption introduced by the Android monitoring applications cannot be neglected".
  - Sources: [PMC4239945](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4239945/), [DOI](https://dx.doi.org/10.3390/s141018543) [H].
- **Casilari, Luque and Morón 2015** published a review of Android-based fall detection. Source: Sensors 15:17827, mentioned in [search result](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4239945/) [M].
- **Smartphone review (2022).** "Fall detection using accelerometer-based smartphones: where do we go from here?" found the recorded falls were performed exclusively by young subjects. Sources: [ResearchGate](https://www.researchgate.net/publication/364405446_Fall_detection_using_accelerometer-based_smartphones_Where_do_we_go_from_here), [Frontiers Public Health 2022](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.996021/full) [M].
- **Recent smartphone-specific work (2026).** "Lightweight Multi-channel Fall Detection on Smartphone Accelerometers with Probabilistic Calibration and Event-Level Evaluation" (Neural Processing Letters) emphasizes event-level evaluation. Source: [Springer](https://link.springer.com/article/10.1007/s11063-026-11851-4) [L: title only].
- **Smartphone accelerometer plus WiFi CSI (2024).** Source: [arXiv 2412.09980](https://arxiv.org/pdf/2412.09980) [L: title only].

### Inferences
- A smartphone re-implementation of Kangas 2008, Bourke 2010 and PIPTO 2023, evaluated on SisFall plus pocket-phone datasets with false alarms per day on LTMM, would fill a visible gap.
  - It would be a modern, open, cross-dataset Luque-2014 / Bagalà-2012 hybrid.
  - The team should say "we found no recent replication" rather than "none exists".
- The team should report battery or CPU cost on the phone, following Luque 2014.

### Gaps
- No 2022–2026 paper explicitly titled as a replication or reproducibility study of threshold fall detectors on smartphones was found.
- No quoted review sentence stating "smartphone replication" as a gap was retrieved.
- PIPTO 2023 details were not researched in this pass.
