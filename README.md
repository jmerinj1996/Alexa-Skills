# Alexa-Skills
Building Alexa skills using Python's Flask-Ask

This project is following an awesome 3-part series Sentdex tutorial series by Harrison Kinsley and also because I happen to be having an Amazon echo at home!

Flask-Ask is a Flask extension that makes building Alexa skills for the Amazon Echo easier and much more fun.

### Installation
The installation is as simple as typing the following in your terminal:
#### pip install flask
(if you don't already have flask)
#### pip install flask-ask
Also, since we're going to be using unidecode
#### pip install unidecode

### Deployment 
For deployment you would either require a http enabled server or ngrok

##### What is ngrok?
Amazon has no way to access your skill if you are running on the localhost.
Ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels.
Run ngrok over http on port 5000 

You need to create an Amazon Developer Account and don't sweat if you don't have an Amazon echo at home because Amazon provides you with an Alexa simulator.
