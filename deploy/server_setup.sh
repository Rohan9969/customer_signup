#!/usr/bin/env bash

# TODO: Set values for PROJECT_GIT_URL, PROJECT_NAME and APP_NAME
PROJECT_GIT_URL='https://github.com/Rohan9969/customer_signup.git'
PROJECT_NAME='customer_signup'
PROJECT_APP_NAME='cust_signup_api'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
apt-get update
apt-get install -y python3-dev sqlite python-pip supervisor nginx git

# Upgrade pip to the latest version.
pip install --upgrade pip
pip install virtualenv

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/$PROJECT_NAME

mkdir -p $VIRTUALENV_BASE_PATH
virtualenv  $VIRTUALENV_BASE_PATH/$PROJECT_APP_NAME

source $VIRTUALENV_BASE_PATH/$PROJECT_APP_NAME/bin/activate
pip install -r $PROJECT_BASE_PATH/$PROJECT_NAME/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/$PROJECT_NAME/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/$PROJECT_NAME/deploy/supervisor_cust_signup_api.conf /etc/supervisor/conf.d/$PROJECT_APP_NAME.conf
supervisorctl reread
supervisorctl update
supervisorctl restart $PROJECT_APP_NAME

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/$PROJECT_NAME/deploy/nginx_cust_signup_api.conf /etc/nginx/sites-available/$PROJECT_APP_NAME.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/$PROJECT_APP_NAME.conf /etc/nginx/sites-enabled/$PROJECT_APP_NAME.conf
systemctl restart nginx.service

echo "DONE! :)"
