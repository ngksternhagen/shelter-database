Shelter Database
================

# Presentation

Shelter Database.



# Deployment

Tested with Python 3.5 and Python 2.7.


## Install and configure the database

```shell
$ sudo apt-get install -y postgresql postgresql-server-dev-9.4 postgresql-client
$ echo "127.0.0.1:5433:shelter:pgsqluser:pgsqlpwd" > ~/.pgpass
$ chmod 0600 ~/.pgpass
$ sudo -u postgres createuser shelter --no-superuser --createdb --no-createrole
$ sudo -u postgres createdb shelter --no-password
$ echo "ALTER USER pgsqluser WITH ENCRYPTED PASSWORD 'pgsqlpwd';" | sudo -u postgres psql
$ echo "GRANT ALL PRIVILEGES ON DATABASE shelter TO pgsqluser;" | sudo -u postgres psql
```

## Get the code and configure the database connection

```shell
$ git clone https://git.list.lu/cedric/shelter-database.git
$ cd shelter-database/
$ cp conf/conf.cfg-sample conf/conf.cfg
```

If you have chosen another database name, username or password:

```shell
$ sed -i '/database/d' conf/conf.cfg
$ sed -i '/database_url/d' conf/conf.cfg
$ echo '[database]' >> conf/conf.cfg
$ echo 'database_url = postgres://pgsqluser:pgsqlpwd@127.0.0.1:5433/shelter' >> conf/conf.cfg
```

Update appropriately the line just above.

## Install the Python requirements

```shell
$ sudo apt-get install python-pip python-dev
$ sudo pip install --upgrade -r requirements.txt
```

## Install the JavaScript requirements

```shell
$ sudo apt-get install nodejs-legacy
$ sudo npm install -g bower
$ bower install
```

## Initialization of the database

```shell
$ ./init_db.sh
Dropping database...
Creation of the database...
Importing page from 'data/pages/bibliography.html' ...
Importing page from 'data/pages/recommendations.html' ...
Importing page from 'data/pages/glossary.html' ...
Importing page from 'data/pages/about.html' ...
Importing page from 'data/pages/about_fr.html' ...
Importing base structure of shelters from 'data/shelters/Shelters_Structure.csv' ...
Creation of the admin user...
Importing shelters from 'data/shelters/20150518_Haiti_shelters.csv' ...
Importing shelters from 'data/shelters/Phil-Bangla-Burundi.csv' ...
Importing translation file from 'data/translations/sheltersDataTraduction_FR_rev_ED.csv' ...
```

An admin user with the password *password* will be created. You can create
an other user:

```shell
$ python manager.py create_user firstname.lastname@mail.org name password
```

## Launch the application

```shell
$ python runserver.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

The application is now running in standalone mode. For a use in production it is
recommended to run the applicaiton behind Apache or NGINX.



# Generation of the database UML graph

```shell
$ python manager.py uml_graph
```



# Example of requests to the Web Service

```shell
# Get the list of root category
$ GET http://127.0.0.1:5000/api/category?q={"filters":[{"name":"parent_id","op":"is_null"}]}
# Get the list of child category
$ GET http://127.0.0.1:5000/api/category?q={"filters":[{"name":"parent_id","op":"is_not_null"}]}
# Get information about the child category "Walls & Frame"
$ GET http://127.0.0.1:5000/api/category?q={"filters":[{"name":"parent_id","op":"is_not_null"},{"name":"name","op":"eq","val":"Walls %26 frame"}]}

# Get information about an attribute
$ GET http://127.0.0.1:5000/api/attribute?q={"filters":[{"name":"name","op":"eq","val":"Landform"}]}
$ GET http://127.0.0.1:5000/api/attribute?q={"filters":[{"name":"name","op":"eq","val":"Main hazards in country"}]}

# Get the translations of a string
$ GET http://127.0.0.1:5000/api/translation?q={"filters":[{"name":"original","op":"eq","val":"Name of shelter"}]}
```



# License

This application is under **TO BE DEFINED** license.



# Contact

[Luxembourg Institute of Science and Technology](http://www.list.lu)
