# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies for both Basic and Advanced scripts
RUN pip install --no-cache-dir textblob vaderSentiment

# Pre-download the TextBlob corpora (dictionary data)
RUN python -m textblob.download_corpora

# Copy all your project files into the container
COPY . .

# Default command runs the Advanced Intelligence Engine
# We use -u to force unbuffered output so you see logs in real-time
CMD ["python", "-u", "nlp-intelligence.py"]