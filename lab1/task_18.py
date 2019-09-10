#!/usr/bin/python3

from pyrob.api import *

def move_to_the_left_wall():
    while not wall_is_on_the_left():
        move_left()

def find_out():
 
    while True:
      
        if not wall_is_above():
            move_up()
            break
        move_right()
            

def move_to_corner():
    while True:
        if wall_is_above():
            break
        move_up()
    while True:
        if wall_is_on_the_left():
            break
        move_left()

@task
def task_8_28():
    move_to_the_left_wall()
    find_out()
    move_to_corner()


if __name__ == '__main__':
    run_tasks()
