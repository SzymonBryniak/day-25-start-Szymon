import os
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = []
print(os.getcwd())


USA = pandas.read_csv("50_states.csv")
print(USA)

state_no = 0


def put_state(answer):
    global state_no
    state_no += 1
    row = USA[USA.state == answer]
    print(row["x"])
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.setpos(x=int(row['x']), y=int(row['y']))
    text.write(answer)
    states.append(text)
    return


while True:

    answer_state = screen.textinput(title=f"{state_no}/50Guess the State", prompt="What's another state's name?")

    # check_state(answer_state)
    if USA.state.isin([answer_state]).any().any():
        put_state(answer_state)
    elif answer_state is None:
        print('Game Over')
        break

