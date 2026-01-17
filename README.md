# Project 03: NLP Sentiment & Intelligence Dashboard 🧠🎭

A dual-tier Natural Language Processing (NLP) project that demonstrates the evolution from basic sentiment detection to a sophisticated, hybrid intelligence engine. This project focuses on solving the "Nuance Problem" in AI—handling intensity, sarcasm, and subjectivity.

---

## 📂 Project Architecture

This repository contains two distinct levels of NLP analysis to showcase technical progression:

### 1. Basic Sentiment (`sentiment-basic.py`)
* **Engine:** `TextBlob`
* **Focus:** Core Polarity (-1.0 to 1.0) and Subjectivity (0.0 to 1.0).
* **Goal:** A straightforward, rule-based approach for factual text analysis.

### 2. Advanced Intelligence (`nlp-intelligence.py`)
* **Engine:** **Hybrid Model** (`VADER` + `TextBlob`)
* **Focus:** Emotional Intensity & Contextual Nuance.
* **Key Logic:**
    * **VADER:** High-accuracy scoring for social media, slang, and punctuation (recognizes `!!!` and `CAPS` as emotional amplifiers).
    * **Consensus Check:** Cross-references both models to flag potential **Sarcasm** or **Mixed Emotions** when scores contradict.



---

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **NLP Frameworks:** `vaderSentiment`, `TextBlob`
* **Environment:** Docker (Debian Slim)
* **Logic:** Lexicon and Rule-based Sentiment Analysis

---

## 🐳 Containerization (Docker)

To ensure the linguistic "corpora" (the AI's dictionary) are always available regardless of the host OS, the project is fully containerized.

### Build the Unified Image
```bash
docker build -t sentiment-pro .