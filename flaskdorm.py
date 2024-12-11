#Source: https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask, render_template, request
import random 

app = Flask(__name__)


dorm_suite = [
    {
        "area": "Kitchen",
        "description": "A little messy but every college envies it. A personal stove, fridge, and an island! The boys whip up fantastic dishes that you'll love to try",
        "objects": "Peter's T2GO Boxes, Kai's Eggos and Nutella, Cento's Pasta"
    },
    {
        "area": "Living",
        "description": "Where the squad has deep talks and Netflix binges.",
        "objects": "Adriel's 'decorative' pile of laundry, Oby on the couch watching Lucifer, "
    },
    {
        "area": "Sinks",
        "description": "Where the squad washes their hands and gets ready.",
        "objects": "Toothbrushes Galore"
    },
    {
        "area": "Room2",
        "description": "David and Jonas' Domain",
        "objects": "David's Girlfriend Flag vs. Chaewon Flag, Undone Messy Beds, and LED Lights"
    }

]

quiz_question = {
    "question": "Which room is known for Netflix binges and deep talks?",
    "options": ["Kitchen", "Living", "Sinks", "Room2"],
    "answer": "Living"
}


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', dorm_suite=dorm_suite)

def get_random_room():
    return random.choice(dorm_suite)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answer = request.form["answer"]  # Get the user's answer
        correct = user_answer == quiz_question["answer"]  # Check if correct
        return render_template("quiz_result.html", correct=correct, answer=quiz_question["answer"])

    return render_template("quiz.html", question=quiz_question)


@app.route("/chat", methods=['POST'])
def chat():
    user_input = request.form['message'].lower() #Receiving an inputted mesage
    if 'random' in user_input:
        #calls method
        random_room = get_random_room()
        return render_template('random.html', room=random_room)
    if 'about' in user_input:
        return render_template('about.html', dorm_suite=dorm_suite)
    for room in dorm_suite:
        room_area = room['area'].lower()
        if room_area in user_input:
            area_name = room_area + ".html"
            return render_template(area_name, dorm_suite=dorm_suite)  # Pass the matched room data to the template

    # If no room matched, return chat.html
    return render_template('error.html', dorm_suite=dorm_suite)


@app.route("/about")
def about():
    return render_template('about.html')


#for flask to always be in debug mode
if __name__ == '__main__':
    app.run(debug=True)  
