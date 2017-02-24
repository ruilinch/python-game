import simplegui

poker_image = simplegui.load_image("http://pic20.nipic.com/20120419/7258806_091554035378_2.jpg")
poker_image_width = poker_image.get_width()
poker_image_height = poker_image.get_height()
card_width = poker_image_width / 13.0
card_height = poker_image_height / 4.0

frame_size = [200, 200]

    
def draw(canvas):
    
    card_center_width = rank_index * card_width + card_width/2.0 
    card_center_height = suit_index * card_height + card_height/2.0
        
    canvas.draw_image(poker_image, [card_center_width, card_center_height], [card_width, card_height],
                                    [frame_size[0]/2, frame_size[1]/2], [card_width, card_height])
                             
    
frame = simplegui.create_frame("Image Magnifier", frame_size[0], frame_size[1])

frame.set_draw_handler(draw)

frame.start()