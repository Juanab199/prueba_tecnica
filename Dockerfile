ARG BUILD_IMAGE=python:3.9.4

FROM ${BUILD_IMAGE} as base-build

WORKDIR /src

COPY requirements.txt /src/
RUN pip install --upgrade pip==20.2.3 && pip install -r requirements.txt
RUN pip install gunicorn

COPY src /src

RUN pytest

USER root
RUN chmod u+x /src/gunicorn.sh

RUN useradd -ms /bin/sh admin
USER admin

EXPOSE 8080

ENTRYPOINT [ "sh", "/src/gunicorn.sh" ]