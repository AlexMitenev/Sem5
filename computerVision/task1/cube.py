__author__ = 'Mitenev'
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def initGL(width, height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    viewAngle = 45.0
    aspect = float(width) / float(height)
    #gluPerspective(viewAngle, aspect, 0.1, 100.0)
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)


def drawGLScene():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    #glTranslatef(0.0, 0.0, -3.0) # for perspective use translate
    #glRotatef(0.0, 1.0, 1.0, 1.0)

    glBegin(GL_QUADS)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)

    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)

    glEnd()

    # since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()


def main():
    global window
    glutInit(sys.argv)

    # get a 640 x 480 window
    glutInitWindowSize(600, 600)
    window = glutCreateWindow("example")
    glutIdleFunc(drawGLScene)

    # Initialize our window.
    initGL(600, 600)


main()
glutMainLoop()
