from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

def get_quotes_from_reddit():
    authentication_dict = {'user': 'YOUR_USERNAME','passwd': 'YOUR_PASSWORD','api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'I am testing Alexa: Jeffy'})
    sess.post('https://www.reddit.com/api/login', data = authentication_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/quotes/.json?limit=3'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '... '.join([i for i in titles])
    return titles

@app.route('/')
def homepage():
    return "Hi there, how ya doin?"

@ask.launch
def invoke_skill():
    start_message = 'Hey Jeffy, would you like to kick start your day with some inspiring quotes?'
    return question(start_message)

@ask.intent("YesIntent")
def share_quotes():
    quotes = get_quotes_from_reddit()
    quotes_msg = 'Ok... get ready for some awesome quotes from some awesome people... well, some of them{}'.format(quotes)
    return statement(quotes_msg)

@ask.intent("NoIntent")
def no_intent():
    end_message = 'Ok... just let me know when you feel like hearing them... bye'
    return statement(end_message)

if __name__ == '__main__':
    app.run(debug=True)
