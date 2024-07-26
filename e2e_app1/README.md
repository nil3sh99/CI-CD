This is an example of a complete Python application, covering all the steps from version control to deployment, including creating a Docker image for distribution.

Write a simple hello world code for a flask app.

Code -> app.py

Create a requirements.txt file, and write the depdency in it.

Create a virtual env, by running

`python3 -m venv venv_app1`

activate the venv by running: 

`source venv_app1/bin/activate`

`pip install -r requirements.txt`

Freeze the requirements by running: 

`pip freeze > requirements.txt`

Create a `setup.py` file for packaging.

# setup.py

from setuptools import setup

setup(

    name='flask-web-app',

    version='1.0',

    packages=['app'],

    include_package_data=True,

    install_requires=[

    'Flask',

    ],

)

For distribution, create a Dockerfile, code added under the Dockerfile.


Build the docker image: 

`docker build -t flask-web-app:latest .`


##### Summary

* **Build** : Set up a virtual environment and install dependencies.
* **Packaging** : Create a `setup.py` file for packaging.
* **Distribution** : Create a Docker image and push it to Docker Hub.
