
# django-todo

A brief & easy description about the project and it's for Beginner's to get the very basic idea about Django.


## About the Project
This project is a web application built using Python and Django, demonstrating the fundamental CRUD,

  C- Create

  R- Read

  U- Update
  
  D- Delete         

 operations for managing a list.

 The application provides a simple and intuitive interface for users to add, view, edit, and delete items from a list, 
 showcasing Django's powerful and flexible capabilities for building dynamic web applications.
## Run my Project

Step 1: Run the following code on terminal

    python manage.py runserver

This command is used to start a development server for a Django project.

If you are using Visual Studio Code, then you can type this command on the terminal directly.

Step 2: The output of the command gives us the url

    http://127.0.0.1.8000/

Add /admin at last of the url & paste on your browser
    
    http://127.0.0.1.8000/admin

Step 3: Now the project is running on the browser, you will see the form Django Administration.

For admin login,

    username: admin
    password: admin

For user login,

    username:
    password:

Step 4: You've now access to the project.
## Lessons
* Run runserver in a virtual environment to isolate project dependencies.

* Use a unique port number (e.g., python manage.py runserver 8080) to avoid conflicts with other servers.

* Disable debug mode in production environments to prevent exposing sensitive information.

Description:

This Django web application is running with debug mode turned on (DEBUG = False ). One of the main features of debug mode is the display of detailed error pages. If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from settings.py).

Remediation:

Never deploy a site into production with DEBUG turned on. To disable debug mode, set DEBUG = False in your Django settings file.

References:
[Django debug mode](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-DEBUG)

Note: You can find settings.py on Todo folder.
## Troubleshooting
* Port already in use? Change the port number or stop other servers using the same port.

* Database migration errors? Run 

        python manage.py makemigrations

and

        python manage.py migrate 
    
to update changes.
## Create your own new Project

You can also create your new Project

Step 1: Install latest version of Python

[Download Latest Version Python](https://www.python.org/downloads/)

Step 2: Open the VS code terminal,

Run the command to create virtual environment

    virtualenv <env_name>

<env_name> is your virtual environment name.

Step 3: To activate the virtual environment

    .\<env_name>\Scripts\activate

Step 4: Check the versiom

    virtualenv- version

Step 5: Install Django

    pip install django

Step 6: Start Project

    django-admin startproject <project_name>

Step 7: Type the command

    django-admin

Again,

    .\<env_name>\Scripts\activate

Step 8: This command create a folder in your Project

    python manage.py startapp <folder_name>

Step 9:
Link app with Project

    project setting.py to <project_name>

Add in the code 

    INSTALLED_APPS = [
    # ...
    'base',
    # ...
    ]

    EXTERNAL_APPS = [
    # ...
    'base',
    # ...
    ]

Step 10:
Download the extension on VS code named

    Sqlite Viewer 

Step 11: Type on terminal,

    python manage.py makemigrations

and

    python manage.py migrate 
    
to update changes.

Step 12: On terminal,

    python manage.py runserver


Now your code is running on 

    http://127.0.0.1.8000/admin

## Documentation

[Django Documentation](https://docs.djangoproject.com/en/5.1/)

[Python Documentation](https://docs.python.org/3.12/)


## Authors

- [@PRAM1N](https://github.com/PRAM1N)

