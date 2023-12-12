# Test Fabric
## Test task for the interview
stack: Django, Docker, Celery (/Flower), Redis, Postgres

This project demonstrates how to send messages to a desired API using Django, Celery, Redis, and Postgres, all dockerized for easy deployment and scalability.

- Add dispatch object via DRF api page /api/v1/dispatch/
- ✨Magic happened and added task will be parsed by client's phone operator and tag
- Message will be sent according to the local time of the client, specified in the client's timezone
- Can be easily controlled by API

## Features

- Dispatch Object Management:
> Dispatch objects, containing essential dispatch information, can be added via the DRF API.
- Message Tracking:
> Every message, whether sent or not, is recorded along with the correct delivery status.
- Client Information Storage:
> Client information, including phone number, operator, timezone, and tags, is stored.
> The client's operator is automatically added, even if the operator field is left empty.
- Timezone-based Messaging:
> Messages are sent according to the specified timezone of the client.



## Installation

Ensure that Docker is installed on your machine. Follow these steps:

Navigate to the root folder of the repository.
Create .env and .env.db files in the root folder.
##### .env
```sh
#.env file
DJANGO_SECRET_KEY="Your django project secret key"
SEND_JWT_TOKEN="Your JWT token for api authentication"
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=dispatcher
SQL_USER=dispatcher
SQL_PASSWORD=dispatcher
SQL_HOST=db
SQL_PORT=5432
```
##### .env.db file:
```sh
POSTGRES_DB='dispatcher'
POSTGRES_USER='dispatcher'
POSTGRES_PASSWORD='dispatcher'
```
From a base dir of the repository:
```sh
docker-compose up --build
```

## Development

Want to contribute? Great!

While it is an Interview task, you can still make a contribution to improve this app.

