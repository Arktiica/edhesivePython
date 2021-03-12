import simplegui

x = 50
y = 200

def draw_handler(canvas):
    global x
    global y
    color = "RGB(255,0,255)"
    
    x = x + 1
    if (x >= 1000):
        x = 1
    canvas.draw_circle([x, y], 50, 1, color, color)
    canvas.draw_circle([x, y + 50], 50, 1, color, color)
    canvas.draw_line((x - 10, y), (x - 10, y + 50), 5, "White")
    canvas.draw_line((x, y), (x, y + 50), 5, "White")
    canvas.draw_line((x + 10, y), (x + 10, y + 50), 5, "White")


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
