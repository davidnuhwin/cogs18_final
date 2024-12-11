import pytest
from app import app, get_random_room, dorm_suite, quiz_question
# Most of the structure of these tests are new to me and sourced by https://flask.palletsprojects.com/en/stable/testing/
# This is external but the other tests below I have written
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_random_room():
    assert get_random_room() in dorm_suite

def test_quiz_logic():
    assert "Living" == quiz_question["answer"]
    assert "Kitchen" != quiz_question["answer"]

# Client is provided by pytest as if it were a Flask app
def test_chat_route(client):
    # Test a random keyword
    response_random = client.post("/chat", data={"message": "random"})
    # 'Any' checks if at least one condition in list is true.
    # The decode basically decodes the response data into a string and the rest of the code checks if the room's information is in the response data
    # It takes information from the dorm_suite list
    assert any(room["area"] in response_random.data.decode() or room["description"] in response_random.data.decode() for room in dorm_suite)

    # Test a specific room
    response_kitchen = client.post("/chat", data={"message": "Kitchen"})
    assert "Kitchen" in response_kitchen.data.decode()

