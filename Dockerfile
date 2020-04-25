FROM python:3.7 as base
LABEL maintainer="Nick Balandin <balandin.nick@gmail.com>"

WORKDIR /opt/labor-exchange
ENTRYPOINT ["./docker-entrypoint.sh"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

FROM base as production
