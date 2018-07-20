from flask import Flask, render_template
import random, datetime
quote= ["<h1>Live more Worry less</h1>","<h1>Don't dream for success work for it</h1>","<h1>Beauty is a power a smile is its sword</h1>","<h1>When it rains look for rainbow</h1>","<h1>Good vibes only</h1>"]

app = Flask(__name__)
@app.route("/rnd")
def randomq():
    rand_item = quote[random.randrange(len(quote))]
    return (rand_item)
@app.route("/")
def hi():
    return "Mywep2"

@app.route("/mypage")
def loadpage():		
	date =str(datetime.datetime.today())
	nums=[0,1,2,3,4]
	return render_template("mypage.html",numberArray=nums)


@app.route('/<page_name>')
def go_to_page(page_name):
    return render_template(page_name+".html")
    
if __name__ == "__main__":
    app.run()