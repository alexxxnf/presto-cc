# Coding Challenge


## Installation
Put this repository files into `/var/www/vhosts/cc/core`
### Virtual environment
This step is optional, you can use system Python and its packages.
1. Create virtual environment using Python 3.5  
`virtualenv -p /usr/bin/python3.5 /var/www/vhosts/cc/env`
2. Activate the environment  
`source /var/www/vhosts/cc/env/bin/activate`
3. Install requirements  
`pip install -r /var/www/vhosts/cc/core/reqiurements.txt`
4. Copy `config_default.py` from the `src` directory
and redefine configuration variables there.
Provide path to the file via `CONFIG` environmental variable.
5. Set `FLASK_APP` environmental variable (see [Running the application](#running-the-application)).
6. Create/update database structure  
`flask db upgrade` 

## Running the application
### Development
For development purposes the application can be run using built-in server.  
1. Activate virtual environment  
`source /var/www/vhosts/cc/env/bin/activate`
2. Set `FLASK_APP` environmental variable  
`export FLASK_APP=/var/www/vhosts/cc/core/app.py`
3. Run built-in server  
`flask run`

### Production
In production environment the app should be run using [nginx](https://nginx.org/) as a web server
and [uWSGI](http://projects.unbit.it/uwsgi) as an application server.
