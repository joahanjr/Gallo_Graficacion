from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluOrtho2D 

import math
import sys

# Hecho por 
# Joahan Jiemenez Ramirez A200782
# Y 
# Alexis Johesio Solis Utrilla
#8vo "N" - Graficación 

def patas():
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2i(222,163)
    glVertex2i(228,163)
    glVertex2i(228,110)
    glVertex2i(222,110)
    glEnd()
    
    glColor3f(0.0, 0.5, 1.0)
    num_segments = 100
    center_x = 225
    center_y = 95
    radius_x = 50
    radius_y = 10
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius_x * math.cos(theta)
        y = radius_y * math.sin(theta)
        glVertex2f(x + center_x, y + center_y)
    glEnd()

def cola():
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(198, 250)
    glVertex2i(173, 200)
    glVertex2i(138, 250)
    glEnd()
    
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_QUADS)
    glVertex2i(198, 252)
    glVertex2i(138, 252)
    glVertex2i(108, 302)
    glVertex2i(168, 302)
    glEnd()
    
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(106, 302)
    glVertex2i(136, 252)
    glVertex2i(102, 185)
    glEnd()

def cuerpo():
    glColor3f(0.1, 0.1, 0.0)
    glBegin(GL_POLYGON)
    glVertex2i(200, 250)
    glVertex2i(250, 250)
    glVertex2i(275, 200)
    glVertex2i(225, 165)
    glVertex2i(175, 200)
    glEnd()

def cabeza():
    glColor3f(0.1, 0.1, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(250, 252)
    glVertex2i(200, 252)
    glVertex2i(250, 340)
    glEnd()
    
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_QUADS)
    glVertex2i(252, 300)
    glVertex2i(292, 300)
    glVertex2i(292, 340)
    glVertex2i(252, 340)
    glEnd()
    
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(222, 342)
    glVertex2i(292, 342)
    glVertex2i(250, 390)
    glEnd()
    
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(294, 300)
    glVertex2i(294, 335)
    glVertex2i(320, 300)
    glEnd()
    
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(272, 299)
    glVertex2i(254, 265)
    glVertex2i(288, 265)
    glEnd()

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    cuerpo()
    patas()
    cola()
    cabeza()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(800,600)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Gallito")
    myInit()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
