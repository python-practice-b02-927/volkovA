#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    if not (wall_is_above() and wall_is_beneath()):
        if wall_is_above() or wall_is_beneath():
            if not cell_is_filled():
                fill_cell()
    move_right()


if __name__ == '__main__':
    run_tasks()
