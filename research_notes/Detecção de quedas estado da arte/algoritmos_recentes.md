# Recent (2023–2026) fall-detection algorithms for smartphones and body-worn IMUs: reproducibility for a replication study

Scope: algorithms a student team could re-implement without contacting authors, compared with the team's baseline set (Kangas 2008, Bourke3 2010, PIPTO 2023). Research date: 2026-10-13. Limits: WebFetch was blocked for MDPI, PMC, arXiv, IEEE and ScienceDirect, so most paper details below come from **search snippets only** (marked "[snippet]"). GitHub pages were fetched directly (marked "[fetched]"). Confidence: H = high, M = medium, L = low.

## Q1. Which threshold, lightweight-ML, deep-learning and TinyML fall-detection algorithms were published 2023–2026, especially for smartphones, and what are their details?

### Takeaway
There are few new **smartphone-specific** algorithms with open code. The strongest 2023–2026 candidates are a feature-based kNN/SVM method for smartphones with explicit LOSO and cross-dataset validation (Guo & Nakayama, Sensors 2025), the real-world-validated time-series classifiers from the FARSEEING group (Aderinola et al., 2024; code on GitHub), and GRU-type RNNs on smartphone data with public code (Bartczak et al., Appl. Sci. 2025). Most TinyML work targets wrist or MCU devices rather than phones, and much of it is hobby code that has not been peer reviewed.

### Cited Findings

