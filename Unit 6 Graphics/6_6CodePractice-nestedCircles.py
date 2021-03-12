import simplegui

w = 300
h = 300

def draw_handler(canvas):
    canvas.draw_circle((w, h), 250, 5, "Green")
    canvas.draw_circle((w, h), 200, 5, "Green")
    canvas.draw_circle((w, h), 150, 5, "Green")
    canvas.draw_circle((w, h), 100, 5, "Green")
    canvas.draw_circle((w, h), 50, 5, "Green")


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
