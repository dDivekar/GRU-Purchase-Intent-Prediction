import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import torch
import json

# Local modules
from backend.model import model 
from backend.database import log_prediction 
from backend.config import WEIGHTS_PATH 

# --- Initialization: Load Model and App ---
# THIS IS THE LINE THAT WAS MISSING:
app = FastAPI(title="GRU Purchase Intent Predictor API")

@app.on_event("startup")
def load_model():
    """Loads PyTorch model weights into memory when the application starts."""
    global model
    print(f"Attempting to load model from: {WEIGHTS_PATH}")
    try:
        model.load_state_dict(torch.load(WEIGHTS_PATH))
        print("Model loaded successfully.")
    except FileNotFoundError:
        print(f"ERROR: Model weights not found at {WEIGHTS_PATH}. The API will run but predictions will fail.")
        pass 
    except Exception as e:
        print(f"CRITICAL ERROR loading model: {e}")

# --- Data Schemas ---
class SessionRequest(BaseModel):
    """Input schema for the /predict endpoint."""
    session_ids: list[int] = Field(..., description="Sequence of product IDs (clickstream)")

@app.post("/predict/", response_model=dict)
async def predict(request: SessionRequest):
    """
    Accepts a clickstream session and returns the purchase probability and prediction label.
    Logs the result to PostgreSQL database upon success.
    """
    session_ids = request.session_ids

    # --- Configuration Variables ---
    MAX_SEQ_LEN = 20  
    PADDING_ID = 0    

    # --- 1. Preprocessing Logic (Padding/Truncation) ---
    try:
        input_tensor = torch.LongTensor(session_ids)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid session ID format.")

    current_len = len(session_ids)
    seq_len = min(current_len, MAX_SEQ_LEN)
    
    truncated_tensor = input_tensor[:seq_len]

    pad_amount = MAX_SEQ_LEN - seq_len
    if pad_amount > 0:
        padded_tensor = torch.nn.functional.pad(
            truncated_tensor, 
            (0, pad_amount), 
            "constant", 
            value=PADDING_ID 
        )
    else:
        padded_tensor = truncated_tensor

    batched_tensor = padded_tensor.unsqueeze(0)

    # --- 2. Model Inference ---
    with torch.no_grad():
        prediction = model(batched_tensor)
        prob = prediction.item()
    
    # --- 3. Postprocessing & Output Generation ---
    pred_str = "Purchase" if prob >= 0.5 else "No Purchase"

    result = {
        "purchase_probability": round(prob, 4),
        "prediction": pred_str
    }

    # --- 4. Logging (Must happen AFTER successful prediction) ---
    try:
        log_prediction(session_ids, prob, pred_str)
    except Exception as e:
        print(f"WARNING: Failed to log result after prediction. Error: {e}")

    return result

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "GRU Predictor"}