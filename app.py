from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# TODO: set up database



@app.route('/home')
def homepage():
	return render_template('home.html')

@app.route('/register')
def go_to_register():
	return render_template('register.html')
@app.route("/formExample", methods=['POST'])
	
@app.route("/form", methods=['POST'])
def go_to_form():
	firstName = request.form['firstname']
	lastName = request.form['lastname']
	gender = request.form['gender']
	return render_template('form.html', firstName = firstName, lastName=lastName, gender=gender)
@app.route('/Dailyvote')	
def go_to_Dailyvote():
	return render_template('Dailyvote.html')
# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











