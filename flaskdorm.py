#Source: https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask, render_template
app = Flask(__name__)


dorm_suite = [
    {
        "area": "kitchen",
        "description": "We be cooking.",
        "objects": "Peter's T2GO Boxes and Kai's Socks"
    },
    {
        "area": "living room",
        "description": "Where the squad gathers for deep talks and Netflix binges.",
        "objects": "Ryan's broken controller and Adriel's 'decorative' pile of laundry"
    },

]



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', dorm_suite=dorm_suite)

@app.route("/about")
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)