**Threshold / rule-based**
- [H] **PIPTO** (the team's baseline). Moutsis, Tsintotas, Gasteratos, *Sensors* 2023, DOI 10.3390/s23187951. Reported sensitivity is 90.40% (MMsys) and 91.56% (KFall), with specificity 93.96% (MMsys) and 85.90% (KFall). The authors state that it fails to reach high performance when the sensor is on the thigh rather than the chest, and that it does not beat the logistic-regression and CNN baselines it compares against [snippet] — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10534597/); [ResearchGate](https://www.researchgate.net/publication/374012894_PIPTO_Precise_Inertial-Based_Pipeline_for_Threshold-Based_Fall_Detection_Using_Three-Axis_Accelerometers)
- [H] PIPTO code: the repo exists [fetched], with `C++` and `python` folders, 17 commits on `main`, and no visible license. It asks users to cite the paper. The thresholds are not on the top-level README and must be read from the code or the sub-READMEs — [GitHub](https://github.com/smoutsis/fall_detection_through_acceleration_data)
- [L] No genuinely new (2023–2026), peer-reviewed, smartphone threshold algorithm with open code turned up. Threshold results returned by searches were older work, such as Pham Van Thanh et al.'s dual-threshold (LFT/UFT) method with posture and vertical velocity, published in the Arabian J. Sci. Eng. around 2018/2019 and reporting 100% on a small volunteer set [snippet] — [UET repository](https://eprints.uet.vnu.edu.vn/eprints/id/eprint/3048/)

**Lightweight ML (feature-based kNN/SVM, time-series classifiers)**
- [H/M] **3s2sub**. Pengyu Guo & Masaya Nakayama (Univ. Tokyo), *Sensors* 25(20):6500, 21 Oct 2025, DOI 10.3390/s25206500. Smartphone accelerometer only. A 3 s window is split into two overlapping sub-windows, eight types of statistical features are extracted, and the result is a 44-dimensional feature vector classified with kNN or SVM. Datasets are UniMiB SHAR, MobiAct and FARSEEING. Reported results [snippet]: 98.45% mean accuracy with LOSO on UniMiB SHAR, peak 99.89% with kNN on MobiAct, 96.41% best accuracy in cross-dataset validation on MobiAct, and 95.35% sensitivity / 98.12% specificity on FARSEEING (real falls). The 2022 IPSJ technical report is the precursor. No code repository was found in the search results — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568134/); [MDPI](https://www.mdpi.com/1424-8220/25/20/6500); [IPSJ 2022](https://ipsj.ixsq.nii.ac.jp/records/218727)
- [M] The same paper's comparison table lists a MobiAct 1D-CNN at 99.49% accuracy, 96.55% sensitivity and 99.50% specificity, with a model of about 0.18 MB and about 0.16 ms per window. These figures are not an on-device Android benchmark [snippet] — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568134/)
- [H] **Real-world time-series fall detection**. Aderinola, Palmerini, D'Ascanio, Chiari, Klenk, Becker, Caulfield, Ifrim, "Accurate and Efficient Real-World Fall Detection Using Time Series Techniques", AALTD 2024 (Springer LNCS). Datasets are FARSEEING (real falls, available on request), FallAllD and SisFall. Mean F1 on FARSEEING is 90.7%, with false alarms and missed falls each "as few as one in three days". The snippet gives an estimated 0.012 false alarms/h and 0.013 misses/h for Hydra; this is a model-based estimate, not measured in deployment. Code repo [fetched]: README cites the paper and links preprocessed FallAllD and SisFall; no license visible — [GitHub mlgig/ts_fall_detection](https://github.com/mlgig/ts_fall_detection); [Springer](https://link.springer.com/chapter/10.1007/978-3-031-77066-1_4); [ResearchGate](https://www.researchgate.net/publication/382940726_Accurate_and_Efficient_Real-World_Fall_Detection_Using_Time_Series_Techniques)
- [M] The algorithm names (Hydra / ROCKET-family) come from the search snippet only. The GitHub README I fetched did not name the algorithms — [Springer snippet](https://link.springer.com/chapter/10.1007/978-3-031-77066-1_4)

**Deep learning**
- [H/M] **RNN (GRU-type) on smartphone accelerometer data**. Bartczak, Glanowska, Kowalewicz, Kunin, Susik, "Fall Detection Based on Recurrent Neural Networks and Accelerometer Data from Smartphones", *Applied Sciences* 15(12):6688, 2025. Dataset is UniMiB-SHAR. The paper notes that authors often do not share code, which hurts reproducibility [snippet]. Repo [fetched]: `rsusik/fall_detection_rnn` is a fork of `martaglanowska/fall_detection_rnn`. It contains a notebook, hyperparameter tuning output, Keras `.h5` models (`model-6-fold-*.h5`), Python 3.9 and TF 2.10. There is no TFLite export and no license visible. The metrics were not visible on the README — [MDPI](https://www.mdpi.com/2076-3417/15/12/6688); [GitHub](https://github.com/rsusik/fall_detection_rnn)
- [M] **Smartphone IMU + WiFi CSI** (two-stage). Wang, Su, Zhang, Zhu, Jiang, He, Yang, arXiv 2412.09980 (Dec 2024, formatted for IEEE Sensors Journal). The phone IMU screens for falls, then a CNN on WiFi CSI checks post-fall mobility, and an Android app sends the alert. The CSI stage reports 99% accuracy. No code link was seen. It needs CSI-capable WiFi hardware, so it is not phone-only [snippet] — [arXiv](https://www.arxiv.org/abs/2412.09980)
- [M] **Fula & Moreno**, "Wrist-Based Fall Detection: Towards Generalization across Datasets", *Sensors* 24(5):1679, 2024. Three wrist datasets are combined (more than 1300 falls, about 28K negative samples). The authors argue that small-scope train/test produces over-optimistic rates and many false positives. One reported cross-dataset accuracy is 78.51 ± 4.06%. Code status unknown [snippet] — [PubMed](https://pubmed.ncbi.nlm.nih.gov/38475215); [ResearchGate](https://www.researchgate.net/publication/378760322_Wrist-Based_Fall_Detection_Towards_Generalization_across_Datasets)
- [M] **Wrist CNN with knowledge distillation on UMAFall**, *Sensors* 2026, DOI 10.3390/s26113328. LOSO is used, but the authors call it only a "supplementary feasibility analysis" [snippet] — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13259118/)
- [M] **Dual-stream Transformer with Kalman fusion**, *BDCC* 2026, DOI 10.3390/bdcc10030090. LOSO on three datasets, wrist sensors [snippet] — [DOI](https://doi.org/10.3390/bdcc10030090)
- [M] **Hybrid CNN–Transformer** (Biomed. Signal Process. Control, 2024). Reports 99.95%, 98.68% and 99.71% accuracy on SisFall, UniMiB-SHAR and MobiAct. Accuracy only, the model is heavy, and no code was seen [snippet] — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1746809424004701)
- [L] **KD-LSTM for offline embedded devices**, arXiv 2308.12481 (2023). The snippet says the notebooks are on GitHub; the URL was not verified — [arXiv](https://arxiv.org/pdf/2308.12481)
- [L] **TSFallDetect / "Physics Sensor Based Deep Learning Fall Detection System"**, arXiv 2403.06994 (2024). The conclusion links code at github.com/WuShaoa/SensorDataClassification-TCN (not fetched) [snippet] — [arXiv](https://arxiv.org/pdf/2403.06994)
- [L] **PREFALLKD** (CNN-ViT with knowledge distillation, KFall, pre-impact). Repo brianchi0607/PREFALLKD is listed in awesome-fall-detection; the repo was not fetched — [awesome list](https://awesome.ecosyste.ms/lists/mintisan/awesome-fall-detection)

**TinyML / on-device**
- [M] **MicroFallNet**, a lightweight CNN for smart wristbands (*Pervasive and Mobile Computing*, 2025). Not a smartphone method; code unknown [snippet] — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1574119225000355)
- [M] A wearable real-time system (*Future Internet* 2026, DOI 10.3390/fi18040211) uses an MLP with hidden layers of 40 and 20 neurons and INT8 TFLite [snippet] — [DOI](https://doi.org/10.3390/fi18040211)
- [L] Hobby or non-peer-reviewed TinyML repos: an ESP32-S3 INT8 1D-CNN on an MPU-6050 at 100 Hz with TFLite Micro, and Edge Impulse projects on ESP8266, Nesso N1 and Nano 33 BLE. None of these were validated on older adults [snippet] — [esp32s3 repo](https://github.com/BuiDoanAnhKhoa/esp32s3-tinyml-fall-detector); [Fall-Detection-TinyML](https://github.com/geethasree198/Fall-Detection-TinyML); [nesso-n1](https://github.com/haziqa5122/nesso-n1-fall-detection)

### Inferences
- In 2023–2026 the field moved toward ML/DL, and few new threshold algorithms appeared. PIPTO looks like the most recent peer-reviewed threshold pipeline that has public code.
- Validation schemes in recent papers vary widely (k-fold, LOSO, cross-dataset). Only Guo & Nakayama (2025) and Aderinola et al. (2024) report results on real falls (FARSEEING), which matters for older adults.
- A phone can easily run models of 1D-CNN, kNN/SVM or MiniRocket size. An app can run small Keras models (such as the RNN repo) only after conversion to TFLite.

### Gaps
- I could not open the full texts (MDPI, PMC and arXiv were blocked), so sampling rates, exact window parameters and per-class sensitivity/specificity for 3s2sub, the RNN paper and Fula & Moreno are missing.
- No code repository was confirmed for Guo & Nakayama 2025 or Fula & Moreno 2024. Their full texts would need to be checked for a data/code availability statement.
- I fetched only three GitHub repos (PIPTO, mlgig, rsusik). The others were not verified.
- None of the papers found reported a peer-reviewed, smartphone-only TinyML/TFLite deployment with measured false alarms per hour in older adults.

## Q2. Which are good candidates to ADD to (or swap into) the team's study? Top 3 ranking

### Takeaway
Rank: (1) Aderinola et al. 2024 time-series classifiers (code public, real-fall validation, false alarms reported per day); (2) Guo & Nakayama 2025 3s2sub kNN/SVM (smartphone-specific, fully specified features, LOSO plus cross-dataset, peer-reviewed; but code not confirmed); (3) Bartczak et al. 2025 smartphone RNN (code and weights public; but validation only on UniMiB-SHAR). Together these add a lightweight-ML arm and a DL arm to the team's three threshold algorithms.

### Cited Findings
- #1 Aderinola et al. 2024. Public repo with preprocessed SisFall/FallAllD [fetched]. F1 is 90.7% on real falls, with about 1 false alarm per 3 days (estimated) — [GitHub](https://github.com/mlgig/ts_fall_detection); [Springer](https://link.springer.com/chapter/10.1007/978-3-031-77066-1_4). Downsides: it is a conference/workshop paper (AALTD), FARSEEING data is available only on request, and the sensor is lumbar or thigh rather than a phone (placement not confirmed in snippet).
- #2 Guo & Nakayama 2025. The method is smartphone accelerometer only, with a 3 s window, two sub-windows, eight statistical features and 44 dimensions, classified with kNN/SVM. It was evaluated with LOSO, cross-dataset, and on FARSEEING (95.35% sensitivity / 98.12% specificity) [snippet] — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568134/). It is open access in *Sensors*, and a feature-based method is reproducible from the text if the features are fully listed (to be verified).
- #3 Bartczak et al. 2025. Smartphone data (UniMiB-SHAR), with notebook and `.h5` fold models public [fetched] — [GitHub](https://github.com/rsusik/fall_detection_rnn); [MDPI](https://www.mdpi.com/2076-3417/15/12/6688).
- Honourable mention: the 2024 *Measurement* cross-dataset study (Silva, Casilari, García-Bermúdez) as a methodological template for "lab-trained, tested on real-life" designs — [UMA repository](https://riuma.uma.es/entities/publication/044b23da-8d37-4245-9392-20de3918fc18)

### Inferences
- For a study about false positives on a phone, the most informative addition is #2, because it is the only one that is smartphone-specific, peer-reviewed in a journal and tested on real falls. #1 is the easiest to reproduce because its code exists, but it would have to be ported to phone placement.
- I would not swap out Kangas or Bourke3. They are the classic real-world references, and Bagalà 2012 already gives a real-world benchmark for comparing the team's phone results.
- I recommend against adding the IMU+CSI, CNN–Transformer or TinyML hobby projects: they are hardware-dependent, have no code, or are not peer reviewed.

### Gaps
- Whether all 44 features of 3s2sub are fully specified (formulas, sub-window overlap, sampling rate) needs to be checked in the full text.
- The license is unknown for both the PIPTO and mlgig repos, so the team should ask or use the code for research only, with citation.

## Q3. Has any recent paper re-evaluated PIPTO, Kangas or Bourke algorithms?

### Takeaway
I found no 2023–2026 paper that re-implements and re-evaluates PIPTO, Kangas 2008 or Bourke 2010 specifically. The closest is the classic real-world benchmark (Bagalà et al. 2012) plus recent cross-dataset studies showing that lab-trained detectors degrade on real-life data. This gap is exactly what makes the team's replication study a novel contribution.

### Cited Findings
- [H] Bagalà et al. 2012 (PLOS ONE, context only, outside the window) evaluated published algorithms on real-world falls. Kangas' algorithms gave fewer than 9 false alarms but sensitivity below 55%. Bourke1a and 1b gave 22–85 and 27–84 false alarms per 24 h, which was judged unacceptable (more than 2 per hour) [snippet] — [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0037062)
- [H] Silva, Casilari, García-Bermúdez, *Measurement* 235:114992 (2024), DOI 10.1016/j.measurement.2024.114992. AI detectors trained on simulated falls were tested on real falls and long-term daily-life recordings. Sensitivity, specificity and false alarm rate all degrade, with about 0.61–2.74 false positives per hour for LSTM/CNN models on about 11,542 h of data, which the authors call impractical. The per-hour figures come from a snippet — [UMA repository](https://riuma.uma.es/entities/publication/044b23da-8d37-4245-9392-20de3918fc18); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0263224124008777)
- [M] Fula & Moreno 2024: small-scope train/test produces over-optimistic rates and many false positives in real life [snippet] — [PubMed](https://pubmed.ncbi.nlm.nih.gov/38475215)
- [M] PIPTO's own comparison is internal only, against a heuristic method [45] on MMsys and a rule-based method [7] on KFall. Search found no later independent re-evaluation. The group's later YOLOv8 paper is vision-based, not inertial [snippet] — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10534597/); [ResearchGate YOLOv8](https://www.researchgate.net/publication/376698898_Fall_detection_paradigm_for_embedded_devices_based_on_YOLOv8)

### Inferences
- The literature consistently finds that real-life false alarms are the failure point, both for threshold methods (Bagalà 2012) and for DL methods (Silva et al. 2024). This supports the team's focus on false positives in on-phone use.

### Gaps
- A Google Scholar "cited by" check of PIPTO and Kangas 2008 was not possible (Semantic Scholar and Scholar were blocked or not used). A citation-level search might still find a 2024–2026 re-implementation.
