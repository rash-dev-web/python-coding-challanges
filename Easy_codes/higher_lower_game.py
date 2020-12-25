# Display logo
from Easy_codes.art import higher_lower_logo, vs
from random import choice
from Easy_codes.game_data import data
from replit import clear

print(higher_lower_logo)


# Get two data from data file and show with VS logo
def get_data(datalist):
    random_data = choice(datalist)
    return random_data


# Ask user to enter A or B
def more_follower(frist_data, second_data, user_input):
    user_one_follower = int(frist_data["follower_count"])
    user_two_follower = int(second_data["follower_count"])
    # print(f"{user_one_follower} {user_two_follower} {user_input}")
    if user_one_follower > user_two_follower and user_input == 'a':
        return True
    elif user_two_follower > user_one_follower and user_input == 'b':
        return True
    else:
        return False


def show_data(first_data, second_data):
    print(f"Compare A: {first_data['name']}, {first_data['description']}, from {first_data['country']}")
    print(vs)
    print(f"Compare B: {second_data['name']}, {second_data['description']}, from {second_data['country']}")


# game
def higher_lower_game():
    data_a = get_data(data)
    data_b = get_data(data)
    if data_a == data_b:
        data_b = get_data(data)
    show_data(data_a, data_b)

    score = 0
    should_continue = True
    while should_continue:
        user_input = input("Who has more followers? Type 'A' or 'B':").lower()
        result = more_follower(data_a, data_b, user_input)
        print(result)
        if result == True:
            score += 1
            clear()
            print(higher_lower_logo)
            print(f"You're right! Current score: {score}.")

            data_a = data_b
            data_b = get_data(data)
            show_data(data_a, data_b)

        if result == False:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


higher_lower_game()