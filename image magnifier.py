import simplegui

image = simplegui.load_image("http://pic20.nipic.com/20120419/7258806_091554035378_2.jpg")
image_width = image.get_width()
image_height = image.get_height()
IMAGE_SCALE = 3
frame_size = [image_width/IMAGE_SCALE, image_height/IMAGE_SCALE]

mag_pos = [frame_size[0]/2, frame_size[1]]
mag_size = [100, 100]

def multiply_vector(p1, v):
    """one vector p1, one double v
    multiply each elements of the p1 by v
    """
    p = [p1[0]*v, p1[1]*v]
    return p
    

def draw(canvas):
    canvas.draw_image(image, 
                        (image_width/2, image_height/2), (image_width, image_height),
                        (frame_size[0]/2, frame_size[1]/2), (frame_size[0], frame_size[1]))
                        
                        
    mag_original_pos = multiply_vector(mag_pos, IMAGE_SCALE)
    canvas.draw_image(image, mag_original_pos, mag_size, mag_pos, mag_size)

def click(pos):
    global mag_pos
    mag_pos = list(pos)
    
frame = simplegui.create_frame("Image Magnifier", frame_size[0], frame_size[1])

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()