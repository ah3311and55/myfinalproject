from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('thisWontWork.html')

if __name__ == "__main__":
    app.run()
