FROM python:3.11-slim
WORKDIR /app
COPY app.py .
COPY templates/ templates/
RUN apt-get update && apt-get install -y docker.io
RUN pip install flask
CMD ["python", "app.py"]
