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
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POINTS)
	glVertex2f(0.0, 0.0)
	glEnd()
	glFlush()

def roundf(x):
	return (math.floor(x+0.5))

def setpixel(x0, y0):
	glColor3f(1.0,1.0,1.0)
	glBegin(GL_POINTS)
	glVertex2i(x0, y0)
	glEnd()

def bx(x0,y0,x1,y1,dx,dy):
	i = 2*dy - dx
	j = 2*dy
	k = 2*(dy - dx)
	if(not(x0 < x1)):
		t = x0
		x0 = x1
		x1 = t
		t = y0
		y0 = y1
		y1 = t
	setpixel(x0,y0)
	while(x0 < x1):
		if(i<0):
			i = i + j
		else:
			if (y0 < y1):
				y0 = y0 + 1
			else:
				y0 = y0 - 1
			i = i + k
		x0 = x0 + 1
		setpixel(x0,y0)

def by(x0,y0,x1,y1,dx,dy):
	i = 2*dx - dy
	j = 2*dx
	k = 2*(dx - dy)
	if(not(y0 < y1)):
		t = y0
		y0 = y1
		y1 = t
		t = x0
		x0 = x1
		x1 = t
	setpixel(x0,y0)
	while(y0 < y1):
		if(i<0):
			i = i + j
		else:
			if (x0 < x1):
				x0 = x0 + 1
			else:
				x0 = x0 - 1
			i = i + k
		y0 = y0 + 1
		setpixel(x0,y0)

def bressenham():
	x0 = 0
	y0 = 0
	x1 = 600
	y1 = 400
	dx = abs(x1 - x0)
	dy = abs(y1 - y0)
	if(dx >= dy):
		bx(x0,y0,x1,y1,dx,dy)
	else:
		by(x0,y0,x1,y1,dx,dy)
	glFlush()

def main():
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(640,480)
	glutInitWindowPosition(50,50)
	glutCreateWindow(b'Plot Points')
	glutDisplayFunc(bressenham)



	init()
	glutMainLoop()

main()
