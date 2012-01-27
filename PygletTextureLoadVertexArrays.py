# PygletTextureLoadVertexArrays.py
# By Mark Szymczyk

# This example loads a texture and draws it on the screen.
# It uses OpenGL vertex arrays for drawing. To use a different image,
# add it to the same folder as this script and change the name
# from Background.png to the name of your image file.

import pyglet
from pyglet.gl import *
import pyglet.media

# Create the window for OpenGL drawing
config = pyglet.gl.Config(double_buffer=True, depth_size = 32)
window = pyglet.window.Window(config=config)

# Load the background
background = pyglet.resource.image('Background.png')
texture = background.get_texture();

# Set up the texture.
glEnable(GL_TEXTURE_2D)
glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
glBindTexture(GL_TEXTURE_2D, texture.id)

# Create the vertex arrays
backgroundVertices = [
	0, 0,
	window.width, 0,
	window.width, window.height,
	0, window.height]
backgroundVerticesGL = (GLfloat * len(backgroundVertices))(*backgroundVertices)
glEnableClientState(GL_VERTEX_ARRAY)
# A 2D vertex has two components: x and y.
glVertexPointer(2, GL_FLOAT, 0, backgroundVerticesGL)

# Create the texture coordinate arrays
backgroundTextureCoordinates = [
	0, 1,
	1, 1,
	1, 0,
	0, 0]
backgroundTextureCoordinatesGL = (GLfloat * len(backgroundTextureCoordinates))(*backgroundTextureCoordinates)
glEnableClientState(GL_TEXTURE_COORD_ARRAY)
# A texture coordinate has two components: u and v.
glTexCoordPointer(2, GL_FLOAT, 0, backgroundTextureCoordinatesGL)

@window.event
def on_draw():
	draw_background()
	
def draw_background():
	glClear(GL_COLOR_BUFFER_BIT)
	# A texture-mapped quad has 4 vertices.
	glDrawArrays(GL_QUADS, 0, 4)


pyglet.app.run()