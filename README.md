# Getting Started

1. setup the airavata-django-portal locally. See
    https://github.com/apache/airavata-django-portal.

    Then, activate the virtual environment for the airavata-django-portal:
    
    ```
    cd ../airavata-django-portal
    source venv/bin/activate
    ```

2. In order to replicate some data for interactwel, there's a dataset provided on this repository
    You need to add or replace the `db.sqlite3` in the directory airavata-django-portal with `db.sqlite3`
    provided in the `data` directory.

3. Change to the directory of this project and install this project as a
    python package in the airavata-django-portal's virtual environment:
    ```
    cd ../interactactwel-django-app/
    pip install -r requirements.txt
    pip install -e .
    ```
    Note: `python setup.py develop` also builds the Vue JS app.
    
4. Go back to the airavata-django-portal and start the server
    ```
    cd ../airavata-django-portal
    python manage.py migrate
    python manage.py runserver
    ```
5. Browse `http://localhost:8000/` and login to the portal.
6. Browse the `db.sqlite3` in airavata-django-portal through a sqlite database browser
    and change the `username`, `firstname`, `lastname`, and `email` columns in `interactwel_user` table.
    So, that the interactwel data would be linked to your login.

7. The InterACTWEL Dashboard will be available at http://localhost:8000/interactwel/ with data.

## Run Vue js app in development mode

Go to interactwel/ directory

Run ```npm run serve``` to locally run the vue app

## Build Vue js app for production use

Run ```npm run build``` 

----
**Older instructions**

## To start the Django app

Go to interactwel directory

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

##Wagtail CMS
After running above commands, to create a superuser run,
```
./manage.py createsuperuser
```

Browse the admin panel using

```
localhost:8000/cms
```

Browse the web site using

```
localhost:8000/home
```

----


## REST API

Rest API is exposed in http://localhost:8000/api

#### Resources 

##### Subbasin: http://localhost:8000/api/subbasins

Get All
```
GET http://localhost:8000/api/subbasins/
```

Get one
```
GET http://localhost:8000/api/subbasins/1
```

Create 
```
POST http://localhost:8000/api/subbasins/

{
    "detail_json": <JSON COntent>
}
```
 

