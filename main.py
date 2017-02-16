from display import *
from draw import *
import random

screen = new_screen()
powderblue = [ 176, 224, 230 ]
deepskyblue = [ 0, 191, 255 ]
royalblue = [ 65, 105, 225 ]

lines = 200

while lines > 0:
    draw_line(random.randint(0,500), random.randint(0,500), 255, 255, screen, powderblue)
    draw_line(random.randint(0,500), random.randint(0,500), 255, 255, screen, deepskyblue)
    draw_line(random.randint(0,500), random.randint(0,500), 255, 255, screen, royalblue)
    lines = lines - 1

while lines < 200:
    draw_line(255, 255, random.randint(0,500), random.randint(0,500), screen, powderblue)
    draw_line(255, 255, random.randint(0,500), random.randint(0,500), screen, deepskyblue)
    draw_line(255, 255, random.randint(0,500), random.randint(0,500), screen, royalblue)
    lines = lines + 1

'''
TESTING
XRES = 500
YRES = 500
color = powderblue
1 & 5
draw_line(0, 0, XRES-1, YRES-1, screen, color)
draw_line(0, 0, XRES-1, YRES/2, screen, color)
draw_line(XRES-1, YRES-1, 0, YRES/2, screen, color)
4 & 8
draw_line(0, YRES-1, XRES-1, 0, screen, color)
draw_line(0, YRES-1, XRES-1, YRES/2, screen, color)
draw_line(XRES-1, 0, 0, YRES/2, screen, color)
2 & 6
draw_line(0, 0, XRES/2, YRES-1, screen, color)
draw_line(XRES-1, YRES-1, XRES/2, 0, screen, color)
3 & 7
draw_line(0, YRES-1, XRES/2, 0, screen, color)
draw_line(XRES-1, 0, XRES/2, YRES-1, screen, color)
H & V
draw_line(0, YRES/2, XRES-1, YRES/2, screen, color)
draw_line(XRES/2, 0, XRES/2, YRES-1, screen, color)
'''

display(screen)

save_extension(screen, 'pic.png')
