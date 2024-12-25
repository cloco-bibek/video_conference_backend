FROM python:3.11-slim

WORKDIR /usr/src/app
COPY app /usr/src/app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]