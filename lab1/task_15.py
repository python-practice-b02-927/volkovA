#!/usr/bin/python3

from pyrob.api import *


def move_horizontally():
    if wall_is_on_the_left():
        while True:
            move_right()
            if  wall_is_on_the_right():
                break

    else:
        while True:
            move_left()
            #print('move_left')
            if wall_is_on_the_left():
                #print('smth_in_the_left')
                break

    
def move_vertically():
    if wall_is_above():
        while True:
             move_down()
             if  wall_is_beneath():
                 break

    else:
        while True:
            move_up()
            if wall_is_above():
                break


@task
def task_8_21():
    move_horizontally()
    move_vertically()

if __name__ == '__main__':
    run_tasks()
