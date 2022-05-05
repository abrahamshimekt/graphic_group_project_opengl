import math
import pygame  # import a pygame class
from OpenGL.GL import *  # from python opengl.gl module import all classes
from OpenGL.GLU import *  # from opengl.glu module import all classes
from pygame.locals import *  # from pygame.locals import all class

""" Init function initialize the pygame display window with width, height and colors
"""


def init():
    pygame.init()
    display = (900, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 100, 0, 100)


def draw_sky():
    """sky"""
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2d(0, 80)
    glVertex2d(100, 80)
    glVertex2d(100, 100)
    glVertex2d(0, 100)
    glEnd()


def draw_sun():
    """sun"""
    glColor3f(0.9601, 0.956, 0.502)
    glBegin(GL_POLYGON)
    for i in range(361):
        angle = 2 * math.pi * i / 360
        x = 20 + 3 * math.cos(angle)
        y = 85 + 3 * math.sin(angle)
        glVertex2d(x, y)
    glEnd()


def draw_fence():
    """fence"""
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex2d(0, 17)
    glVertex2d(2, 17)
    glVertex2d(2, 10)
    glVertex2d(0, 10)
    glEnd()

    """fence"""
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    a = 0
    for i in range(25):
        x = 2
        a += x
        glVertex2d(0 + a, 17)
        glVertex2d(2 + a, 17)
        glVertex2d(2 + a, 10)
        glVertex2d(0 + a, 10)

    glEnd()
    """fence"""
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    for i in range(21):
        x = 2
        a += x
        glVertex2d(10 + a, 17)
        glVertex2d(12 + a, 17)
        glVertex2d(12 + a, 10)
        glVertex2d(10 + a, 10)

    glEnd()


