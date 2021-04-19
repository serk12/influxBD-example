FROM python:3.8-alpine

RUN pip install influxdb pandas
CMD sleep 1000
