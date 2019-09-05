#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_6_6():
    h = 0
    l = 0
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            h = 0
            while not wall_is_above():
                move_up()
                fill_cell()
                h += 1
            move_down(h)

        l += 1
    move_left(l)


if __name__ == '__main__':
    run_tasks()
