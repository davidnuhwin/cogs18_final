#Source: https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask, render_template, request
app = Flask(__name__)


dorm_suite = [
    {
        "area": "Kitchen",
        "description": "We be cooking.",
        "objects": "Peter's T2GO Boxes and Kai's Socks"
    },
    {
        "area": "Living",
        "description": "Where the squad gathers for deep talks and Netflix binges.",
        "objects": "Ryan's broken controller and Adriel's 'decorative' pile of laundry"
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', dorm_suite=dorm_suite)

@app.route("/chat", methods=['POST'])
def chat():
    user_input = request.form['message'].lower() #Receiving an inputted mesage
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

@app.route("/kitchen")
def kitchen():
    return render_template('kitchen.html')

@app.route('/living')
def living():
    return render_template('living.html')


if __name__ == '__main__':
    app.run(debug=True)  
