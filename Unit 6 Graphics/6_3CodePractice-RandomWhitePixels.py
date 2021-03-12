import simplegui
import random

def draw_handler(canvas):
    canvas.draw_point([1000, 1000], "White")


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
