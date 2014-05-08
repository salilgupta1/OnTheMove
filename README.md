OnTheMove
=========
Development Environment

In order to set up your dev environment create a virtual environment first. 

<code>virtualenv name of your environment </code>

cd into your environment and activate it 

<code>source bin/activate</code>

Once inside clone this repo. 

cd into the repo 

using pip install the requirements as such

<code>pip install -r requirements/development.txt</code>

Then do <code>python manage.py syncdb</code>

this command will create your dbs

after that make sure you can collect all the static files 

<code>python manage.py collectstatic </code>


For Production
log into heroku whereever your repo is

<code>heroku login</code>

