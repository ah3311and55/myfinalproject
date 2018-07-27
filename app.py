from flask import Flask, render_template, request, redirect, url_for, session
import dataset, random, os

app = Flask(__name__)
app.secret_key = os.urandom(24)
db = dataset.connect('postgres://pcpqiiqtxfhuor:c42f976e9ba808eb5a122108768095ba8c0d8fd8d9c9ea3e3e1212aa840c77f6@ec2-50-19-86-139.compute-1.amazonaws.com:5432/ddjpbk8t7a4qav')
# TODO: set up database
app.debug = True

@app.route('/')
def default():
	return render_template('home.html')

@app.route('/home')
def homepage():
	return render_template('home.html')

@app.route('/login')
def go_to_login():
	return render_template('login.html')

# @app.route("/formExample", methods=['POST'])
@app.route("/login", methods=['POST', 'GET'])
def login_page1():
   accounts=db["accounts"]
   username=request.form['userName']
   password=request.form['password']
   user = accounts.find_one(userName=username,password=password)
   # global show_data
   # if username=="1":
   #     show_data = True
   # else:
   #     show_data =False
   if user:
       session['loggedIn']=True
       session['formsVoted'] = []
       return render_template("form.html")
   else:
       return render_template("login.html",error="The password or username is incorrect")

@app.route("/register")
def register3():
    return render_template('register.html')
# TODO: route to /register
@app.route("/newAccount",methods=['POST', 'GET'])
def register2():
    accounts= db["accounts"]
    potential_username=request.form['userName']
    potential_password=request.form['password']
    username_exists=accounts.find_one(userName=potential_username)
    if username_exists:
        return render_template("register.html", error="username is already taken")
    else :
        accounts.insert(dict(userName=potential_username,password=potential_password))
        return render_template("login.html")
# @app.route("/form", methods=['POST','GET'])
# def go_to_form():
# 	firstName = request.form['firstname']
# 	lastName = request.form['lastname']
# 	gender = request.form['gender']
# 	return render_template('form.html', firstName = firstName, lastName=lastName, gender=gender)
@app.route('/Dailyvote',methods=['POST', 'GET'])	
def go_to_Dailyvote():
	votes=db['votes']

	return render_template('Dailyvote.html')
@app.route('/Fridayvote')
def go_to_Weeklyvote():
	return render_template('Fridayvote.html')	
@app.route('/Veganvote')
def go_to_Veganvote():
	return render_template('Veganvote.html')	
@app.route('/CreateMessage')	
def go_to_Suggestions():
	# message = request.form['message']
	return render_template('SuggestionsPage.html')
@app.route('/form')
def go_back():
	return render_template('form.html')

@app.route("/submitvote", methods=['POST'])
def votes():
	form_id = request.form['form_id']
	if form_id in session['formsVoted']:
		return render_template('Dailyvote.html', message="You already voted for this option")
	else:
		foods = db['food_votes']
		foodname = request.form['vote']
		food_entry = foods.find_one(foodname=foodname)
		if food_entry:
			vote_count = food_entry['votes']
			foods.update(dict(foodname=foodname, votes=vote_count+1), ['foodname'])
		else:
			foods.insert(dict(foodname=foodname, votes=1))
		session['formsVoted'].append(form_id)
		session.modified = True
		return render_template('votes.html', foods=list(foods.all()))
@app.route("/accebtvote", methods=['POST'])
def votees():
	form_id = request.form['form_id']
	if form_id in session['formsVoted']:
		return render_template('Dailyvote.html', message="You already voted for this option")
	else:
		foods = db['food_votes']
		foodname = request.form['vote']
		food_entry = foods.find_one(foodname=foodname)
		if food_entry:
			vote_count = food_entry['votes']
			foods.update(dict(foodname=foodname, votes=vote_count+1), ['foodname'])
		else:
			foods.insert(dict(foodname=foodname, votes=1))
		session['formsVoted'].append(form_id)
		session.modified = True
		return render_template('votes.html', foods=list(foods.all()))
# TODO: route to /error

def init():
	if not db['food_votes'].exists:
		
		foods.insert(dict(foodname='Omelette', votes=0))
		foods.insert(dict(foodname='Falafel', votes=0))
		foods.insert(dict(foodname='Chicken and rice', votes=0))
		foods.insert(dict(foodname='pasta', votes=0))

if __name__ == "__main__":
	init()
	app.run(port=3000)













