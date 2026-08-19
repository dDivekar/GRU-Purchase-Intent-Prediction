import os

VOCAB_SIZE = 21129
MAX_SEQ_LEN = 20
PADDING_ID = 0  # Assuming item ID 0 is used for padding/unknown items

# Add a class or simple structure to hold model configuration constants
class ModelConfig:
    CONFIG = {
        'VOCAB_SIZE': VOCAB_SIZE,
        'MAX_SEQ_LEN': MAX_SEQ_LEN,
        'PADDING_ID': PADDING_ID
    }
WEIGHTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "best_gru_purchase_intent.pth"))