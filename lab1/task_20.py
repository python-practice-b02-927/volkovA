#!/usr/bin/python3

from pyrob.api import * 
 
def count_w():
    i =0 
    while not wall_is_on_the_right():
        move_right()
        i += 1
    return i-1

def count_h():
    i = 0
    while not wall_is_beneath():
        move_down()
        i += 1
    return i-1
    
 
@task(delay=0.05)
def task_4_3():
    pass

    width = count_w()
    height = count_h()
     
    move_up()
    move_left()
    
    for j in range (width):
        for i in range (height):
            move_up()
            fill_cell()
        move_left()
        move_down(height)
    move_right()
 
if __name__ == '__main__':
    run_tasks()
