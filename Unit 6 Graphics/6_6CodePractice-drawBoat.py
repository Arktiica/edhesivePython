import simplegui

def draw_handler(canvas):
    canvas.draw_circle((0,500), 50, 1, "Blue")
    canvas.draw_circle((100, 500), 50, 1, "Blue")
    canvas.draw_circle((200, 500), 50, 1, "Blue")
    canvas.draw_circle((300, 500), 50, 1, "Blue")
    canvas.draw_circle((400, 500), 50, 1, "Blue")
    canvas.draw_circle((500, 500), 50, 1, "Blue")
    canvas.draw_circle((600, 500), 50, 1, "Blue")
    canvas.draw_line((0, 500 - 38), (600, 500 - 38), 78, "White")
    
    canvas.draw_circle((350, 475), 75, 5, "Black", "White")
    canvas.draw_line((0, 425,), (600, 425), 100, "White")
    canvas.draw_line((275, 475), (425, 475), 5, "Black")
    canvas.draw_line((350, 475), (350, 375), 5, "Black")
    canvas.draw_polygon([(350, 400), (350, 450), (400, 450)], 5, "Black")


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
