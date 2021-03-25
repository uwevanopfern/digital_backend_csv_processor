# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/dsrs_docker_app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/dsrs_docker_app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/dsrs_docker_app/entrypoint.sh
RUN chmod +x /usr/src/dsrs_docker_app/entrypoint.sh

# copy project
COPY . /usr/src/dsrs_docker_app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/dsrs_docker_app/entrypoint.sh"]