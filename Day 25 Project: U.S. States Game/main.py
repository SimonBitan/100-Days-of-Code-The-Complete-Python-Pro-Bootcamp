import turtle
import pandas

# Font and alignment for the text that will write the state names.
FONT = ("Arial", 8, "normal")
ALIGNMENT = "center"

# Reading data using Pandas.
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
data_dict = data.to_dict()
print(data_dict)

# Screen turtle.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Writing turtle.
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Loop to continue guessing.
correct_guesses = []
while len(correct_guesses) != 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in correct_guesses:
        continue
    elif answer_state == "Exit":
        states_missed = []
        for state in state_list:
            if state not in correct_guesses:
                states_missed.append(state)
        states_missed_dataframe = pandas.DataFrame(states_missed)
        states_missed_dataframe.to_csv("states_to_learn.csv")
        break
    elif answer_state in state_list:
        selected_row = data[data["state"] == answer_state]
        writer.goto(int(selected_row.x), int(selected_row.y))
        writer.write(f"{answer_state}", False, ALIGNMENT, FONT)
        correct_guesses.append(answer_state)








screen.exitonclick()
