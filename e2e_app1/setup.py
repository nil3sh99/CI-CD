# setup.py
from setuptools import setup

setup(
    name='flask-web-app',
    version='1.0',
    packages=['e2e_app1'],
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
)
