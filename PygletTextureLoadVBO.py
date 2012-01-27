# PygletTextureLoadVBO.py
# By Mark Szymczyk

# This example loads a texture and draws it on the screen.
# It uses OpenGL vertex buffer objects (VBOs) for drawing. To use a different image,
# add it to the same folder as this script and change the name
# from Background.png to the name of your image file.

import pyglet
from pyglet.gl import *
import pyglet.media
from ctypes import pointer, sizeof

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

# Create the arrays for the vertices and texture coordinates.
backgroundVertices = [
	0, 0,
	window.width, 0,
	window.width, window.height,
	0, window.height]
backgroundVerticesGL = (GLfloat * len(backgroundVertices))(*backgroundVertices)

backgroundTextureCoordinates = [
	0, 1,
	1, 1,
	1, 0,
	0, 0]
backgroundTextureCoordinatesGL = (GLfloat * len(backgroundTextureCoordinates))(*backgroundTextureCoordinates)

# Set up the VBO
theVBO = GLuint()
glGenBuffers(1, pointer(theVBO))
glBindBuffer(GL_ARRAY_BUFFER, theVBO)
arraySize = sizeof(backgroundVerticesGL) + sizeof(backgroundTextureCoordinatesGL)
glBufferData(GL_ARRAY_BUFFER, arraySize, 0, GL_STATIC_DRAW)

# Fill the VBO with the data from the arrays
glBufferSubData(GL_ARRAY_BUFFER, 0, sizeof(backgroundVerticesGL), backgroundVerticesGL)
glBufferSubData(GL_ARRAY_BUFFER, sizeof(backgroundVerticesGL), sizeof(backgroundTextureCoordinatesGL), backgroundTextureCoordinatesGL)

# Set up the vertices and texture coordinates for drawing.
glEnableClientState(GL_VERTEX_ARRAY)
# The second zero means the vertex data starts at the beginning of the VBO.
glVertexPointer(2, GL_FLOAT, 0, 0)

glEnableClientState(GL_TEXTURE_COORD_ARRAY)
# The texture coordinate data starts after the vertex data in the VBO.
glTexCoordPointer(2, GL_FLOAT, 0, sizeof(backgroundVerticesGL))

@window.event
def on_draw():
	draw_background()
	
def draw_background():
	glClear(GL_COLOR_BUFFER_BIT)
	# A texture-mapped quad has 4 vertices.
	glDrawArrays(GL_QUADS, 0, 4)


pyglet.app.run()