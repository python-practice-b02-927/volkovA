#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if not wall_is_above():
	    move_up(1)
    elif not wall_is_beneath():
	    move_down(1)
    elif not wall_is_on_the_left() :
	    move_left(1)
    else: 
	    move_right(1)

 


if __name__ == '__main__':
    run_tasks()
