FROM python:3.10

COPY requirements.txt ${WORKING_DIR}/

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
