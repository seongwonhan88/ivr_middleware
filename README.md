# IVR-Stripe Middleware Application

A middleware application handling transaction between IVR client and [Stripe](https://stripe.com/)(Payment API service)

## Application Services & Framework 
* Django REST API
* Django 

## Getting Started 
These instructions will get you a copy of the project up and running on your local machine for development

### Prerequisites

* [pip3](https://pip.pypa.io/en/stable/)
* MySQL 
* pyenv or virtualenv

Create a MySQL user that matches your computer's user and try logging in(This is to test locally)

### Mac OS X
*  Install [Python 3](https://www.python.org/downloads/mac-osx/)
*  Install MySQL (Steps below)

```bash
brew doctor
brew update
brew install mysql
brew services start mysql
```


### Environment Variables
Ensure that the environment variables are properly set for your project. In your file system, make a new file `.bash_{filename}` and include in your `.bashrc`. 

Add the following, replacing with your own values where needed.

```
export IVR_DB_NAME="your database"
export IVR_DB_USER="your username"
export IVR_DB_PASSWORD="your password"
export IVR_DB_USER="your username"
export IVR_DB_PORT="your db port(default is 3306)"
export IVR_DB_HOST="localhost"
export STRIPE_API_KEY="your stripe secret key"
```

### Installing
