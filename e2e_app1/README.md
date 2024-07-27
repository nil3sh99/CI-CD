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

Option 1: Using docker and venv

* **Build** : Set up a virtual environment and install dependencies.
* **Packaging** : Create a `setup.py` file for packaging.
* **Distribution** : Create a Docker image and push it to Docker Hub.

Option 2: 

Using teamcity tool for all the ci cd operations: 

Create a New Project in TeamCity

Log in to your TeamCity server.

Click on Projects and then Create project.

Follow the wizard to link your version control repository (e.g., GitHub).

Create a Build Configuration

Under your project, create a new build configuration.

Name it Build and Deploy.

Add Build Steps



Build Step 1: Install Dependencies

Runner Type: Command Line

Step Name: Install Dependencies

Script:

sh

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

Build Step 2: Package Application

Runner Type: Command Line

Step Name: Package Application

Script:

sh

python setup.py sdist

Build Step 3: Build Docker Image

Runner Type: Command Line

Step Name: Build Docker Image

Script:

sh

docker build -t your-dockerhub-username/flask-web-app:latest .

Build Step 4: Push Docker Image

Runner Type: Command Line

Step Name: Push Docker Image

Script:

sh

docker login -u %dockerhub_username% -p %dockerhub_password%

docker push your-dockerhub-username/flask-web-app:latest

Add Environment Variables



Click on Parameters.

Add two new environment variables:

dockerhub_username: Your Docker Hub username.

dockerhub_password: Your Docker Hub password.
