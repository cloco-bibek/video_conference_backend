FROM python:3.13-slim

WORKDIR /usr/src/app

# Copy the entire app directory
COPY ./app /usr/src/app/app

# Copy requirements.txt separately
COPY ./app/requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

# Update the CMD to use the correct module path
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]