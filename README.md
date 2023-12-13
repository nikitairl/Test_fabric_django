
# Test Fabric
## Test task for the interview
<p align="center">
<img src="https://github.com/nikitairl/Test_fabric_django/blob/master/disptacher/static/images/stats.png?raw=true" alt="alt text" width="200" height="200">
</p>
stack: Django, Docker, Nginx, Celery (/Flower), Redis, Postgres

This project demonstrates how to send messages to a desired API using Django, Celery, Redis, and Postgres, all dockerized for easy deployment and scalability.

- Add dispatch object via DRF api page /api/v1/dispatch/
- ✨Magic happened and added task will be parsed by client's phone operator and tag
- Message will be sent according to the local time of the client, specified in the client's timezone
- Can be easily controlled by API
- auth0 as an authentication service

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
Create .env and .env.db files in the project's root folder.
##### .env
```sh
# .env file
# django settings
DJANGO_SECRET_KEY="Your django project secret key"

# Dispatch target API
SEND_JWT_TOKEN="Your JWT token for api authentication"

# db
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=dispatcher
SQL_USER=dispatcher
SQL_PASSWORD=dispatcher
SQL_HOST=db
SQL_PORT=5432

# auth0 credentials
# configure you'r app in Auth0 and retrieve the corresponding variables
APP_DOMAIN='Domain'
APP_CLIENT_ID='Client id'
APP_CLIENT_SECRET='Secret'
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
Now the app should be available at http://127.0.0.1/ or http://127.0.0.1:80/.
Also you can access Flower for Celery tasks webui via http://127.0.0.1:5555/

## Development

Want to contribute? Great!

While it is an Interview task, you can still make a contribution to improve this app.

