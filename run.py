from flask import Flask, request, redirect, session
import twilio.twiml
import os
from handler import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def receive_sms():
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    body = body.lower().strip()  # removes spaces and converts all to lower case

    a = session.get('a', 0)
    b = session.get('b', 0)
    c = session.get('c', 0)
    d = session.get('d', 0)

    message, a, b, c, d = response_handler(body, a, b, c, d)

    session['a'] = a
    session['b'] = b
    session['c'] = c
    session['d'] = d
 
    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.  For Heroku deployment
	# http://stackoverflow.com/questions/17260338/deploying-flask-with-heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)