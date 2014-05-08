OnTheMove
=========
Development Environment

In order to set up your dev environment create a virtual environment first. 

virtualenv <name of your environment>

cd into your environment and activate it 

source bin/activate

Once inside clone this repo. 

cd into the repo 

using pip install the requirements as such

pip install -r requirements/development.txt

Then do python manage.py syncdb

this command will create your dbs

after that make sure you can collect all the static files 

python manage.py collectstatic 


For Production
log into heroku whereever your repo is

heroku login

