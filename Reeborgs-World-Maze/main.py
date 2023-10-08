def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# The problem is that whenever the robot is in a starting
# position without a wall on it's right side, it will
# end up in an infinite loop. To solve this problem
# we have to just make sure that there is a wall on the right
# side of the robot.

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()