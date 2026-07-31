# Cold-Start Session-Based E-Commerce Purchase Intent Prediction

## Overview

This project presents a **Deep Learning-based Purchase Intent Prediction System** designed to address the **cold-start problem** in e-commerce. Traditional recommendation systems rely on users' historical interactions, making them ineffective for anonymous or first-time visitors. This project predicts whether a user is likely to make a purchase using only their current browsing session.

The system is built using the **YooChoose dataset**, where sequences of clicked products are processed and used to train a **Gated Recurrent Unit (GRU)** model. A **Graph Convolutional Network (GCN)** is also implemented as a baseline for comparison. The trained model is deployed through a **FastAPI** backend and integrated with a **React** frontend to provide real-time purchase predictions.

---

# Features

* Session-based purchase intent prediction
* Solves the cold-start recommendation problem
* GRU model for sequential clickstream learning
* GCN baseline comparison
* FastAPI REST API for inference
* React-based e-commerce demo interface
* Real-time purchase probability prediction
* Model evaluation using standard classification metrics

---

# Problem Statement

Most e-commerce recommendation systems require historical user data. However, a large percentage of website visitors browse anonymously without logging in. Since these users have no purchase history, traditional recommendation algorithms fail to personalize recommendations.

This project predicts purchase intent using only the sequence of products viewed during the current browsing session.

---

# Dataset

**Dataset:** YooChoose (RecSys Challenge 2015)

The dataset consists of:

* Clickstream data
* Purchase records
* Session IDs
* Item IDs
* Timestamps

The purchase dataset is used to generate labels indicating whether a browsing session resulted in a purchase.

---

# Project Workflow

```text
YooChoose Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Session Generation
        │
        ▼
Label Encoding
        │
        ▼
Sequence Padding
        │
        ▼
GRU Model Training
        │
        ▼
Model Evaluation
        │
        ▼
FastAPI Deployment
        │
        ▼
React Frontend
        │
        ▼
Real-Time Purchase Prediction
```

---

# Model Architecture

```
Input Session
      │
      ▼
Embedding Layer
      │
      ▼
GRU Layer
      │
      ▼
Dropout Layer
      │
      ▼
Fully Connected Layer
      │
      ▼
Sigmoid Activation
      │
      ▼
Purchase Probability
```

---

# Technologies Used

## Programming Language

* Python

## Deep Learning

* PyTorch

## Machine Learning

* Scikit-learn

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Backend

* FastAPI
* Uvicorn

## Frontend

* React

## Deployment

* Docker

## Version Control

* Git
* GitHub

---

# Project Structure

```
ColdStartPurchasePrediction/

├── dataset/
│   ├── yoochoose-clicks.dat
│   └── yoochoose-buys.dat
│
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── training.ipynb
│   └── evaluation.ipynb
│
├── model/
│   └── best_gru_purchase_intent.pth
│
├── backend/
│   ├── app.py
│   ├── predict.py
│   ├── model.py
│   └── requirements.txt
│
├── frontend/
│   └── React Application
│
├── Dockerfile
├── README.md
└── LICENSE
```

---

# Performance Evaluation

The trained model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

A Graph Convolutional Network (GCN) is implemented as a baseline to compare its performance with the GRU model.

---

# API Endpoint

### Predict Purchase Intent

**POST**

```
/predict
```

Example Request

```json
{
    "session": [214, 325, 412, 785]
}
```

Example Response

```json
{
    "purchase_probability": 0.84,
    "prediction": "Purchase"
}
```

---

# Future Enhancements

* Transformer-based sequential recommendation
* Attention mechanisms
* Explainable AI (XAI)
* Real-time recommendation engine
* Cloud deployment
* Online model retraining
* Personalized product recommendations

---

# Applications

* E-commerce platforms
* Personalized recommendation systems
* Customer behavior analysis
* Marketing campaign optimization
* Cart abandonment prediction
* Retail analytics

---

# Team Members

* Dhananjay Divekar
* Shubhankar Bhosale
* Aditya Jadhav
* Parth Kulkarni

---

# License

This project is developed for academic and educational purposes as part of the Mini Project for the Department of Computer Science Engineering (AI & ML), Kolhapur Institute of Technology's College of Engineering.
