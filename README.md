## Digital - (LDSG) Local Development Setup Guide

### Prerequisite

- #### Have a docker installed in your pc, or mac, and make sure docker desktop is running

### Steps to setup and run application on local development pc

- Open your terminal and clone the project

        git clone https://github.com/uwevanopfern/digital_backend_software

- Navigate into project root

        cd digital_backend_software

- Once you are in the root project, Next steps, Build image and fire up container:

        docker-compose up --build
        
- Give permission to entrypoint.sh, cd in dsrs_docker_app folder, in digital_backend_sotware and run the below permission command

        chmod +x entrypoint.sh

- Make sure that two images are running: check running containers, has to be two, for app backend-software_dsrs_1, for postgreSQL backend-software_dsrs-db_1

        docker ps

- Run migrations:

        docker-compose exec dsrs python manage.py makemigrations
        docker-compose exec dsrs python manage.py migrate

- Check running server on this port: http://localhost:8080/

- Create superadmin in your project terminal:

        docker-compose exec dsrs python manage.py createsuperuser

- Create Currency and Territory models in your project terminal:

        docker-compose exec dsrs python manage.py create_models

- Create DSRs Model in your project terminal:

        docker-compose exec dsrs python manage.py create_dsrs

- Import Csvs(Create Resource Model): it may take between 7 to 25 minutes depending on the speed of your pc to finish importing all of 4000 csv data files

        docker-compose exec dsrs python manage.py import_csv_files

- Run tests in terminal and see if they pass:

        docker-compose exec dsrs python -m pytest

- Navigate to admin: http://localhost:8080/admin to view all your entry, and perfom any action you want, like Updation, Deletion on DSR Model, and others

## Endpoints to navigate

- All dsrs: http://localhost:8080/dsrs/
- Single dsr: http://localhost:8080/dsrs/2
- Resource Percentile: http://localhost:8080/resources/percentile/10?period_start=2020-01-01 00:00:00&period_end=2020-05-31 00:00:00&territory=ES

## The first two steps belong to the above questions

- Because there is django custom main command, which is:

        docker-compose exec dsrs python manage.py import_csv_files

- Create a cron job to run and may be schedule it to run during night hours because it takes time to finish up and populate all data into database

- Try to implement POSTGRES indexing, in django, for query optimazition

#### General steps to optimize django app

- For endpoing to resources, you may need to paginate data, and can try to use limit to increase the perfomance of query especially on listing ones
- Implementation of postgres logs to details of the query may be needed
- Alternative of postgres logs, Using Django Profiling tool, and check whats going in the query

NOTE: When you run some docker related commands like these below

        docker-compose up or docker-compose up --build

migrations get deleted, If that happens

MAKE SURE YOU REPEAT THE ABOVE PROCESS OF RE RUNNING THOSE COMMANDS OF CREATING SUPER USER, CREATE MODELS, AND THE MAIN ONE FOR IMPORTING CSV FILES
