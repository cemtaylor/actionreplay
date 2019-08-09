FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y wget python3.7 python3-pip
CMD ["sh"]