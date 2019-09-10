#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
        move_down()
    i = 0
    while True:
        move_right()
        i +=1
        if not wall_is_beneath():
            break
    move_down()            
    move_left(i)


if __name__ == '__main__':
    run_tasks()
