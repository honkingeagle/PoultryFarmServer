from setuptools import setup

setup(
    name='poultryfarmserver',
    version='1.0.0',
    author='Tiras Mwangi',
    author_email='tmwangi599@gmail.com',
    packages=['poultryfarmserver'],
    install_requires=['flask', 'flask_sqlalchemy', 'flask_marshmallow']
)