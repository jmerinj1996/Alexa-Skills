
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







## Alexa reads encouraging quotes from reddit
Since Flask-ask is an extension of Flask, the code will look very similar to Flask.

For this code to work, you would need to create a reddit account.
In the code where it says YOUR_USERNAME and YOUR_PASSWORD, you are required to fill in your username and password


Now, you can ask your Alexa device: "Alexa, start Reddit Reader." You will be asked if you want to hear some quotes to which you can either respond "yes" or "no." If you say "yes" you will get the quotes and then the skill will end. If you respond "no," then the skill will end.
