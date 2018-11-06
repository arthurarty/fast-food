[![Coverage Status](https://coveralls.io/repos/github/arthurarty/fast-food/badge.svg?branch=develop)](https://coveralls.io/github/arthurarty/fast-food?branch=develop)
[![Build Status](https://travis-ci.com/arthurarty/fast-food.svg?branch=develop)](https://travis-ci.com/arthurarty/fast-food)
[![Maintainability](https://api.codeclimate.com/v1/badges/0d7befbf06875d2ca626/maintainability)](https://codeclimate.com/github/arthurarty/fast-food/maintainability)
## Fast-Food-Fast 
A food delivery service app for a restaurant.

# Link to demo on Heroku
https://arty-fast.herokuapp.com/

## Getting Started
* Clone the repo https://github.com/arthurarty/fast-food

### Prerequisites

Listed below are the python packages need to run the application.

* `Python 3.5` or greater : Python is interpreted high-level programming language for general-purpose programming. [Download python](https://www.python.org/downloads/)
* `Virtualevn` : A tool for creating isolated Python environments. [Get-virtualenv](https://packaging.python.org/key_projects/#virtualenv) 
* `Postman` : Postman is a powerful tool for performing integration testing with your API. [Get-postman](https://www.getpostman.com/)
* `Postgres` : An open source relational database management system ( DBMS ) developed by a worldwide team of volunteers. Similar commands to msyql. 

### Installing

A step by step series of examples to get the application up and running. Before you run the commands listed below, ensure you are working in virtual env. 

Using terminal or command line prompt enter the directory fast-fast.

```
cd fast-food
```

- Install the application requirements.
- Using postgres create a database called fastfood.
- Go to config.py file and change the password to your password in each DATABASE_URL these are on line 21 and 29.

```
pip install -r requirements.txt
```
Checkout the develop branch

```
git checkout develop
```
Run the application

```
python run.py
```
Example of output
```(fast-food) C:\Users\Arty\fast-food>python run.py
 Serving Flask app "app" (lazy loading)
 Environment: production
 WARNING: Do not use the development server in a production environment.
 Use a production WSGI server instead.
 Debug mode: on
 Restarting with stat
 Debugger is active!
 Debugger PIN: 177-242-549
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Use postman to intract with the application. 
## Running the tests

Tests for this application are runnning using the [pytest framework.](https://docs.pytest.org/en/latest/)
To run them use the command pytest.
```
pytest
```
Example of output 
```
============================= test session starts =============================
platform win32 -- Python 3.6.4, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
rootdir: C:\Users\Arty\fast-food, inifile: pytest.ini
plugins: cov-2.5.1
collected 10 items

tests\test_order.py ....                                                 [ 40%]
tests\test_validations.py ......                                         [100%]

========================== 10 passed in 0.25 seconds ==========================
```
## Built With

* `FLask` : [Flask](http://flask.pocoo.org/) is a micro web framework written in Python.

## Authors

* **Nangai Arthur** - [Linkedin](www.linkedin.com/in/arthur-nangai)