def draw_bushes():
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(58, 50)
    glVertex2d(64, 50)
    glVertex2d(61, 52)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(48, 55)
    glVertex2d(54, 55)
    glVertex2d(51, 57)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(43, 60)
    glVertex2d(49, 60)
    glVertex2d(46, 62)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(43, 10)
    glVertex2d(49, 10)
    glVertex2d(46, 12)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(40, 10)
    glVertex2d(46, 10)
    glVertex2d(43, 12)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(13, 10)
    glVertex2d(19, 10)
    glVertex2d(16, 12)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(10, 10)
    glVertex2d(16, 10)
    glVertex2d(13, 12)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(66, 10)
    glVertex2d(72, 10)
    glVertex2d(69, 12)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(69, 10)
    glVertex2d(75, 10)
    glVertex2d(72, 12)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(89, 10)
    glVertex2d(95, 10)
    glVertex2d(92, 12)
    glEnd()
    """bush"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(92, 10)
    glVertex2d(98, 10)
    glVertex2d(95, 12)
    glEnd()

def draw_flag():
    """green"""
    glColor3f(0.04, .93, 0.04)
    glBegin(GL_POLYGON)
    glVertex2d(15, 55)
    glVertex2d(25, 55)
    glVertex2d(25, 53)
    glVertex2d(15, 53)
    glEnd()
    """yellow"""
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2d(15, 53)
    glVertex2d(25, 53)
    glVertex2d(25, 51)
    glVertex2d(15, 51)
    glEnd()
    """red"""
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2d(15, 51)
    glVertex2d(25, 51)
    glVertex2d(25, 49)
    glVertex2d(15, 49)
    glEnd()
    """bar"""
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2d(15, 49)
    glVertex2d(16, 49)
    glVertex2d(16, 30)
    glVertex2d(15, 30)
    glEnd()


def draw_tree():
    """root """
    glColor3f(0.5, 0.0, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2d(5, 50)
    glVertex2d(11, 50)
    glVertex2d(8, 55)
    glEnd()

    """tree"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_POLYGON)
    glVertex2d(9, 63)
    glVertex2d(12, 60)
    glVertex2d(12, 64)
    glVertex2d(15, 67)
    glVertex2d(14, 70)
    glVertex2d(15, 73)
    glVertex2d(11, 77)
    glVertex2d(9, 81)
    glVertex2d(6, 77)
    glVertex2d(3, 75)
    glVertex2d(1, 72)
    glVertex2d(2, 66)
    glVertex2d(4, 65)
    glVertex2d(4, 61)
    glVertex2d(5, 63)
    glVertex2d(7, 63)
    glVertex2d(9, 63)
    glEnd()
    """trunck"""
    glColor3f(0.5, 0.0, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(7, 53)
    glVertex2d(9, 53)
    glVertex2d(9, 66)
    glVertex2d(7, 66)
    glEnd()
    """branch"""
    glColor3f(0.5, 0.0, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(9, 65)
    glVertex2d(12, 68)
    glVertex2d(10, 70)
    glVertex2d(8, 66)
    glVertex2d(6, 72)
    glVertex2d(5, 70)
    glVertex2d(7, 65)
    glEnd()

    """root """
    glColor3f(0.5, 0.0, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2d(88, 50)
    glVertex2d(94, 50)
    glVertex2d(91, 55)
    glEnd()

    """tree"""
    glColor3f(0.0, 0.6, 0.0)
    glBegin(GL_POLYGON)
    glVertex2d(92, 63)
    glVertex2d(95, 60)
    glVertex2d(95, 64)
    glVertex2d(98, 67)
    glVertex2d(97, 70)
    glVertex2d(98, 73)
    glVertex2d(94, 77)
    glVertex2d(92, 81)
    glVertex2d(89, 77)
    glVertex2d(86, 75)
    glVertex2d(84, 72)
    glVertex2d(85, 66)
    glVertex2d(87, 65)
    glVertex2d(87, 61)
    glVertex2d(88, 63)
    glVertex2d(90, 63)
    glVertex2d(92, 63)
    glEnd()
    """trunk"""
    glColor3f(0.5, 0.0, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(90, 53)
    glVertex2d(92, 53)
    glVertex2d(92, 66)
    glVertex2d(90, 66)
    glEnd()
    """branch"""
    glColor3f(0.5, 0.0, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(92, 65)
    glVertex2d(95, 68)
    glVertex2d(93, 70)
    glVertex2d(91, 66)
    glVertex2d(89, 72)
    glVertex2d(88, 70)
    glVertex2d(90, 65)
    glEnd()


def draw_road():
    """road"""
    glColor3f(0.4, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2d(0, 5)
    glVertex2d(100, 5)
    glVertex2d(100, 10)
    glVertex2d(0, 10)
    glEnd()



def draw_field():
    """field"""
    glColor3f(0.0, 0.8, 0.2)
    glBegin(GL_POLYGON)
    glVertex2d(0, 70)
    glVertex2d(100, 70)
    glVertex2d(100, 40)
    glVertex2d(0, 40)
    glEnd()


def draw_mountain():
    """mountain"""
    glColor3f(0.1, 0.7, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(0, 50)
    glVertex2d(0, 70)
    glVertex2d(100, 80)
    glVertex2d(100, 70)
    glVertex2d(55, 70)
    glVertex2d(0, 85)
    glEnd()


def draw_beside():
    """a"""
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.8, 0.2)
    glBegin(GL_POLYGON)
    glVertex2d(0, 0)
    glVertex2d(100, 0)
    glVertex2d(100, 60)
    glVertex2d(0, 60)
    glEnd()


def draw_house():
    """h1r1"""
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex2d(25, 52)
    glVertex2d(30, 50)
    glVertex2d(30, 60)
    glVertex2d(25, 62)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(24, 62)
    glVertex2d(30, 60)
    glVertex2d(28, 65)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(26, 54.5)
    glVertex2d(28, 53.5)
    glVertex2d(28, 57.5)
    glVertex2d(26, 58.5)
    glEnd()
    """side"""
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_POLYGON)
    glVertex2d(30, 50)
    glVertex2d(40, 50)
    glVertex2d(40, 60)
    glVertex2d(30, 60)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(34, 50)
    glVertex2d(37, 50)
    glVertex2d(37, 58)
    glVertex2d(34, 58)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 0.8)
    glBegin(GL_TRIANGLES)
    glVertex2d(30, 60)
    glVertex2d(41, 60)
    glVertex2d(35, 65)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 0.8)
    glBegin(GL_TRIANGLES)
    glVertex2d(28, 65)
    glVertex2d(30, 60)
    glVertex2d(35, 65)
    glEnd()

    """h2r1"""
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex2d(20, 57)
    glVertex2d(25, 55)
    glVertex2d(25, 65)
    glVertex2d(20, 67)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(19, 67)
    glVertex2d(25, 65)
    glVertex2d(23, 70)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(21, 59.5)
    glVertex2d(23, 58.5)
    glVertex2d(23, 62.5)
    glVertex2d(21, 63.5)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 0.8)
    glBegin(GL_TRIANGLES)
    glVertex2d(25, 65)
    glVertex2d(36, 65)
    glVertex2d(30, 70)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 0.8)
    glBegin(GL_TRIANGLES)
    glVertex2d(23, 70)
    glVertex2d(25, 65)
    glVertex2d(30, 70)
    glEnd()
    """h3r1"""
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex2d(15, 62)
    glVertex2d(20, 60)
    glVertex2d(20, 70)
    glVertex2d(15, 72)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(14, 72)
    glVertex2d(20, 70)
    glVertex2d(18, 75)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(16, 64.5)
    glVertex2d(18, 63.5)
    glVertex2d(18, 67.5)
    glVertex2d(16, 68.5)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, .8)
    glBegin(GL_TRIANGLES)
    glVertex2d(20, 70)
    glVertex2d(31, 70)
    glVertex2d(25, 75)
    glEnd()
    """roof"""
    glColor3f(0.0, 0.0, 0.8)
    glBegin(GL_TRIANGLES)
    glVertex2d(18, 75)
    glVertex2d(20, 70)
    glVertex2d(25, 75)
    glEnd()

    """h1r2"""
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex2d(70, 52)
    glVertex2d(75, 50)
    glVertex2d(75, 60)
    glVertex2d(70, 62)
    glEnd()
    """roof"""
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(69, 62)
    glVertex2d(75, 60)
    glVertex2d(73, 65)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(71, 54.5)
    glVertex2d(73, 53.5)
    glVertex2d(73, 57.5)
    glVertex2d(71, 58.5)
    glEnd()
    """side"""
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_POLYGON)
    glVertex2d(75, 50)
    glVertex2d(85, 50)
    glVertex2d(85, 60)
    glVertex2d(75, 60)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(79, 50)
    glVertex2d(82, 50)
    glVertex2d(82, 58)
    glVertex2d(79, 58)
    glEnd()
    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(75, 60)
    glVertex2d(86, 60)
    glVertex2d(80, 65)
    glEnd()
    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(73, 65)
    glVertex2d(75, 60)
    glVertex2d(80, 65)
    glEnd()

    """h2r2"""
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex2d(65, 57)
    glVertex2d(70, 55)
    glVertex2d(70, 65)
    glVertex2d(65, 67)
    glEnd()
    """roof"""
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(64, 67)
    glVertex2d(70, 65)
    glVertex2d(68, 70)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(66, 59.5)
    glVertex2d(68, 58.5)
    glVertex2d(68, 62.5)
    glVertex2d(66, 63.5)
    glEnd()

    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(70, 65)
    glVertex2d(81, 65)
    glVertex2d(75, 70)
    glEnd()
    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(68, 70)
    glVertex2d(70, 65)
    glVertex2d(75, 70)
    glEnd()

    """h3r2"""
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex2d(60, 62)
    glVertex2d(65, 60)
    glVertex2d(65, 70)
    glVertex2d(60, 72)
    glEnd()
    """roof"""
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(59, 72)
    glVertex2d(65, 70)
    glVertex2d(63, 75)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(61, 64.5)
    glVertex2d(63, 63.5)
    glVertex2d(63, 67.5)
    glVertex2d(61, 68.5)
    glEnd()

    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(65, 70)
    glVertex2d(76, 70)
    glVertex2d(70, 75)
    glEnd()
    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(63, 75)
    glVertex2d(65, 70)
    glVertex2d(70, 75)
    glEnd()

    """h3r2"""
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex2d(38, 67)
    glVertex2d(43, 65)
    glVertex2d(43, 75)
    glVertex2d(38, 77)
    glEnd()
    """roof"""
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(37, 77)
    glVertex2d(43, 75)
    glVertex2d(41, 80)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(39, 69.5)
    glVertex2d(41, 68.5)
    glVertex2d(41, 72.5)
    glVertex2d(39, 73.5)
    glEnd()
    """side"""
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_POLYGON)
    glVertex2d(43, 65)
    glVertex2d(53, 65)
    glVertex2d(53, 75)
    glVertex2d(43, 75)
    glEnd()
    """door"""
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2d(47, 65)
    glVertex2d(50, 65)
    glVertex2d(50, 72)
    glVertex2d(47, 72)
    glEnd()
    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(43, 75)
    glVertex2d(54, 75)
    glVertex2d(48, 80)
    glEnd()
    """roof"""
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(41, 80)
    glVertex2d(43, 75)
    glVertex2d(48, 80)
    glEnd()


def draw():
    draw_beside()
    draw_mountain()
    draw_field()
    draw_road()
    draw_sky()
    draw_sun()
    draw_flag()
    draw_fence()
    draw_house()
    draw_bushes()
    draw_tree()
    glFlush()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
