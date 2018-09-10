FROM debian:9.4
LABEL maintainer "Taketoshi Kazusa <taketoshi.kazusa@gmail.com>"
ENV REFRESHED_AT 2018/09/07

RUN apt-get -qq update; \
    apt-get -qq -y upgrade; \
    apt-get -qq -y install \
        curl python python-dev python-pip \
        python-flask python-requests; \
    pip install --upgrade setuptools; \
    pip install --upgrade gcloud

ADD src /src
EXPOSE 8081
RUN ["chmod", "+x", "/src/backend.py"]
CMD ["python", "/src/backend.py"]
