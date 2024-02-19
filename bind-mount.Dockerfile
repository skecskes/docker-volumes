FROM python:3.10-slim-buster

COPY requirements.txt  requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
VOLUME ["/app/temp"]

EXPOSE 80
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=80"]