#!/usr/bin/python3

from pyrob.api import *

 
@task
def task_5_10():


    while True:
        while True:
            fill_cell()
            if wall_is_on_the_right():
                break
            move_right()
        while not wall_is_on_the_left():
            move_left()
        if wall_is_beneath():
            break
        move_down()
    
    
if __name__ == '__main__':
    run_tasks()
