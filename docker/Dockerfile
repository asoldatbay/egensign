ARG PYTHON_VERSION=3.8

FROM python:3

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN apt-get update


WORKDIR ${APP_HOME}

COPY ./requirements.txt requirements.txt

RUN apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev

RUN #python setup.py clean --all

RUN pip install --no-cache-dir --force-reinstall reportlab

RUN python -m pip install --upgrade pip setuptools

RUN pip install -r requirements.txt

COPY ./docker/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./src .

ENTRYPOINT ["/entrypoint"]
CMD [ "/start" ]