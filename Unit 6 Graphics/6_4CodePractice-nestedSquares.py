import simplegui

def draw_handler(canvas):
    canvas.draw_polygon([(0, 0), (0, 400), (400, 400), (400, 0)], 2.5, "Black")
    canvas.draw_polygon([(50, 50), (50, 350), (350, 350), (350, 50)], 2.5, "Black")
    canvas.draw_polygon([(100, 100), (100, 300), (300, 300), (300, 100)], 2.5, "Black")
    canvas.draw_polygon([(150, 150), (150, 250), (250, 250), (250, 150)], 2.5, "Black")


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
