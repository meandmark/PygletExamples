# PygletOpenGLIntro.py
# By Mark Szymczyk

# This is a simple example of setting up an OpenGL context in pyglet.
# It draws a purple rectangle in the lower left corner of the screen.

import pyglet
from pyglet.gl import *

# Create a double-buffered window with 32-bit color.
config = pyglet.gl.Config(double_buffer=True, depth_size = 32)
window = pyglet.window.Window(config=config)

# Draw the rectangle.
@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.7, 0.5, 0.8)
	glRectf(0.0, 0.0, (window.width / 2), (window.height / 2))

pyglet.app.run()