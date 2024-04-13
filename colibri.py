from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluOrtho2D 
import math
import sys

# Variables para la rotación
angle_x = 0.0
angle_y = 0.0
scale = 400

# Variable para alternar entre las vistas de los colibríes
def colibri():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(angle_x, 1.0, 0.0, 0.0)  # Rotar en el eje X
    glRotatef(angle_y, 0.0, 1.0, 0.0)  # Rotar en el eje Y
    glScalef(0.5, 0.5, 1.0)

    #parte traseras
    #Cuerpo triangulo 1
    glColor3f(0.9843, 0.6745, 0.2275)
    glBegin(GL_TRIANGLES)
    glVertex3i(700, 560, -1)
    glVertex3i(570, 800, -1)
    glVertex3i(680, 880, -1)
    glEnd()

    #Cuerpo triangulo 2
    glBegin(GL_TRIANGLES)
    glVertex3i(705, 565, -1)
    glVertex3i(820, 640, -1)
    glVertex3i(685, 880, -1)
    glEnd()

    #Ala
    glBegin(GL_TRIANGLES)
    glVertex3i(825, 645, -1)
    glVertex3i(695, 880, -1)
    glVertex3i(1100, 1050, -1)
    glEnd()

    #cuello
    glBegin(GL_TRIANGLES)
    glVertex3i(680, 885, -1)
    glVertex3i(580, 940, -1)
    glVertex3i(565, 805, -1)
    glEnd()

    #cuello2
    glBegin(GL_TRIANGLES)
    glVertex3i(575, 945, -1)
    glVertex3i(560, 810, -1)
    glVertex3i(500, 890, -1)
    glEnd()
    
    #Cabeza
    glBegin(GL_TRIANGLES)
    glVertex3i(450, 930, -1)
    glVertex3i(560, 940, -1)
    glVertex3i(495, 895, -1)
    glEnd()

    #Pico
    glBegin(GL_TRIANGLES)
    glVertex3i(445, 925, -1)
    glVertex3i(485, 895, -1)
    glVertex3i(340, 930, -1)
    glEnd()

    #Para las piernas
    glBegin(GL_TRIANGLES)
    glVertex3i(825, 635, -1)
    glVertex3i(800, 500, -1)
    glVertex3i(700, 555, -1)
    glEnd()

    #Piernas
    glBegin(GL_TRIANGLES)
    glVertex3i(700, 550, -1)
    glVertex3i(700, 420, -1)
    glVertex3i(795, 495, -1)
    glEnd()

    #Pie
    glBegin(GL_TRIANGLES)
    glVertex3i(695, 420, -1)
    glVertex3i(695, 500, -1)
    glVertex3i(630, 420, -1)
    glEnd()

    #Cola1
    glBegin(GL_TRIANGLES)
    glVertex3i(830, 630, -1)
    glVertex3i(805, 500, -1)
    glVertex3i(890, 420, -1)
    glEnd()

    #Cola2
    glBegin(GL_TRIANGLES)
    glVertex3i(900, 410, -1)
    glVertex3i(840, 630, -1)
    glVertex3i(1020, 300, -1)
    glEnd()

    #Cola3
    glBegin(GL_TRIANGLES)
    glVertex3i(1010, 300, -1)
    glVertex3i(890, 410, -1)
    glVertex3i(920, 230, -1)
    glEnd()

    #Cola4
    glBegin(GL_TRIANGLES)
    glVertex3i(910, 230, -1) 
    glVertex3i(880, 415, -1)
    glVertex3i(800, 495, -1)
    glEnd()
    
    # Aparte de adelante

    #Cuerpo triangulo 1
    glColor3f(0.9294, 0.3019, 0.2549)
    glBegin(GL_TRIANGLES)
    glVertex3i(700, 560, 1)
    glVertex3i(570, 800, 1)
    glVertex3i(680, 880, 1)
    glEnd()

    #Cuerpo triangulo 2
    glBegin(GL_TRIANGLES)
    glVertex3i(705, 565, 1)
    glVertex3i(820, 640, 1)
    glVertex3i(685, 880, 1)
    glEnd()

    #Ala
    glBegin(GL_TRIANGLES)
    glVertex3i(825, 645, 1)
    glVertex3i(695, 880, 1)
    glVertex3i(1100, 1050, 1)
    glEnd()

    #cuello
    glBegin(GL_TRIANGLES)
    glVertex3i(680, 885, 1)
    glVertex3i(580, 940, 1)
    glVertex3i(565, 805, 1)
    glEnd()

    #cuello2
    glBegin(GL_TRIANGLES)
    glVertex3i(575, 945, 1)
    glVertex3i(560, 810, 1)
    glVertex3i(500, 890, 1)
    glEnd()
    
    #Cabeza
    glBegin(GL_TRIANGLES)
    glVertex3i(450, 930, 1)
    glVertex3i(560, 940, 1)
    glVertex3i(495, 895, 1)
    glEnd()

    #Pico
    glBegin(GL_TRIANGLES)
    glVertex3i(445, 925, 1)
    glVertex3i(485, 895, 1)
    glVertex3i(340, 930, 1)
    glEnd()

    #Para las piernas
    glBegin(GL_TRIANGLES)
    glVertex3i(825, 635, 1)
    glVertex3i(800, 500, 1)
    glVertex3i(700, 555, 1)
    glEnd()

    #Piernas
    glBegin(GL_TRIANGLES)
    glVertex3i(700, 550, 1)
    glVertex3i(700, 420, 1)
    glVertex3i(795, 495, 1)
    glEnd()

    #Pie
    glBegin(GL_TRIANGLES)
    glVertex3i(695, 420, 1)
    glVertex3i(695, 500, 1)
    glVertex3i(630, 420, 1)
    glEnd()

    #Cola1
    glBegin(GL_TRIANGLES)
    glVertex3i(830, 630, 1)
    glVertex3i(805, 500, 1)
    glVertex3i(890, 420, 1)
    glEnd()

    #Cola2
    glBegin(GL_TRIANGLES)
    glVertex3i(900, 410, 1)
    glVertex3i(840, 630, 1)
    glVertex3i(1020, 300, 1)
    glEnd()

    #Cola3
    glBegin(GL_TRIANGLES)
    glVertex3i(1010, 300, 1)
    glVertex3i(890, 410, 1)
    glVertex3i(920, 230, 1)
    glEnd()

    #Cola4
    glBegin(GL_TRIANGLES)
    glVertex3i(910, 230, 1) 
    glVertex3i(880, 415, 1)
    glVertex3i(800, 495, 1)
    glEnd()

    # Conexión entre la parte trasera y la parte delantera
    glColor3f(0.10196078431, 0.27450980392, 0.78039215686)
    glBegin(GL_QUADS)
    glVertex3i(700, 560, -1)
    glVertex3i(570, 800, -1)
    glVertex3i(570, 800, 1)
    glVertex3i(700, 560, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(825, 645, -1)
    glVertex3i(695, 880, -1)
    glVertex3i(695, 880, 1)
    glVertex3i(825, 645, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(680, 885, -1)
    glVertex3i(580, 940, -1)
    glVertex3i(580, 940, 1)
    glVertex3i(680, 885, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(450, 930, -1)
    glVertex3i(560, 940, -1)
    glVertex3i(560, 940, 1)
    glVertex3i(450, 930, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(445, 925, -1)
    glVertex3i(340, 930, -1)
    glVertex3i(340, 930, 1)
    glVertex3i(445, 925, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(825, 635, -1)
    glVertex3i(800, 500, -1)
    glVertex3i(800, 500, 1)
    glVertex3i(825, 635, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(700, 550, -1)
    glVertex3i(700, 420, -1)
    glVertex3i(700, 420, 1)
    glVertex3i(700, 550, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(695, 420, -1)
    glVertex3i(695, 500, -1)
    glVertex3i(695, 500, 1)
    glVertex3i(695, 420, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(830, 630, -1)
    glVertex3i(805, 500, -1)
    glVertex3i(805, 500, 1)
    glVertex3i(830, 630, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(900, 410, -1)
    glVertex3i(840, 630, -1)
    glVertex3i(840, 630, 1)
    glVertex3i(900, 410, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(1010, 300, -1)
    glVertex3i(890, 410, -1)
    glVertex3i(890, 410, 1)
    glVertex3i(1010, 300, 1)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3i(910, 230, -1) 
    glVertex3i(880, 415, -1)
    glVertex3i(880, 415, 1)
    glVertex3i(910, 230, 1)
    glEnd()

    glPopMatrix()


def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # Establece el color de fondo como blanco
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Cambia el color de dibujo a negro
    colibri()  # Mostrar el colibrí actual
    glFlush()

def specialKeys(key, x, y):
    global angle_x
    global angle_y
    if key == GLUT_KEY_LEFT:
        angle_y -= 5  # Girar hacia la izquierda en el eje Y
    elif key == GLUT_KEY_RIGHT:
        angle_y += 5  # Girar hacia la derecha en el eje Y
    elif key == GLUT_KEY_UP:
        angle_x += 5  # Girar hacia arriba en el eje X
    elif key == GLUT_KEY_DOWN:
        angle_x -= 5  # Girar hacia abajo en el eje X
    glutPostRedisplay()


def update(value):
    glutTimerFunc(10, update, 0)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(int((glutGet(GLUT_SCREEN_WIDTH) - 800) / 2), int((glutGet(GLUT_SCREEN_HEIGHT) - 600) / 2))  # Centrado
    glutCreateWindow(b"Colibri")
    myInit()
    glutDisplayFunc(display)
    glutSpecialFunc(specialKeys)  # Manejar teclas especiales
    glutTimerFunc(10, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
