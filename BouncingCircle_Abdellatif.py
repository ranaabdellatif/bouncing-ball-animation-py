"""
Author: Rana Abdellatif 
Randomized Color Bouncing Ball
"""


from random import random
import dudraw
from dudraw import Color

# main code block:
dudraw.set_canvas_size(400,400)

# create values to represent circle's properties



class BouncingCircle:
    x_position = random()
    y_position = random()
    x_velocity = 0.05*random()
    y_velocity = 0.05*random()
    radius = 0.05
    color = Color(int(random()*256), int(random()*256), int(random()*256))

    def __init__(self, x_center= x_position, y_center = y_position, x_velocity = x_velocity, y_velocity = y_velocity, radius = radius):
        self.x_center = x_center
        self.y_center = y_center
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.radius = radius
    
    def move(self):
        self.x_center += self.x_velocity
        self.y_center += self.y_velocity

        if self.x_center > 1 or self.x_center < 0:
            self.x_velocity *= -1

        if self.y_center > 1 or self.y_center < 0:
                    self.y_velocity *= -1
    
    def draw(self):
        dudraw.show()

  #  def overlaps(BouncingCircle)->bool:
      #  if 


bc = BouncingCircle


# animation loop, continue until user types 'q'
key = ''
while key != 'q':
    # advance the circle to the next position:
    bc.x_position += bc.x_velocity
    bc.y_position += bc.y_velocity

    # bounce off the edges of the canvas if necessary:
    if (bc.x_position > 1-bc.radius and bc.x_velocity > 0 or 
        bc.x_position < bc.radius and bc.x_velocity < 0):
        bc.x_velocity *= -1

    if (bc.y_position > 1-bc.radius and bc.y_velocity > 0 or 
        bc.y_position < bc.radius and bc.y_velocity < 0):
        bc.y_velocity *= -1 

    # redraw the frame:
    dudraw.clear(dudraw.LIGHT_GRAY)

    # draw the circle at its new position
    dudraw.set_pen_color(bc.color)
    dudraw.filled_circle(bc.x_position, bc.y_position, bc.radius)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.circle(bc.x_position, bc.y_position, bc.radius)

    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()

    # display the new frame and pause for 1/20 of a second
    dudraw.show(50)   
    # dudraw.show(50)