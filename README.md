# 📰 Fake News Detector using Logistic Regression

A machine learning-powered system that classifies news articles as **real** or **fake** using a **Logistic Regression** model. This project uses **Natural Language Processing (NLP)** techniques to preprocess text data and build a lightweight, effective binary classifier.

---

## 📌 Features

- ✅ Detects fake vs. real news using **Logistic Regression**
- 🧹 Preprocessing pipeline includes:
  - Text cleaning (removing punctuation, lowercasing, etc.)
  - Tokenization and stopword removal
  - **TF-IDF vectorization**
- 🌥️ Visualizations using **WordCloud** to show common words in fake vs. real news
- 📊 Performance metrics:
  - **Confusion matrix**
  - **Accuracy, precision, recall, F1-score** via classification report
- 📓 Easy-to-use and explore via **Jupyter Notebook**
- ⚡ Lightweight and fast — ideal for small to medium datasets

---

## 🧠 Machine Learning Approach

1. **Dataset**:
   - A labeled dataset of news articles with `title`, `text`, and `label` (`FAKE` or `REAL`)

2. **Preprocessing**:
   - Clean the text (remove symbols, lowercase, etc.)
   - Tokenize and remove stopwords
   - Convert text to numerical data using **TF-IDF Vectorizer**

3. **Model**:
   - Train a **Logistic Regression** classifier on the TF-IDF vectors
   - Evaluate using a train/test split

4. **Evaluation**:
   - Use confusion matrix and classification report
   - Generate word clouds for better understanding of feature distribution

---

## 🛠 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
