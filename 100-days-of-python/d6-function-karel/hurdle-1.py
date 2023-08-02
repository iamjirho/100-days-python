def jump():
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()
    
for i in range(6):
    move()
    jump()
    turn_right()
    turn_right()
    turn_left()