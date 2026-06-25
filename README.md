# multi-task-distilbert-sentiment-depression-severity-detection
Multi-Task DistilBERT for Joint Sentiment and Depression Severity Detection

📌 Project Overview

This project implements a Multi-Task Learning (MTL) framework using DistilBERT to simultaneously perform:


🎭 Sentiment Classification — Negative / Neutral / Positive
🏥 Depression Severity Detection — Minimum / Mild / Moderate / Severe


By jointly training on both tasks, the model learns richer mental health representations compared to single-task models. The architecture uses CORAL (Consistent Rank Logits) for ordinal severity prediction, respecting the natural ordering of depression severity levels.

Datasets Used (6 Datasets)

This project merges 6 different mental health datasets for robust multi-task training:


 Datasets Used (6 Datasets)

This project merges 6 different mental health datasets for robust multi-task training:


Dataset 1   : Sentiment Analysis for Mental Health (Combined Data.csv) 
Source    :  [Kaggle – suchintikasarkar](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health)
Description :  Text labeled with mental health conditions: Depression, Suicidal, Bipolar, Anxiety, Stress, Normal 

Dataset 2 :   Reddit Depression Dataset (Reddit_depression_dataset.csv)
Source    :  [GitHub – usmaann](https://github.com/usmaann/Depression_Severity_Dataset) 
 Description  : Reddit posts labeled with depression severity: minimum / mild / moderate / severe 
 
Dataset 3 : DepressionEmo (combined.json) 
Source  : [GitHub – abuBakarSiddiqurRahman](https://github.com/abuBakarSiddiqurRahman/DepressionEmo) 
Description : Reddit posts annotated with fine-grained emotions like hopelessness, worthlessness, suicide intent 

Dataset 4 :  Reddit Depression Cleaned
Source   :  [HuggingFace – hugginglearners](https://huggingface.co/datasets/hugginglearners/reddit-depression-cleaned) 
Description : Cleaned Reddit posts with binary depression / non-depression labels 

Dataset 5 :  Mental Health Counseling Conversations 
Source :   [HuggingFace – Amod](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations) 
Description : Real counseling conversation data for mental health context 

Dataset 6 :  Suicide Watch (Suicide_Detection.csv) 
Source : [Kaggle – nikhileswarkomati](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch) 
Description : Reddit posts from r/SuicideWatch and r/teenagers labeled as suicide or non-suicide 

> ⚠️ **Note:** Some Dataset files are NOT included in this repository due to file size limits. Use the `download_data.py` script below to download them automatically.


 


