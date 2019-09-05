#!/usr/bin/python3

from pyrob.api import *

def check_left():
    while not wall_is_on_the_left() and wall_is_above():
        move_left()
    if not wall_is_above():
        return 1

def check_right():
    while not wall_is_on_the_right() and wall_is_above():
        move_right()
    if not wall_is_above():
        return 1
         
         
def move_to_corner():
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()

@task
def task_8_29():
    
    if check_left() == 1:
        move_to_corner()
    elif check_right() == 1:
        move_to_corner()        
 
if __name__ == '__main__':
    run_tasks()
