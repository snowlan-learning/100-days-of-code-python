def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


########################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()



while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

########################################################


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()  
    else:
        turn_left()
        




