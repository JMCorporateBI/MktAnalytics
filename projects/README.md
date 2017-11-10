# Projects repository

## Organization

All Python projects should follow a similar organization structure. Here we've included an project example with the following structure organization.

* **run.py**	This is the file that is invoked to start up a development server. It should get a copy of the app from your package and run it. This won’t be used in production, but it will see a lot of mileage in development.
* **requirements.txt**	This file lists all of the Python packages that your app depends on. You may have separate files for production and development dependencies.
* **config.py**	This file contains most of the configuration variables that your app needs.
* **/app/**	This is the package that contains your application.
* **/app/__init__.py**	This file initializes your application and brings together all of the various components.
* **/app/partials/** Folder with code parts to be reused in many parts of the project, but that are unique to your project. Reusable code across several projects are to be stored in the 'helpers' folder
* **/app/static/**	This directory contains the static files, like images and pdfs, that you want to make public via your app
* **/app/tests/** Tests files should be stored in here
