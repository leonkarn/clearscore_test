FROM python:3.8
ADD main/ home/
COPY requirements.txt .
RUN pip install -r requirements.txt
