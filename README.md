# IVR-Stripe Middleware Application

A middleware application handling transaction between IVR client and [Stripe](https://stripe.com/)(Payment API service)

## Application Services & Framework 
* Django REST API
* Django 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development

### Prerequisites
If you don't have the listed items below, click the link and follow the instruction

* Python Package - [pip3](https://pip.pypa.io/en/stable/)
* Database - [MySQL](https://formulae.brew.sh/formula/mysql) 
* Virtual Environment - [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv/blob/master/README.md) or [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)
* Payment Service - [Stripe API Key](https://stripe.com/docs/development)

### Environment Variables
Ensure that the environment variables are properly set for your project. In your file system, make a new file `.bash_{your filename}` and include in your `.bashrc`. 

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

### Installing the project
1) Copy the command below to your terminal to clone the repository

 > git clone https://github.com/seongwonhan88/ivr_middleware.git

2) Setup your pyenv or virtualenv using python version 3.6 or higher
 > - If you are using **virtualenv** make sure to activate with `source your_env/bin/activate` your environment after creation
 
 > - If you are using **pyenv-virtualenv** make sure to localize with `pyenv local your_env` your environment after creation

3) Install project requirements. 
 > - Change to the project directory. 
 > - Install project requirements with `pip install -r requirements.txt` 


### Django Basic Settings

**make sure that your environment variables match with the local database**

1) Export the environment variables from `.bash_{your filename}`
 > - command `source ~/.bash_{your filename}` 
 > - command `printenv` in your terminal to check if your variables are exported

2) Database (steps to follow)
 > - command `mysql>CREATE DATABASE {your database}` to create database (if you have trouble setting up, click [here](https://dev.mysql.com/doc/refman/8.0/en/creating-database.html) for troubleshoot)
 > - command `python manage.py migrate` in your terminal to migrate database schema

3) Fire up Django
 > - command `python manage.py runserver` to fire up the service
 > - if you see something like below, the middleware server is listening on port 8000

```
Django version 2.1.15, using settings 'ivr_payment.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Requesting API
**Once Django is ready to serve, you can start making a request**

### POST http://localhost:8000/api/payment/
* You can copy the cURL command below for simple testing

`curl -d '{"cc_num":"4111111111111111", "cvv":"123", "exp_date":"0221", "trans_id":"123345123"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/payment/`

* If you want to modify the JSON data and test vulnerability, you can use [Postman API](https://www.postman.com/)


## Behind The Architecture
### Capturing Request and Response data
Custom Django [Middleware](https://docs.djangoproject.com/en/2.1/topics/http/middleware/) was created to capture all request and response data into MySQL database. Since django middleware is called before request goes in and after response goes out, it was possible to capture all requests and response logs.

### Database modeling 
Saving as much as data from request and response was my number one concern since it could be used for troubleshooting. I decided to use NoSQL style field to our database to give more flexibility. Therefore [Django-MySql](https://django-mysql.readthedocs.io/en/latest/model_fields/json_field.html) is used to store JSONField. At the same time, it was important to distinguish certain fields for fast querying purpose. So common field such as response status code and request method(type) are separately stored.

### Exception handling 
Server-side should never assume that the client will always request correctly. Therefore error handling on missing data, wrote data input, or even sending an empty data needed to be handled correctly. Using [Django-REST-Framework](https://www.django-rest-framework.org/api-guide/serializers/#serializers)'s serializer is used to validate the each data type without writing too much code for error handling. 

### Data Formatting
Using Stripe requires certain format. IVR's request data was needed to be properly formatted in order to send request using Stripe. format handler function was made to make sure the IVR request data is adjusted.

### Sensitive Data Masking 
It was strictly forbidden to save credit card info to database. A masking function was created in middleware to make sure that the request log will only save the last 4 digits and mask the rest of the credit card info. 


## Author

* **Seongwon Han**
* If you have any questions please send me an email to *seongwonhan88@gmail.com*