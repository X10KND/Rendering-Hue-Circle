from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import colorsys

WIDTH = 500
HEIGHT = 500
RADIUS = 200
'''
RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.4, 1.0)

def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
'''

def draw_rgb_points(x, y, c):
    glColor3f(c[0], c[1], c[2])
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

'''
def drawLine(x0, y0, x1, y1):

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    if dy >= 0:
        sign = 1
    else:
        sign = -1

    if abs(dx) >= abs(dy):
        d = 2 * dy - dx
        x, y = x0, y0
        draw_points(x, y)

        while x < x1:
            if d * sign > 0:
                d -= 2 * abs(dx) * sign
                y += 1 * sign

            x += 1
            d += 2 * abs(dy) * sign

            draw_points(x, y)

    else:
        d = 2 * dx - dy

        if y0 > y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        x, y = x0, y0
        draw_points(x, y)

        while y < y1:
            if d * sign > 0:
                d -= 2 * abs(dy) * sign
                x += 1 * sign

            y += 1
            d += 2 * abs(dx) * sign

            draw_points(x, y)


def draw_rgb(v0, c0, v1, c1, v2, c2):
    vs1 = (v1[0] - v0[0], v1[1] - v0[1])
    vs2 = (v2[0] - v0[0], v2[1] - v0[1])

    r1 = (vs1[0] * vs2[1] - vs1[1] * vs2[0])
    r2 = (vs1[0] * vs2[1] - vs1[1] * vs2[0])

    minX = int(min(v0[0], v1[0], v2[0]))
    maxX = int(max(v0[0], v1[0], v2[0]))

    minY = int(min(v0[1], v1[1], v2[1]))
    maxY = int(max(v0[1], v1[1], v2[1]))

    for x in range(minX, maxX + 1):
        for y in range(minY, maxY + 1):

            s = ((x - v0[0]) * vs2[1] - (y - v0[1]) * vs2[0]) / r1
            t = (vs1[0] * (y - v0[1]) - vs1[1] * (x - v0[0])) / r2

            if s >= 0 and t >= 0 and s + t <= 1:
                c = [0, 0, 0]
                for i in range(3):
                    c[i] = (1 - s - t) * c0[i] + s * c1[i] + t * c2[i]

                draw_rgb_points(x, y, c)


def CirclePoints(x, y, cx, cy):
    glPointSize(1)
    glBegin(GL_POINTS)

    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)
    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)
    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)

    glEnd()


def drawCircle(r, cx, cy):
    d = 1 - r
    x, y = 0, r

    while x < y:
        CirclePoints(x, y, cx, cy)
        if d >= 0:
            d += 2 - (2 * y)
            y = y - 1

        d += (2 * x) + 3
        x = x + 1
'''

def HueCirclePoints(x, y, cx, cy):
    glPointSize(1)
    glBegin(GL_POINTS)

    for i in range(-x, x + 1):
        d = ((i ** 2 + y ** 2) ** 0.5 / RADIUS) ** 0.75

        c = colorsys.hsv_to_rgb((math.atan2(y, i) / (2 * math.pi)) + 1.75, d, 1.0)
        glColor3f(c[0], c[1], c[2])
        glVertex2f(i + cx, y + cy)

        c = colorsys.hsv_to_rgb((math.atan2(-y, i) / (2 * math.pi)) + 1.75, d, 1.0)
        glColor3f(c[0], c[1], c[2])
        glVertex2f(i + cx, -y + cy)

    for i in range(-y, y + 1):
        d = ((i ** 2 + x ** 2) ** 0.5 / RADIUS) ** 0.75

        c = colorsys.hsv_to_rgb((math.atan2(x, i) / (2 * math.pi)) + 1.75, d, 1.0)
        glColor3f(c[0], c[1], c[2])
        glVertex2f(i + cx, x + cy)

        c = colorsys.hsv_to_rgb((math.atan2(-x, i) / (2 * math.pi)) + 1.75, d, 1.0)
        glColor3f(c[0], c[1], c[2])
        glVertex2f(i + cx, -x + cy)

    glEnd()


def drawSolidCircle(r, cx, cy):
    d = 1 - r
    x, y = 0, r

    while x < y:
        HueCirclePoints(x, y, cx, cy)
        if d >= 0:
            d += 2 - (2 * y)
            y = y - 1

        d += (2 * x) + 3
        x = x + 1


def iterate():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WIDTH, 0.0, HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    drawSolidCircle(RADIUS, WIDTH // 2, HEIGHT // 2)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Hue Circle")
glutDisplayFunc(showScreen)
glutMainLoop()
