# Movie Web Application

## Description

A Web application that makes use of Flask configuration, Jinja templating, WTForms and blueprints. 

## Installation

**Installation via requirements.txt**

```shell
$ cd COMPSCI235_A2_ston253
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:COMPSCI235_A2_ston253' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Configuration

The COMPSCI235_A2_ston253/.env file contains variable settings. They are set with appropriate values.

FLASK_APP: Entry point of the application (should always be wsgi.py).
FLASK_ENV: The environment in which to run the application (either development or production).
SECRET_KEY: Secret key used to encrypt session data.
TESTING: Set to False for running the application. Overridden and set to True automatically when testing the application.
WTF_CSRF_SECRET_KEY: Secret key used by the WTForm library.

## Execution

**Running the application**

From the *COMPSCI235_A2_ston253* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 

The homepage can be accessed from a Web browser:

http://127.0.0.1:5000/
