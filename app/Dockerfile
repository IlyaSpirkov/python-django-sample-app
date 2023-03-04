FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y locales && \
    apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev && \
    echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    python -m pip install poetry==1.3.1 && \
    poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN python -m pip install --upgrade pip && poetry install --no-root
COPY ./ /app/

RUN mkdir -p /app/sample/static && python manage.py collectstatic --noinput
EXPOSE 80
CMD /usr/local/bin/gunicorn --config /app/gunicorn.conf
