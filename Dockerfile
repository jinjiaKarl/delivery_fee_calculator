FROM python:3.10.8-alpine3.16

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app .
EXPOSE 8080

CMD ["python3","main.py"]