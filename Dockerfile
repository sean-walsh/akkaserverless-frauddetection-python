#FROM python:3.8.0-slim
FROM python:latest

# set the working directory in the container
WORKDIR /code
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
#ENTRYPOINT python ./fraud_detection.py
ENV HOST 0.0.0.0
ENV PORT 8080
EXPOSE 8080
CMD [ "python", "./fraud_detection.py" ]