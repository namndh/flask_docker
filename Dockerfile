FROM ubuntu:latest
RUN apt update -y
RUN apt-get install -y python3-pip python3.7 build-essential
COPY src /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
