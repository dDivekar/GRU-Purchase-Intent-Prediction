# Android Implementation & Production Deployment Plan

This document outlines the step-by-step strategy for taking the GRU-Purchase-Intent-Prediction project from a local backend to a production-ready cloud backend with a functional Android frontend.

## Phase 1: Backend Cloud Deployment
*Goal: Move the heavy PyTorch inference off the local laptop and into a cloud environment.*

- [ ] **1.1 Dockerize the Backend**
  - [ ] Create a `Dockerfile` for the FastAPI app.
  - [ ] Ensure Python 3.9+, PyTorch (CPU version to save costs), and FastAPI dependencies are included.
  - [ ] Add a `requirements.txt` specifically for the backend branch.
- [ ] **1.2 Cloud Hosting Setup**
  - [ ] Choose a hosting provider (Render, Railway, or AWS EC2).
  - [ ] Connect the GitHub repository to the hosting provider (target the `Backend-Implementation` branch).
  - [ ] Deploy the Docker container and secure the public API URL.
- [ ] **1.3 Security & Database**
  - [ ] Add basic API Key authentication to `app.py` to prevent unauthorized inference requests.
  - [ ] Provision a cloud PostgreSQL database (e.g., Supabase or Render Postgres) and update the backend connection string.

## Phase 2: Android Frontend Foundation
*Goal: Establish the base Android e-commerce UI using an open-source clone.*

- [ ] **2.1 Select & Clone Base Repository**
  - [ ] Review Android E-Commerce clones (e.g., `saurabhkharade/E-CommerceApp` for Kotlin or `hiteshsahu/ECommerce-App-Android` for Java).
  - [ ] Integrate the clone's UI code into this `Android-Implementation` branch.
- [ ] **2.2 Clean the Clone**
  - [ ] Remove existing mock backends (Firebase, local SQLite, or static JSON files).
  - [ ] Strip out unnecessary UI features that don't serve the purchase intent prediction use case.

## Phase 3: Android API Integration
*Goal: Connect the Android UI to the cloud-hosted GRU model.*

- [ ] **3.1 Network Layer Setup**
  - [ ] Add **Retrofit** and **Gson** dependencies to the Android `build.gradle`.
  - [ ] Create data classes/models for the API request (Clickstream session data) and response (Intent Prediction).
  - [ ] Build the Retrofit API Interface using the public URL from Phase 1.
- [ ] **3.2 Clickstream Tracking**
  - [ ] Implement click listeners on product items to track user interactions.
  - [ ] Format the interaction history into the YooChoose dataset format expected by `item_encoder.pkl`.
- [ ] **3.3 Asynchronous Inference**
  - [ ] Ensure API calls are executed on background threads (using Coroutines or RxJava) to prevent UI freezing.
  - [ ] Display loading states in the UI while waiting for the prediction.

## Phase 4: Final Testing & Optimization
- [ ] **4.1 End-to-End Testing**
  - [ ] Simulate user sessions on the Android emulator/device.
  - [ ] Verify predictions are returned and displayed accurately.
  - [ ] Check PostgreSQL database to ensure user interactions and predictions are being logged.
- [ ] **4.2 Performance**
  - [ ] Optimize payload sizes between Android and the FastAPI backend.