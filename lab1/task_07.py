#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath() == False:
        move_down()
    i = 0
    while True:
        move_right()
        i +=1
        if wall_is_beneath()==False:
            break
    move_down()            
    move_left(i)


if __name__ == '__main__':
    run_tasks()
