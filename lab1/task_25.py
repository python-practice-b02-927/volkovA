#!/usr/bin/python3

from pyrob.api import *

def cross():
    move_right(1)
    for i in range(3):
        move_down()
        fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up(2)


@task
def task_2_2():
    for i in range (4):
        cross()
        move_right(4)
    cross()
    move_down()


if __name__ == '__main__':
    run_tasks()
