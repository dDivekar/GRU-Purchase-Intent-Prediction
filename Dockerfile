FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies (using --no-cache-dir to keep the image lightweight)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using the correct folder structure
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]