# Project Overview: Cold-Start Session-Based E-Commerce Purchase Intent Prediction

## Objective
Implement a deep learning-based purchase intent prediction system designed to address the cold-start problem in e-commerce[cite: 1]. The system uses a trained Gated Recurrent Unit (GRU) model to predict purchase intent based on an anonymous user's current browsing session (sequence of clicked product IDs)[cite: 1]. The model will be served via a FastAPI backend[cite: 1] and consumed by a native Android application.

## Current State
*   **Model:** The GRU model is fully trained on the YooChoose dataset (RecSys Challenge 2015)[cite: 1].
*   **Artifacts:** The model weights are saved at `model/best_gru_purchase_intent.pth`[cite: 1].
*   **Pending Work:** The FastAPI backend needs to be finalized to serve the model[cite: 1], and the native Android application needs to track user clickstreams and communicate with the backend.

## Tech Stack
*   **Deep Learning:** PyTorch[cite: 1]
*   **Backend API:** FastAPI, Uvicorn, Python[cite: 1]
*   **Frontend (Target):** Native Android (Java, XML UI)
*   **Database (Target):** PostgreSQL (for logging interactions and future model retraining)

---

## Agent Instructions: Automation Tasks

AI Agent: Please execute the following tasks in order. Ensure all code is modular, well-documented, and handles edge cases (e.g., missing data, network failures).

### Task 1: Construct the FastAPI Backend (`backend/`)
1.  **Create `model.py`:** Define the PyTorch `nn.Module` class (`SessionGRU`) matching the architecture of the trained model. It must include an Embedding layer, a GRU layer, a Dropout layer, a Fully Connected layer, and a Sigmoid activation[cite: 1].
2.  **Create `app.py`:**
    *   Initialize a FastAPI application.
    *   Load the PyTorch model (`best_gru_purchase_intent.pth`) into memory on startup.
    *   Define a POST endpoint at `/predict`[cite: 1].
    *   **Input Schema:** Accept JSON in the format `{"session": [214, 325, 412, 785]}`[cite: 1].
    *   **Preprocessing:** Implement padding/truncation logic to ensure the incoming session array matches the input dimensions expected by the GRU. Implement a fallback for unknown Item IDs (Out-of-Vocabulary).
    *   **Output Schema:** Return JSON in the format `{"purchase_probability": 0.84, "prediction": "Purchase"}`[cite: 1]. The prediction string should be "Purchase" if probability >= 0.5, else "No Purchase".

### Task 2: Backend Database Integration
1.  **PostgreSQL Setup:** Integrate SQLAlchemy or psycopg2 in the backend.
2.  **Logging Mechanism:** After every prediction, asynchronously log the `session` array, the `purchase_probability`, and a timestamp to a PostgreSQL database table named `prediction_logs`.

### Task 3: Android Frontend Integration (Java)
1.  **Retrofit Setup:** Generate the necessary Java classes to set up a Retrofit2 client communicating with the FastAPI endpoint.
2.  **Data Models:** Create `SessionRequest.java` and `PredictionResponse.java` matching the API schemas.
3.  **Clickstream Tracking:** Generate a utility class or ViewModel logic in Java to temporarily buffer integer Product IDs as the user navigates the app.
4.  **API Call Logic:** Write the asynchronous API call to send the buffered session to the `/predict` endpoint after 3 item clicks.
5.  **Dynamic UI:** Provide XML layout snippets and Java logic to display a promotional bottom sheet (using a dark, minimalist aesthetic—strictly avoid blue tones) if the `purchase_probability` returned is > 0.75.

---

## Project Structure Expected

```text
ColdStartPurchasePrediction/
├── dataset/
│   ├── yoochoose-clicks.dat[cite: 1]
│   └── yoochoose-buys.dat[cite: 1]
├── model/
│   └── best_gru_purchase_intent.pth[cite: 1]
├── backend/
│   ├── app.py[cite: 1]
│   ├── model.py[cite: 1]
│   ├── database.py
│   └── requirements.txt[cite: 1]
├── android_app/
│   ├── network/
│   │   ├── RetrofitClient.java
│   │   ├── PredictionApi.java
│   │   ├── SessionRequest.java
│   │   └── PredictionResponse.java
│   ├── viewmodel/
│   │   └── SessionTrackerViewModel.java
│   └── res/layout/
│       └── promo_bottom_sheet.xml
└── README.md[cite: 1]