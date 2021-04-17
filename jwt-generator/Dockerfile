FROM python:3.7-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY google-jwt-client.py .

ENTRYPOINT ["python3","google-jwt-client.py"]