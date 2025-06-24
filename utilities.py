import game_data
import random

def get_personal_data():
    return random.choice(game_data.data)

def checking_choice(value):
    if value in ["A", "B"]:
        return True
    else:
        return False

def display_person(data, label):
    return f"{label}: {data['name']}, a {data['description']},from {data['country']}"

def check_answer(choice, follower_a, follower_b):
    if follower_a > follower_b:
        return choice == "A"
    else:
        return choice == "B"