FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirement.txt

COPY . /app

EXPOSE 8080

CMD ["python", "main.py"]