# base image
FROM python:3.11-slim

# working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir fastapi uvicorn pydantic scikit-learn numpy pandas xgboost joblib

# copy application files and codes
COPY app.py .
COPY model/ ./model/
COPY schema/ ./schema/

# expose the port for fast api
EXPOSE 8000

# command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]