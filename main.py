from hashlib import new
import turtle
import pandas as pd

# create screen object
screen = turtle.Screen()
screen.title('U.S. Map Quiz')
image_path = 'blank_states_img.gif'
screen.addshape(image_path)
turtle.shape(image_path)

# load DF
df = pd.read_csv('50_states.csv')
all_states = df.state.to_list()
guessed_states = []

# game loop
while len(guessed_states) < 50:
    answer_state = (screen.textinput(
        title=f'{len(guessed_states)}/50 States Correct', prompt='Please enter the name of a state:')).title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        state_data = df[df.state == answer_state]
        pen.goto(int(state_data.x), int(state_data.y))
        pen.write(state_data.state.item())
