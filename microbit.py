# Add your Python code here. E.g.
from microbit import *
import random

board_x=2
board_y=4
egg_x = 2
egg_y = 0
egg_interval = 100
egg_counter = 0

a_press_count=0
b_press_count=0
bg_x = -1
bg_delay = -1

def led_on( x, y, lv ):
    display.set_pixel( x, y, display.get_pixel( x, y ) | lv )


def led_off( x, y, lv ):
    display.set_pixel( x, y, display.get_pixel( x, y ) &~lv )


def background(x):
    global bg_x
    global bg_delay
    bg_x = x
    bg_delay = 30


def draw_background():
    global bg_delay

    if bg_x<0:
        return
    
    if bg_delay<0:
        return
    
    bg_delay=bg_delay-1
    
    if bg_delay>0:
        led_on( bg_x, 0, 1 )
        led_on( bg_x, 1, 1 )
        led_on( bg_x, 2, 1 )
        led_on( bg_x, 3, 1 )
        led_on( bg_x, 4, 1 )
    else:
        led_off( bg_x, 0, 1 )
        led_off( bg_x, 1, 1 )
        led_off( bg_x, 2, 1 )
        led_off( bg_x, 3, 1 )
        led_off( bg_x, 4, 1 )


def draw_board(x,y):
    li = display.get_pixel(x,y)
    led_on( x, y, 4 )


def move_board(x0,x1):
    if x1>=0 and x1<=4:
        led_off( x0, board_y, 4 )
        return x1
    return x0


def move_egg():
    global egg_interval
    global egg_counter
    global egg_y
    global egg_x
    egg_counter = egg_counter+1
    
    if egg_counter<egg_interval:
        return
    
    led_off( egg_x, egg_y, 2 )
    egg_counter=0
    egg_y = egg_y+1
    
    if egg_y<4:
        return
    
    if egg_x == board_x:
        background(egg_x)
        if egg_interval>17:
            egg_interval = egg_interval-7
    elif egg_interval<70:
        egg_interval = egg_interval+12
        
    egg_y = 0
    egg_x = random.choice([0,1,2,3,4])
    return


def draw_egg():
    led_on( egg_x, egg_y, 2 )


while True:
    
    if button_b.get_presses() > b_press_count :
        board_x = move_board(board_x, board_x+1)
        b_press_count = button_b.get_presses()

    if button_a.get_presses() > a_press_count:
        board_x = move_board(board_x, board_x-1)
        a_press_count = button_a.get_presses()
    
    move_egg()

    draw_board( board_x, board_y )
    draw_egg()
    draw_background()
    
    sleep(10)
    