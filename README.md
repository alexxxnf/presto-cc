# Coding Challenge
This repo demonstrates a RESTful API that returns a list of menu items for a restaurant.
Menu items contain a list of modifiers which may have their own modifiers.
So API returns a tree-like structure.

I decided that one modifier may belong to multiple "standalone" items, thus I created
one table with all the items including modifiers and one extra table to store relations.

Considering nested nature of items, I decided to retrieve them from DB
using singe recursive SQL query.

In real life nested structures may become too big to handle. Depending on the application,
it may be better to use flat lists that can be paginated. Also, it may be useful
to include some meta-information in response.

The solution uses Code-First approach with SQLAlchemy migrations handled by Alembic.

If I had more time I would have included tests and dockerized this repo.

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

### DB config
1. Copy `config_default.py` from the `src` directory
and redefine configuration variables there.
Provide the path to the file via `CONFIG` environmental variable.
2. Set `FLASK_APP` environmental variable (see [Running the application](#running-the-application)).
3. Create/update database structure  
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
