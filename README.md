[![Build Status](https://travis-ci.com/jadonwolffs/csc3003s-capstone.svg?token=42WKBBESQyTJCATo8mTj&branch=master)](https://travis-ci.com/jadonwolffs/csc3003s-capstone)
# PneumoVis
Capstone Pneumococal Infection Visualisation Project - [PneumoVis](https://github.com/jadonwolffs/csc3003s-capstone)
## Implementation and releases
Click [here](http://bit.ly/csc3003s-capstone) to check out the live site

## Installation
### Pre-requisites
*   [Python (version 3+) and pip](https://www.python.org/)
*   [PostgreSQL](https://www.postgresql.org/)
### Database setup
1.  Login to PostgreSQL
    *   On Windows:     `psql -U postgres`
    *   On Linux/UNIX:  `sudo -u postgres psql`
2.  Create database
    `CREATE DATABASE dbname;` - replace dbname with the name of the DB you want to create, take note of it because you'll need it for the server settings.
3.  Create a user to manage the individual database (other than postgres)
    `CREATE USER dbadmin WITH PASSWORD 'password';` - replace dbadmin and password with values of your choice, take note of them because you'll need them for the server settings.
4.  Alter the settings of the new user to ensure that they are Django compatible
    ```sql
    ALTER ROLE dbadmin SET client_encoding TO 'utf8';
    ALTER ROLE dbadmin SET default_transaction_isolation TO 'read committed';
    ALTER ROLE dbadmin SET timezone TO 'UTC';
    ```
    Note: replace dbadmin with whichever user you created in step 3.
5.  Grant full privileges to the user on the db
    `GRANT ALL PRIVILEGES ON DATABASE dbname TO dbadmin;`
    Note: replace dbadmin with whichever user you created in step 3. and dbname with the name of the database you created in step 2.
6.  Exit postgres using `\q` or inspect the current structure using `\l`

### Server setup
1.  Clone the repo
    1.  Clone:
        *   via HTTPS:  `https://github.com/jadonwolffs/csc3003s-capstone.git`
        *   via SSH:    `git@github.com:jadonwolffs/csc3003s-capstone.git`
    2.  Navigate in with: `cd csc3003s-capstone`
2.  Create a new Python virtual environment
    `python -m venv nameofvenv` - will create a virtual environment named `nameofvenv`
3.  Activate the virtual environment 
    *   Linux and MacOS: `source nameofvenv/bin/activate`
    *   Windows: `.\nameofvenv\Scripts\activate`
4.  Navigate into the `pneumovis` directory
    `cd pneumovis`
5.  Create a file called `local_settings.py` and fill it as follows:
    ```python
    # Secret key
    SECRET_KEY = 'some secret key'
    # Debug
    DEBUG = True #or False for deployments
    # Databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',         # the name of the database
            'USER': '',         # name of the user with access to the db
            'PASSWORD': '',     # password of that user
            'HOST': 'localhost' # address of the host
        }
    }
    # Hosts
    ALLOWED_HOSTS = ['*']
    # Email - currently not used
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = True
    ```
    Be sure to replace the database settings with the ones you made on postgres when setting that up.
6.  Install the requirements
    `pip install -r requirements.txt`
7.  Run the Django migrations
    `python manage.py migrate`
8.  Create a superuser to access the admin area with
    `python manage.py createsuperuser` and follow the onscreen prompts
9.  Collect the static files into the root so that Django can find and serve them
    `python manage.py collectstatic`
10.  Run the server
    `python manage.py runserver`

## Docs

### Official documentation
*   [django](https://docs.djangoproject.com/en/2.2/)
*   [dash plotly](https://dash.plot.ly/)
*   [django-plotly-dash](https://django-plotly-dash.readthedocs.io/en/latest/index.html)

### Unofficial resources
*   [Django cheatsheet gist](https://gist.github.com/bradtraversy/0df61e9b306db3d61eb24793b6b7132d)
*   [Django deployment gist](https://gist.github.com/bradtraversy/cfa565b879ff1458dba08f423cb01d71)

## Testing
For testing it is imperative that you give the dbadmin user permissions on the DB
```sql
ALTER USER dbadmin CREATEDB;
```


## Credits
* [A'aisha Dout](https://github.com/adout1902)
* [Kiara Beilinsohn](https://github.com/kiaraBeilinsohn)
* [Jadon Wolffs](https://github.com/jadonwolffs)

## Requirements
* [csvkit](https://github.com/wireservice/csvkit) (not included in requirements.txt, has to be set up manually)
```python
Django==2.2.4
gunicorn==19.9.0
Pillow==5.2.0
psycopg2==2.7.5
psycopg2-binary==2.7.5
pytz==2019.1
sqlparse==0.3.0
django-plotly-dash==1.0.1
pandas==0.25.0
plotly==4.1.0
```
## Things to inspire
* [Information is Beautiful](https://informationisbeautiful.net/)

## TODO

### Jadon
#### Misc
* [x] contacts page
    * [x] details of Dr Dube
    * [x] details of students
* [x] uploads
    * [x] form input
    * [x] process files
    * [x] create swabs
* [x] redesign admin
* [ ] night mode
* [x] fix csv pathing


* [ ] fill out about page (lorem ipsums)