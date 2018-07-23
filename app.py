from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# TODO: set up database



@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/register')
def go_to_register():
	return render_template('register.html')

# TODO: route to /register

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











