from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    #OCTANTS 3-6 (SWITCH ENDPOINTS)
    if x0 > x1:
        temp = x0
        temp = y0
        x0 = x1
        y0 = y1
        x1 = temp
        y1 = temp

    #UNDEFINED SLOPE (VERTICAL LINE)
    if (x1 - x0) == 0:
        while y0 < y1:
            plot(screen, color, x0, y0)
            y0 += 1

    #YAS LEGGO
    else:
        slope = (float(y1) - float(y0))/(float(x1) - float(x0))
        A = y1 - y0
        B = -(x1 - x0)

        if slope >= 0 and slope < 1:
            octant1(x0, y0, x1, y1, screen, color, A, B)

        elif slope >= 1:
            octant2(x0, y0, x1, y1, screen, color, A, B)

        elif slope <= -1:
            octant7(x0, y0, x1, y1, screen, color, A, B)

        elif slope < 0 and slope > -1:
            octant8(x0, y0, x1, y1, screen, color, A, B)

        else:
            print "Y R U TRYING TO DRAW IMPOSSIBLE LINES HUH"

def octant1(x0, y0, x1, y1, screen, color, A, B):
    d = 2*A + B
    while x0 <= x1:
        plot(screen, color, x0, y0)
        if d > 0:
            y0 += 1
            d += 2*B
        x0 += 1
        d += 2*A

def octant2(x0, y0, x1, y1, screen, color, A, B):
    d = A + 2*B
    while y0 < y1:
        plot(screen, color, x0, y0)
        if d < 0:
            x0 += 1
            d += 2*A
        y0 += 1
        d += 2*B

def octant7(x0, y0, x1, y1, screen, color, A, B):
    d = A - 2*B
    while y0 > y1:
        plot(screen, color, x0, y0)
        if d > 0:
            x0 += 1
            d += 2*A
        y0 -= 1
        d -= 2*B

def octant8(x0, y0, x1, y1, screen, color, A, B):
    d = 2*A - B
    while x0 < x1:
        plot(screen, color, x0, y0)
        if d < 0:
            y0 -= 1
            d -= 2*B
        x0 += 1
        d += 2*A
