from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(0, 640, 0, 480)
def plotpoints():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 0.0, 0.0)

	glBegin(GL_POINTS)
	glVertex2f(0.0, 0.0)
	glEnd()

	glFlush()

def roundf(x):
	return (math.floor(x+0.5))

def dda_line():
	x1 = 1
	x2 = 640
	y1 = 1
	y2 = 480
	dx = (x2 - x1)
	dy = (y2 - y1)
	if abs(dx) >= abs(dy):
		length = dx
	else:
		length = dy
	xinc = dx/length
	yinc = dy/length
	x = x1
	y = y1
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 0.0, 0.0)

	glBegin(GL_POINTS)
	glVertex2d(x,y)

	for i in range(0,length):
		x = x+xinc
		y = y+yinc
		glVertex2d(roundf(x), roundf(y))
	
	glEnd()
	glFlush()


def main():
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(640,480)
	glutInitWindowPosition(50,50)
	glutCreateWindow(b'Plot Points')
	glutDisplayFunc(dda_line)



	init()
	glutMainLoop()

main()