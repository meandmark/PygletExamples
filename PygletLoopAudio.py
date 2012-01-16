# PygletLoopAudio.py
# By Mark Szymczyk

# This example builds upon the PygletTextureLoadImmediate sample
# by playing looping background music. The background music in this
# example is an MP3 file. Make sure you install the AVbin library or
# else you will not be able to run this example. To use a different music
# file, add it to the same folder as this script and change the name of
# the file from Music.mp3 to the name of your file.

import pyglet
from pyglet.gl import *
import pyglet.media.avbin
import pyglet.media

# Create the window for OpenGL drawing
config = pyglet.gl.Config(double_buffer=True, depth_size = 32)
window = pyglet.window.Window(config=config)

# Load the background
background = pyglet.resource.image('Background.png')
texture = background.get_texture();
glBindTexture(texture.target, texture.id)

# Set up the texture.
glEnable(GL_TEXTURE_2D)
glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
glBindTexture(GL_TEXTURE_2D, texture.id)

# Loop the background music
player = pyglet.media.Player()
player.queue(pyglet.media.load('Music.mp3'))
player.eos_action = 'loop'
player.play()


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