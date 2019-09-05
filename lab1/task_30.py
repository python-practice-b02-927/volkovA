#!/usr/bin/python3

from pyrob.api import *

def count():
    i = 0
    while not wall_is_on_the_right():
        move_right()
        i += 1
    return i

@task(delay=0.02)
def task_9_3():
    size = count()
    for j in range(size+1):
        for k in range(size+1):
 
            if not (k==j or k == size - j):
                fill_cell()
            if not k == size:
                move_left()
        if not j == size:
            move_right(size)
            move_down()

if __name__ == '__main__':
    run_tasks()
