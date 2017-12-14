from flask import Flask, redirect, url_for, request, render_template, session, send_from_directory, flash, escape, g, abort
from flask_mail import Mail, Message
from jinja2 import Template

import CommuHub_Forms as customForms
import Time_Functions as timeFunctions

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("cred/commuhub-2017-firebase-adminsdk-mf4l3-5449d3e484.json")
default_app = firebase_admin.initialize_app(cred, {
    "databaseURL": 'https://commuhub-2017.firebaseio.com/'
})

root = db.reference()

# Required line, __name__ contains all the Flask module names(?)
app = Flask(__name__)

# Might need later
# app.config.from_object()

# Ahmad's config update - Currently used for email(?)
app.config.update(
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT= 465,
	MAIL_USE_SSL= True,
	MAIL_USERNAME = 'jonsnow3050@gmail.com',
	MAIL_PASSWORD = 'jonsnowisdead',
    MAIL_DEFAULT_SENDER = 'jonsnow3050@gmail.com'
)

# The route for URL navigation to all pages
@app.route('/')
@app.route('/<path:page>')
def show_page(page=None):
    # print(page)  To test for page
    if page == "CommuHub_Home" or not page:  # Just the base host URL (no page value set) or homepage
        return render_template("CommuHub_Home.html", returnDate=timeFunctions.returnCurrentDate())
    elif page != "favicon.ico":  # Called with a argument for page, that's not homepage
        return render_template("{}.html".format(page))
    else:  # For favicon request
        return page

mail = Mail(app)
@app.route('/feedback', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = Message(subject="Feedback",
                      recipients=['jonsnow3050@gmail.com'])
        msg.html = 'From: {} ({}) <br> <br> Subject: {} <br> <br> Message: {}'.format(request.form['name'],
                                                                                      request.form['email'],
                                                                                      request.form['subject'],
                                                                                      request.form['message'])
        mail.send(msg)
        return render_template('index.html')

    return render_template('index.html')

# Note using URL strings as arguments and "returned" strings are parsed as HTML
@app.route("/hello/<username>/")
def hello_user(username):
    return "<h1>Hello {}<h1>".format(username)

# End code to execute
if __name__ == '__main__':
    app.secret_key = "e7AdCq7iwNN0RO9YixqraD6l4TuiwCyZh0yd9Yfp"
    app.run()
    # app.run(debug=True)  optimisation?
