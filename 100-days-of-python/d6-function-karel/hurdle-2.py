def jump():
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()

while not at_goal():
    move()
    jump()
    turn_right()
    turn_right()
    turn_left()