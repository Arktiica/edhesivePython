import simplegui

top = 250
bot = 450
lef = 150
rig = 450

def draw_handler(canvas):
    # Top Left, Top Right, Bottom Right, Bottom Left
    canvas.draw_polygon([(lef, top), (rig, top), (rig, bot), (lef, bot)], 2.5, "Black") # House
    canvas.draw_polygon([(lef, top), (rig, top), ((rig + lef)/ 2, 100)], 2.5, "Black") # Roof
    canvas.draw_polygon([(lef + 50, top + 75), (rig - 200, top + 75), (rig - 200, bot), (lef + 50, bot)], 2.5, "Black")


frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("White")
frame.set_draw_handler(draw_handler)
frame.start()
