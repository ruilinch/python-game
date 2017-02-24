# Memory
import simplegui
import random

# define globals
num_of_pair = 8 # how many pairs of number will there be
frame_size = [1000, 200]
card_width = frame_size[0]/(num_of_pair * 2) # width of each card drawn on frame

card = [] # store card-related values ==> list
flipped_index = [] # related to mouse click
number = range(num_of_pair) * 2 # array of number pairs

num_attempt = 0
num_matched = 0
num_unmatched = num_of_pair - num_matched

# define helper functions
def gen_card():
    """generate a list storing card-related information
    including [0]the upper_left coordinate of the card polygon,
    [1]whether the card is flipped and [2]the number each card has"""
    global card, number, flipped_index
    random.shuffle(number)
    flipped_index = []
    card = []
    upper_left = 0
    for i in range(num_of_pair * 2):
        flipped = False
        num = number[i]
        card.append([upper_left, flipped, num])
        upper_left += card_width

# define click handler        
def click(pos):
    """determine which card the click picks and then store the card index in flipped_index
    if there are two clicks in a row, change these two cards' status into being flipped.
    if flipped_index has three/five/seven clicks stored, compare -2 and -3 card number
    if they are the same, find a matched pair
    else: pop them out from flipped_index and change the card status into not being flipped.
    """
    global card, flipped_index, num_attempt, num_matched, num_unmatched
    for square in card:
        if pos[0] > square[0] and pos[0] < square[0] + card_width:
            flipped_index.append(card.index(square))
        length = len(flipped_index)
    if length > 0 and length % 2 == 0: 
        card[flipped_index[-1]][1] = True
        card[flipped_index[-2]][1] = True 
        num_attempt += 1
        label_for_attempt.set_text("Total Attempts: " + str(num_attempt))
    elif length > 2 and length % 2 == 1:
        if (card[flipped_index[-2]][2] == card[flipped_index[-3]][2]):
            num_matched += 1
            num_unmatched -= 1
            label_for_matched.set_text("Number of Matched Pairs: " + str(num_matched))
            label_for_unmatched.set_text("Number of Unmatched Pairs: "+ str(num_unmatched))
        else:
            card[flipped_index[-2]][1] = False
            card[flipped_index[-3]][1] = False
            flipped_index.pop(length-2)
            flipped_index.pop(length-3)
        
# define draw handler        
def draw(canvas):
    """draw cards"""
    for square in card:
        plot = [[square[0], 0], [square[0]+card_width, 0],[square[0]+card_width, frame_size[1]],[square[0],frame_size[1]]]
        if square[1] == True:
            canvas.draw_polygon(plot, 4, "Black", "Black")
            canvas.draw_text(str(square[2]), [square[0]+card_width/2-30, frame_size[1]/2+30], 60, "White")
        else:
            canvas.draw_polygon(plot, 4, "Blue","Green")

# define restart button
def new_game():
    global num_attempt, num_matched, num_unmatched
    gen_card()
    num_attempt = 0
    num_matched = 0
    num_unmatched = num_of_pair - num_matched
    label_for_attempt.set_text("Total Attempts: " + str(num_attempt))
    label_for_matched.set_text("Number of Matched Pairs: " + str(num_matched))
    label_for_unmatched.set_text("Number of Unmatched Pairs: "+ str(num_unmatched))
       
# create a frame
frame = simplegui.create_frame("Memory", frame_size[0], frame_size[1])

# register handler functions
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("White")
frame.add_button("New Game", new_game, 100)

label_for_attempt = frame.add_label("Total Attempts: " + str(num_attempt))
label_for_matched = frame.add_label("Number of Matched Pairs: " + str(num_matched))
label_for_unmatched = frame.add_label("Number of Unmatched Pairs: "+ str(num_unmatched))

# start
frame.start()
gen_card()
