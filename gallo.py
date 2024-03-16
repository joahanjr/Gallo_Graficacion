from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluOrtho2D 
import math
import sys

# Hecho por 
# Joahan Jiemenez Ramirez A200782
# Y 
# Alexis Johesio Solis Utrilla
# 8vo "N" - Graficación 

def patas():
    glColor3f(0.1, 0.8, 0.3) 
    glBegin(GL_QUADS)
    glVertex2i(372,113)
    glVertex2i(378,113)
    glVertex2i(378,60)
    glVertex2i(372,60)
    glEnd()
    
    glColor3f(0.2, 0.5, 0.7) 
    num_segments = 100
    center_x = 375
    center_y = 45
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
    glColor3f(0.8, 0.4, 0.2)  
    glBegin(GL_TRIANGLES)
    glVertex2i(348,200)
    glVertex2i(323,150)
    glVertex2i(288,200)
    glEnd()
    
    glColor3f(0.9, 0.1, 0.1)  
    glBegin(GL_QUADS)
    glVertex2i(348,202)
    glVertex2i(288,202)
    glVertex2i(258,252)
    glVertex2i(318,252)
    glEnd()
    
    glColor3f(0.8, 0.4, 0.2) 
    glBegin(GL_TRIANGLES)
    glVertex2i(256,252)
    glVertex2i(286,202)
    glVertex2i(252,135)
    glEnd()

def cuerpo():
    glColor3f(0.9, 0.9, 0.8)  
    glBegin(GL_POLYGON)
    glVertex2i(350,200)
    glVertex2i(400,200)
    glVertex2i(425,150)
    glVertex2i(375,115)
    glVertex2i(325,150)
    glEnd()

def cabeza():
    glColor3f(0.5, 0.5, 0.2) 
    glBegin(GL_TRIANGLES)
    glVertex2i(400,202)
    glVertex2i(350,202)
    glVertex2i(400,290)
    glEnd()
    
    glColor3f(0.2, 0.2, 0.2) 
    glBegin(GL_QUADS)
    glVertex2i(402,250)
    glVertex2i(442,250)
    glVertex2i(442,290)
    glVertex2i(402,290)
    glEnd()
    
    glColor3f(0.8, 0.1, 0.1) 
    glBegin(GL_TRIANGLES)
    glVertex2i(372,292)
    glVertex2i(442,292)
    glVertex2i(400,340)
    glEnd()
    
    glColor3f(0.8, 0.4, 0.2) 
    glBegin(GL_TRIANGLES)
    glVertex2i(444,250)
    glVertex2i(444,285)
    glVertex2i(470,250)
    glEnd()
    
    glColor3f(0.9, 0.1, 0.1) 
    glBegin(GL_TRIANGLES)
    glVertex2i(412,249)
    glVertex2i(394,215)
    glVertex2i(428,215)
    glEnd()

def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  
    cuerpo()
    patas()
    cola()
    cabeza()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(800,600)
    glutInitWindowPosition(int((glutGet(GLUT_SCREEN_WIDTH)-800)/2), int((glutGet(GLUT_SCREEN_HEIGHT)-600)/2))  # Centrado
    glutCreateWindow(b"Gallito")
    myInit()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
