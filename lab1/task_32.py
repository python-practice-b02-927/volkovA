#!/usr/bin/python3

from pyrob.api import *

def filling_cell():
    if not cell_is_filled():
        fill_cell()
        return 0
    else:
        return 1

def coloring():
    h = 0
    all_colored = 0
    if wall_is_above():
        all_colored += filling_cell()
    else:
        while not wall_is_above():
            move_up()
            h +=1
            all_colored += filling_cell()
        move_down(h)
    return all_colored


@task(delay=0.03)
def task_8_18():
    v = 0
    while True:
        if not wall_is_beneath():
            break
        v += coloring()
        move_right()
    mov('ax', v)   
        
 
if __name__ == '__main__':
    run_tasks()
