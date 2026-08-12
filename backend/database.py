from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker

# --- Database Setup (Using Neon DB compatible dialect) --
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_JYpjNU0M6dQl@ep-aged-sunset-azdiss58.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define the ORM model for logging purposes
class PredictionLog(Base):
    __tablename__ = 'prediction_logs'
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow) 
    session_ids = Column(ARRAY(Integer), nullable=False) # Store session IDs as a PostgreSQL array of integers
    purchase_probability = Column(Float, nullable=False)
    prediction = Column(String, nullable=False)

def init_db():
    """Creates all tables defined by Base metadata."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Provides a transactional database session."""
    return SessionLocal()

def log_prediction(session_ids: list[int], prob: float, prediction: str):
    """
    Logs the successful prediction and its metadata to the PostgreSQL database.
    """
    try:
        db = get_db()
        new_log = PredictionLog(
            session_ids=session_ids, 
            purchase_probability=prob, 
            prediction=prediction
        )
        db.add(new_log)
        db.commit()
        print("Database log successful.")
    except Exception as e:
        # In a real application, you'd use proper logging here.
        print(f"WARNING: Failed to log prediction to DB: {e}")