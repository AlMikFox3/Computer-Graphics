#include <iostream>
#include <GL/glut.h>
#include <math.h>
using namespace std;

int xc,yc,r;

float round_value(int v)
{
	return v;
}

void Init()
{
	glClearColor(1.0,1.0,1.0,0);
	glColor3f(0.0,0.0,0.0);
	gluOrtho2D(-640, 640, -480, 480);
}

void drawReflectedPoints(int x, int y)
{
	glBegin(GL_POINTS);
	glVertex2i(round_value(y), round_value(x));
	glVertex2i(round_value(y), round_value(-x));
	glVertex2i(round_value(x), round_value(-y));
	glVertex2i(round_value(-x), round_value(y));
	glVertex2i(round_value(-y), round_value(x));
	glVertex2i(round_value(-x), round_value(-y));
	glVertex2i(round_value(-y), round_value(-x));
	glEnd();
}

void plot(int x, int y)
{
	glBegin(GL_POINTS);
	glVertex2i(x+xc, y+yc);
	glEnd();
}

void MPC(void)
{
	int x = 0;
	int y = r;
	float d = (5/4)-r;
	glClear(GL_COLOR_BUFFER_BIT);
	glPointSize(1.0);
	glBegin(GL_POINTS);
	while(x<y)
	{
		plot(x,y);
		//drawReflectedPoints(x+xc, y+yc);
		
		plot(x, y);
		plot(x, -y);
		plot(-x, y);
		plot(-x, -y);
		plot(y, x);
		plot(-y, x);
		plot(y, -x);
		plot(-y, -x);
		if(d<0)
			d = d + (2*x) + 3;
		else{
			d = d + 2*(x-y) + 5;
			y = y-1;
		}
		x = x+1;

	}


  	glFlush();
}

int main(int argc, char **argv)
{
	cin>>xc>>yc>>r;
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition(0,0);
	glutInitWindowSize(640,480);
	glutCreateWindow("Midpoint Circle Algorithm");
	Init();
	glutDisplayFunc(MPC);
	glutMainLoop();
	return 0;	
}

