# PygletTextureLoadImmediate.py
# By Mark Szymczyk

# This example loads a texture and draws it on the screen.
# It uses immediate mode for drawing. To use a different image,
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


@window.event
def on_draw():
	draw_background()
	
def draw_background():
    
	# Draw the texture
	glBegin(GL_QUADS)
    
	# Lower left corner
	glTexCoord2f(0.0, 1.0)
	glVertex3f(0.0, 0.0, 0.0)
    
	# Lower right corner
	glTexCoord2f(1.0, 1.0)
	glVertex3f(window.width, 0.0, 0.0)
    
	# Upper right corner
	glTexCoord2f(1.0, 0.0)
	glVertex3f(window.width, window.height, 0.0)
    
	# Upper left corner
	glTexCoord2f(0.0, 0.0)
	glVertex3f(0.0, window.height, 0.0)
    
	glEnd()


pyglet.app.run()