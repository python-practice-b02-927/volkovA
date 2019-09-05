#!/usr/bin/python3

from pyrob.api import *

def count():
    i = 0
    while not wall_is_beneath():
        move_down()
        i += 1
    return i-1

@task(delay=0.05)
def task_4_11():
    pass

    size = 0
    size = count()
    move_up(size + 1)
    move_right()
    move_down()
    i = 0
    for i in range (size):
        for a in range (i+1):
            fill_cell()
            move_right()
        move_left(i+1)
        move_down()
    
    
if __name__ == '__main__':
    run_tasks()
