FROM python:3.13-slim

RUN apt-get update && \
    apt-get clean && \
    apt-get autoremove

COPY requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

COPY src/ /app/

WORKDIR /app

CMD ["python", "main.py"]