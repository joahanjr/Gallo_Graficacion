from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluOrtho2D 
import math
import sys

# Variables para la rotación
angle_x = 0.0
angle_y = 0.0
scale = 5.0

# Variable para alternar entre las vistas de los colibríes
def colibri():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)  # Establecer el modo de matriz de vista/modelo
    glLoadIdentity()  # Cargar la matriz identidad
    glPushMatrix()
    glRotatef(angle_x, 1.0, 0.0, 0.0)  # Rotar en el eje X
    glRotatef(angle_y, 0.0, 1.0, 0.0)  # Rotar en el eje Y

    # Parte trasera
    glColor3f(0.9843, 0.6745, 0.2275)  # Color de la parte trasera
    glBegin(GL_TRIANGLES)
    # Cuerpo triangulo 1
    glVertex3f(700.0 / scale, 560.0 / scale, -5.0 / scale)
    glVertex3f(570.0 / scale, 800.0 / scale, -5.0 / scale)
    glVertex3f(680.0 / scale, 880.0 / scale, -5.0 / scale)
    # Cuerpo triangulo 2
    glVertex3f(705.0 / scale, 565.0 / scale, -5.0 / scale)
    glVertex3f(820.0 / scale, 640.0 / scale, -5.0 / scale)
    glVertex3f(685.0 / scale, 880.0 / scale, -5.0 / scale)
    # Ala
    glVertex3f(825.0 / scale, 645.0 / scale, -5.0 / scale)
    glVertex3f(695.0 / scale, 880.0 / scale, -5.0 / scale)
    glVertex3f(1100.0 / scale, 1050.0 / scale, -5.0 / scale)
    # Cuello
    glVertex3f(680.0 / scale, 885.0 / scale, -5.0 / scale)
    glVertex3f(580.0 / scale, 940.0 / scale, -5.0 / scale)
    glVertex3f(565.0 / scale, 805.0 / scale, -5.0 / scale)
    # Cuello2
    glVertex3f(575.0 / scale, 945.0 / scale, -5.0 / scale)
    glVertex3f(560.0 / scale, 810.0 / scale, -5.0 / scale)
    glVertex3f(500.0 / scale, 890.0 / scale, -5.0 / scale)
    # Cabeza
    glVertex3f(450.0 / scale, 930.0 / scale, -5.0 / scale)
    glVertex3f(560.0 / scale, 940.0 / scale, -5.0 / scale)
    glVertex3f(495.0 / scale, 895.0 / scale, -5.0 / scale)
    # Pico
    glVertex3f(445.0 / scale, 925.0 / scale, -5.0 / scale)
    glVertex3f(485.0 / scale, 895.0 / scale, -5.0 / scale)
    glVertex3f(340.0 / scale, 930.0 / scale, -5.0 / scale)
    # Para las piernas
    glVertex3f(825.0 / scale, 635.0 / scale, -5.0 / scale)
    glVertex3f(800.0 / scale, 500.0 / scale, -5.0 / scale)
    glVertex3f(700.0 / scale, 555.0 / scale, -5.0 / scale)
    # Piernas
    glVertex3f(700.0 / scale, 550.0 / scale, -5.0 / scale)
    glVertex3f(700.0 / scale, 420.0 / scale, -5.0 / scale)
    glVertex3f(795.0 / scale, 495.0 / scale, -5.0 / scale)
    # Pie
    glVertex3f(695.0 / scale, 420.0 / scale, -5.0 / scale)
    glVertex3f(695.0 / scale, 500.0 / scale, -5.0 / scale)
    glVertex3f(630.0 / scale, 420.0 / scale, -5.0 / scale)
    # Cola1
    glVertex3f(830.0 / scale, 630.0 / scale, -5.0 / scale)
    glVertex3f(805.0 / scale, 500.0 / scale, -5.0 / scale)
    glVertex3f(890.0 / scale, 420.0 / scale, -5.0 / scale)
    # Cola2
    glVertex3f(900.0 / scale, 410.0 / scale, -5.0 / scale)
    glVertex3f(840.0 / scale, 630.0 / scale, -5.0 / scale)
    glVertex3f(1020.0 / scale, 300.0 / scale, -5.0 / scale)
    # Cola3
    glVertex3f(1010.0 / scale, 300.0 / scale, -5.0 / scale)
    glVertex3f(890.0 / scale, 410.0 / scale, -5.0 / scale)
    glVertex3f(920.0 / scale, 230.0 / scale, -5.0 / scale)
    # Cola4
    glVertex3f(910.0 / scale, 230.0 / scale, -5.0 / scale) 
    glVertex3f(880.0 / scale, 415.0 / scale, -5.0 / scale)
    glVertex3f(800.0 / scale, 495.0 / scale, -5.0 / scale)
    glEnd()
    # Parte delantera
    glColor3f(0.9294, 0.3019, 0.2549)  # Color de la parte delantera
    glBegin(GL_TRIANGLES)
    # Cuerpo triangulo 1
    glVertex3f(700.0 / scale, 560.0 / scale, 5.0 / scale)
    glVertex3f(570.0 / scale, 800.0 / scale, 5.0 / scale)
    glVertex3f(680.0 / scale, 880.0 / scale, 5.0 / scale)
    # Cuerpo triangulo 2
    glVertex3f(705.0 / scale, 565.0 / scale, 5.0 / scale)
    glVertex3f(820.0 / scale, 640.0 / scale, 5.0 / scale)
    glVertex3f(685.0 / scale, 880.0 / scale, 5.0 / scale)
    # Ala
    glVertex3f(825.0 / scale, 645.0 / scale, 5.0 / scale)
    glVertex3f(695.0 / scale, 880.0 / scale, 5.0 / scale)
    glVertex3f(1100.0 / scale, 1050.0 / scale, 5.0 / scale)
    # Cuello
    glVertex3f(680.0 / scale, 885.0 / scale, 5.0 / scale)
    glVertex3f(580.0 / scale, 940.0 / scale, 5.0 / scale)
    glVertex3f(565.0 / scale, 805.0 / scale, 5.0 / scale)
    # Cuello2
    glVertex3f(575.0 / scale, 945.0 / scale, 5.0 / scale)
    glVertex3f(560.0 / scale, 810.0 / scale, 5.0 / scale)
    glVertex3f(500.0 / scale, 890.0 / scale, 5.0 / scale)
    # Cabeza
    glVertex3f(450.0 / scale, 930.0 / scale, 5.0 / scale)
    glVertex3f(560.0 / scale, 940.0 / scale, 5.0 / scale)
    glVertex3f(495.0 / scale, 895.0 / scale, 5.0 / scale)
    # Pico
    glVertex3f(445.0 / scale, 925.0 / scale, 5.0 / scale)
    glVertex3f(485.0 / scale, 895.0 / scale, 5.0 / scale)
    glVertex3f(340.0 / scale, 930.0 / scale, 5.0 / scale)
    # Para las piernas
    glVertex3f(825.0 / scale, 635.0 / scale, 5.0 / scale)
    glVertex3f(800.0 / scale, 500.0 / scale, 5.0 / scale)
    glVertex3f(700.0 / scale, 555.0 / scale, 5.0 / scale)
    # Piernas
    glVertex3f(700.0 / scale, 550.0 / scale, 5.0 / scale)
    glVertex3f(700.0 / scale, 420.0 / scale, 5.0 / scale)
    glVertex3f(795.0 / scale, 495.0 / scale, 5.0 / scale)
    # Pie
    glVertex3f(695.0 / scale, 420.0 / scale, 5.0 / scale)
    glVertex3f(695.0 / scale, 500.0 / scale, 5.0 / scale)
    glVertex3f(630.0 / scale, 420.0 / scale, 5.0 / scale)
    # Cola1
    glVertex3f(830.0 / scale, 630.0 / scale, 5.0 / scale)
    glVertex3f(805.0 / scale, 500.0 / scale, 5.0 / scale)
    glVertex3f(890.0 / scale, 420.0 / scale, 5.0 / scale)
    # Cola2
    glVertex3f(900.0 / scale, 410.0 / scale, 5.0 / scale)
    glVertex3f(840.0 / scale, 630.0 / scale, 5.0 / scale)
    glVertex3f(1020.0 / scale, 300.0 / scale, 5.0 / scale)
    # Cola3
    glVertex3f(1010.0 / scale, 300.0 / scale, 5.0 / scale)
    glVertex3f(890.0 / scale, 410.0 / scale, 5.0 / scale)
    glVertex3f(920.0 / scale, 230.0 / scale, 5.0 / scale)
    # Cola4
    glVertex3f(910.0 / scale, 230.0 / scale, 5.0 / scale) 
    glVertex3f(880.0 / scale, 415.0 / scale, 5.0 / scale)
    glVertex3f(800.0 / scale, 495.0 / scale, 5.0 / scale)
    glEnd()

    glPopMatrix()


def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # Establece el color de fondo como blanco
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400.0, 400.0, -300.0, 300.0, -400.0, 400.0)  # Definir la proyección en 3D
    glEnable(GL_DEPTH_TEST)  # Habilitar el z-buffer para ocultación de caras

    # Deshabilitar el culling de caras para mostrar ambos lados del objeto
    glDisable(GL_CULL_FACE)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
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
