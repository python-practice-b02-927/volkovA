#!/usr/bin/python3

from pyrob.api import *

def count_w():
    i = 0
    while not wall_is_on_the_left():
        move_left()
        i += 1
    return i



def find_exit(width):
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_right():
        if not wall_is_beneath():
            move_down()
            return 1
        move_right()
        
    for j in range (width):
        if not wall_is_beneath():
            move_down()
            return 1
        move_left()
    return 0


@task(delay=0.01)
def task_8_30():
    
    width = count_w()
    while find_exit(width) == 1:
        pass
 


if __name__ == '__main__':
    run_tasks()
