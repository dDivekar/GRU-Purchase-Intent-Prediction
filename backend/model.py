import torch
import torch.nn as nn
from backend.config import VOCAB_SIZE, MAX_SEQ_LEN
# Using simple placeholder dimensions for demonstration
EMBEDDING_DIM = 64
HIDDEN_DIM = 128
NUM_LAYERS = 3

class SessionGRU(nn.Module):
    def __init__(self, vocab_size, embedding_dim=EMBEDDING_DIM, hidden_dim=HIDDEN_DIM, num_layers=NUM_LAYERS):
        super(SessionGRU, self).__init__()
        
        # Input Embedding Layer (Input: item indices, Output: vector)
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        # GRU/LSTM layer
        self.gru = nn.GRU(embedding_dim, hidden_dim, num_layers=num_layers, batch_first=True)
        # Dropout
        self.dropout = nn.Dropout(0.25)
        # Output Fully Connected Layer (Input: GRU output, Output: 1 probability score)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        """
        Performs the forward pass for the session data.
        x must be a LongTensor of shape (batch_size, seq_len).
        """
        # 1. Embed item IDs into dense vectors
        embedded = self.embedding(x)  # Shape: (batch_size, seq_len, embedding_dim)
        
        # 2. Pass through GRU
        output, hidden = self.gru(embedded) 
        
        # We are interested in the final hidden state output
        last_hidden_state = output[:, -1, :] # Take the last token's combined output features (simplified for this context)
        
        # In a typical session-based approach, we often take the *final* hidden state of the LSTMs. 
        # Let's refine to use the final sequence representation:
        last_sequence_output = output[:, -1, :] # (batch_size, hidden_dim)
        
        dropped = self.dropout(last_sequence_output)
        prediction = torch.sigmoid(self.fc(dropped))  # Output shape: (batch_size, 1)
        return prediction

# Instantiate the model using constants from config
model = SessionGRU(VOCAB_SIZE)