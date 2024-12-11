# Source: https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Nested dictionary within a list 
dorm_suite = [
    {
        "area": "Kitchen",
        "description": (
            "A little messy but every college envies it. A personal stove, fridge, "
            "and an island! The boys whip up fantastic dishes that you'll love to try"
        ),
        "objects": "Peter's T2GO Boxes, Kai's Eggos and Nutella, Cento's Pasta"
    },
    {
        "area": "Living",
        "description": "Where the squad has deep talks and Netflix binges.",
        "objects": "Adriel's 'decorative' pile of laundry, Oby on the couch watching Brooklyn 99"
    },
    {
        "area": "Sinks",
        "description": "Where the squad washes their hands and gets ready.",
        "objects": "Toothbrushes Galore"
    },
    {
        "area": "Room2",
        "description": "David and Jonas' Domain",
        "objects": "David's Girlfriend Flag vs. Jonas Girlfriend Flag, Undone Messy Beds, and LED Lights"
    }
]

# Dictionary for quiz 
quiz_question = {
    "question": "Which room is known for Netflix binges and deep talks?",
    "options": ["Kitchen", "Living", "Sinks", "Room2"],
    "answer": "Living"
}

# utilizes flask in order to route user to the about page
@app.route("/about")
def about():
    return render_template('about.html')

# utilizes flask in order to route user to the home page
@app.route("/")
@app.route("/home")
# the dorm_suite=dorm_suite passes data from the Flask backend to the template being rendered
# we use this syntax over and over each time we pass data from here onto the html templates
def home():
    return render_template('index.html', dorm_suite=dorm_suite)

# method to get a random room
def get_random_room():
    return random.choice(dorm_suite)

# utilizes flask in order to route user to the quiz page
@app.route("/quiz", methods=["GET", "POST"])
# method to quiz user 
def quiz():
    # post means to send data (learned this while doing project)
    if request.method == "POST":
        # what the user inputs changes the value of "answer" to that input
        # request.form stores the form data submitted by a post request
        user_answer = request.form["answer"]  
        # correct can either evalute true or false
        correct = user_answer == quiz_question["answer"]  
        return render_template("quiz_result.html", correct=correct, answer=quiz_question["answer"])

    return render_template("quiz.html", question=quiz_question)

# utilizes flask in order to route user to the chat page
@app.route("/chat", methods=['POST'])
def chat():
    # lowercases user input to avoid user error
    user_input = request.form['message'].lower() 
    if 'random' in user_input:
        # calls method created earlier
        random_room = get_random_room()
        return render_template('random.html', room=random_room)
    if 'about' in user_input:
        return render_template('about.html', dorm_suite=dorm_suite)
    for room in dorm_suite:
        room_area = room['area'].lower()
        if room_area in user_input:
            area_name = room_area + ".html"
            return render_template(area_name, dorm_suite=dorm_suite)  

    return render_template('error.html', dorm_suite=dorm_suite)

# for flask to always be in debug mode
if __name__ == '__main__':
    app.run(debug=True)
