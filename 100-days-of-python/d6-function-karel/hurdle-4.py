def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    while wall_on_right():
        move()
    turn_right()
    move()
          
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_left()
            jump()
