#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_1():
    move_left(3)
    move_down(1)


if __name__ == '__main__':
    run_tasks()
