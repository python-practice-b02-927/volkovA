#!/usr/bin/python3

from pyrob.api import *



@task
def task_8_22():
    while True:
        if wall_is_above():
            break
        move_up()
    if wall_is_on_the_left():
        while True:
            if wall_is_on_the_right():
                break
            move_right()
    else:
        while True:
            if wall_is_on_the_left():
                break
            move_left()


if __name__ == '__main__':
    run_tasks()
