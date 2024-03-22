from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluOrtho2D 
import math
import sys

# Variables para la posición del dibujo
pos_x = 0
pos_y = 0

def tortuga():
    # Dibuja el cuerpo 
    glPushMatrix()
    glTranslatef(200, 200, 0)  # Movemos la tortuga al centro de la ventana
    glScalef(0.5, 0.5, 0.0)  # Escalamos la tortuga a la mitad de su tamaño original
    glTranslate(pos_x, pos_y, 0) # Movemos la tortuga según las teclas presionadas
    #Cabeza
    glColor3f(0.3255, 0.0314, 0.0275)
    glBegin(GL_POLYGON)
    glVertex2i(300, 590)
    glVertex2i(230, 550)
    glVertex2i(230, 650)
    glVertex2i(300, 690)
    glVertex2i(370, 650)
    glVertex2i(370, 550)
    glEnd()
    #Aleta izquierda
    glColor3f(0.2745, 0.0431, 0.0392)
    glBegin(GL_POLYGON)
    glVertex2i(170, 590)
    glVertex2i(200, 540)
    glVertex2i(150, 510)
    glVertex2i(60, 590)
    glEnd()
    glColor3f(0.2196, 0.0118, 0.0118)
    glBegin(GL_TRIANGLES)
    glVertex2i(60, 590)
    glVertex2i(150, 510)
    glVertex2i(50, 510)
    glEnd()
    glColor3f(0.1255, 0, 0.0039)
    glBegin(GL_POLYGON)
    glVertex2i(50, 510)
    glVertex2i(60, 590)
    glVertex2i(-10, 530)
    glVertex2i(-20, 430)
    glEnd()
    #Aleta derecha
    glColor3f(0.2745, 0.0431, 0.0392)
    glBegin(GL_POLYGON)
    glVertex2i(430, 590)
    glVertex2i(400, 540)
    glVertex2i(450, 510)
    glVertex2i(540, 590)
    glEnd()
    glColor3f(0.2196, 0.0118, 0.0118)
    glBegin(GL_TRIANGLES)
    glVertex2i(540, 590)
    glVertex2i(450, 510)
    glVertex2i(550, 510)
    glEnd()
    glColor3f(0.1255, 0, 0.0039)
    glBegin(GL_POLYGON)
    glVertex2i(550, 510)
    glVertex2i(540, 590)
    glVertex2i(600, 530)
    glVertex2i(610, 430)
    glEnd()
    # Penagono de hasta arriba
    glColor3f(0.8414, 0.3665, 0.3925)
    glBegin(GL_POLYGON)
    glVertex2i(210, 480)
    glVertex2i(390, 480)
    glVertex2i(400, 540)
    glVertex2i(300, 590)
    glVertex2i(200, 540)
    glEnd()
    #Pentagono oscuro de la derecha
    glColor3f(0.6, 0.1137, 0.098)
    glBegin(GL_POLYGON)
    glVertex2i(180, 450)
    glVertex2i(200, 540)
    glVertex2i(210, 480)
    glVertex2d(150, 510)
    glVertex2d(200, 540)
    glEnd()
    #Pentagono oscuro de la izquierda
    glColor3f(0.6, 0.1137, 0.098)
    glBegin(GL_POLYGON)
    glVertex2i(400, 540)
    glVertex2i(420, 450)
    glVertex2d(390, 480)
    glVertex2d(450, 510)
    glVertex2d(420, 450)
    glEnd()
    #Pentagono central de abajo 
    glColor3f(0.8314, 0.3765, 0.3725)
    glBegin(GL_POLYGON)
    glVertex2i(200, 400)
    glVertex2i(400, 400)
    glVertex2i(420, 450)  
    glVertex2i(180, 450)  
    glVertex2i(210, 480)  
    glVertex2i(390, 480)
    glVertex2i(420, 450)  
    glEnd()
    #Hexagono central
    glColor3f(0.7686, 0.4471, 0.4471)
    glBegin(GL_POLYGON)
    glVertex2i(200, 400)
    glVertex2i(400, 400)
    glVertex2i(400, 300)
    glEnd()
    #Hexagono central arriba izquierda
    glColor3f(0.6235, 0.1843, 0.1843)
    glBegin(GL_POLYGON)
    glVertex2i(200, 400)
    glVertex2i(150, 510)
    glVertex2i(180, 450)
    glVertex2i(160, 350)
    glVertex2i(100, 360)
    glVertex2i(150, 510)
    glEnd()
    #Hexagono central arriba derecha
    glColor3f(0.6235, 0.1843, 0.1843)
    glBegin(GL_POLYGON)
    glVertex2i(400, 400)
    glVertex2i(450, 510)
    glVertex2i(420, 450)
    glVertex2i(440, 350)
    glVertex2i(500, 360)
    glVertex2i(450, 510)
    glEnd()
    # Hazta aqui
    #Mitad de abajo
    glColor3f(0.77, 0.45, 0.45)
    glBegin(GL_POLYGON)
    glVertex2i(200, 400)
    glVertex2i(400, 400)
    glVertex2i(440, 350)  
    glVertex2i(160, 350)
    glVertex2i(200, 300)
    glVertex2i(400, 300)
    glVertex2i(440, 350)  
    glEnd()

    #Hexagono izquierdan arriba
    glColor3f(0.5843, 0.2588, 0.2627)
    glBegin(GL_POLYGON)
    glVertex2i(150, 220)
    glVertex2i(160, 350)
    glVertex2i(100, 360)
    glVertex2i(200, 300)
    glVertex2i(180, 330)
    glVertex2i(160, 350)
    glEnd()

    #Hexagono central abajo 
    glColor3f(0.4235, 0.1490, 0.1451)
    glBegin(GL_POLYGON)
    glVertex2i(200, 300)
    glVertex2i(400, 300)
    glVertex2i(350, 220)  
    glVertex2i(250, 220)  
    glEnd()

    #Hexagono central de abajo derecha
    glColor3f(0.5843, 0.2588, 0.2627)
    glBegin(GL_POLYGON)
    glVertex2i(450, 220)
    glVertex2i(440, 350)
    glVertex2i(500, 360)
    glVertex2i(400, 300)
    glVertex2i(420, 330)
    glVertex2i(440, 350)
    glEnd()

    #Hexagono central de abajo izquierda
    glColor3f(0.4784, 0.2941, 0.2941)
    glBegin(GL_POLYGON)
    glVertex2i(200, 300)
    glVertex2i(150, 220)
    glVertex2i(200, 150)
    glVertex2i(250, 220)  
    glEnd()
    #Hazta aqui
    #Hexagono central de abajo derecha
    glColor3f(0.4784, 0.2941, 0.2941)
    glBegin(GL_POLYGON)
    glVertex2i(400, 300)
    glVertex2i(450, 220)
    glVertex2i(400, 150)
    glVertex2i(350, 220)
    glEnd()
    #Hazta aqui
    #Hexagono central hasta abajo "cola"
    glColor3f(0.4, 0.1059, 0.1137)
    glBegin(GL_POLYGON)
    glVertex2i(250, 220)
    glVertex2i(350, 220)
    glVertex2i(400, 150)
    glVertex2i(300, 80)
    glVertex2i(200, 150)
    glVertex2i(250, 210)  
    glEnd()
    #Hazta aqui
    #Pata izquierda
    glColor3f(0.4235, 0.1647, 0.1686)
    glBegin(GL_POLYGON)
    glVertex2i(200, 150)
    glVertex2i(150, 100)
    glVertex2i(150, 220)
    glVertex2i(100, 150)
    glVertex2i(110, 110)
    glVertex2i(150, 100)
    glEnd()
    #Pata derecha
    glColor3f(0.4235, 0.1647, 0.1686)
    glBegin(GL_POLYGON)
    glVertex2i(400, 150)
    glVertex2i(450, 100)
    glVertex2i(450, 220)
    glVertex2i(500, 150)
    glVertex2i(490, 110)
    glVertex2i(450, 100)
    glEnd()

    glPopMatrix()

# Función para manejar el movimiendo con el teclado
def keyboard(key, x, y):
    global pos_x, pos_y
    # Verifica qué tecla fue presionada
    if key == b'\x1b':  # Escape key
        sys.exit(0)
    elif key == b'w':
        pos_y += 10  # Mueve hacia arriba
    elif key == b's':
        pos_y -= 10  # Mueve hacia abajo
    elif key == b'a':
        pos_x -= 10  # Mueve hacia la izquierda
    elif key == b'd':
        pos_x += 10  # Mueve hacia la derecha
    # Redibuja la escena
    glutPostRedisplay()

def myInit():
    glClearColor(1.0, 1.0, 1.0, 1.0)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 800.0, 0.0, 600.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    tortuga()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(800,600)
    glutInitWindowPosition(int((glutGet(GLUT_SCREEN_WIDTH)-800)/2), int((glutGet(GLUT_SCREEN_HEIGHT)-600)/2))  
    glutCreateWindow(b"Tortuga")
    myInit()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard) 
    glutMainLoop()

if __name__ == "__main__":
    main()