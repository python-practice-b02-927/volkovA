#!/usr/bin/python3

from pyrob.api import *

def cross():
    move_right(1)
    fill_cell()
    for i in range(2):
        move_down()
        fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up(1)


@task(delay=0.02)
def task_2_4():
    for j in range(5):
        for i in range(9):
            cross()
            move_right(4)
        cross()
        move_left(36)
        if j != 4:
            move_down(4)

if __name__ == '__main__':
    run_tasks()
