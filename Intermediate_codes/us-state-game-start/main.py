import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_name = state_data["state"].to_list()


new_state = turtle.Turtle()
correct_data = []

while len(correct_data) < 50:
    answer_start = turtle.textinput(title="Guess the state ",
                                    prompt=f"What's another state name? score: {len(correct_data)}/50")
    user_guess = answer_start.title()

    if user_guess == "Exit":
        # learn_state = []
        # for state in state_name:
        #     if state not in correct_data:
        #         learn_state.append(state)
        #
        # state_to_learn = {
        #     "states": learn_state,
        # }

        # using list comprehension
        missing_state = [state for state in state_name if state not in correct_data]
        df = pandas.DataFrame(missing_state)
        df.to_csv("state_to_learn2.csv")
        # missing_state = [state for state in state_name if state in correct_data]
        break

    if user_guess in state_name:
        state_row = state_data[state_data.state == user_guess]
        x = state_row.x
        y = state_row.y
        new_state.penup()
        new_state.goto(int(x), int(y))
        new_state.write(user_guess)
        correct_data.append(user_guess)

