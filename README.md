# Labor exchange

Training project for [a course on the Stepik](https://stepik.org/course/63298).

## Environment variables

### Django server

* ALLOWED_HOSTS;
* DB_HOST;
* DB_PORT;
* DB_USERNAME;
* DB_PASSWORD;
* DB_NAME.

### Docker compose required variables

* LABOR_EXCHANGE_IMAGE=labor-exchange-dev.

## Building of images

### Development

```bash
docker build -t labor-exchange-dev --target base .
```

### Production

```bash
docker build -t labor-exchange --target production .
```