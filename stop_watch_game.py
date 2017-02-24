# the stop watch game
import simplegui

# define globals
num_stop = 0
num_win = 0
time = 0
message = "0:00.0"
tenth_second = 1

# define format function to process time
def format_time(inp):
    global message
    global tenth_second
    value = inp * 10
    second = int (value // 10)
    tenth_second = int(value % 10)
    
    # second to minute
    minute = second // 60
    second = second - minute * 60
    if (second // 10 == 0):
        message = str(minute) + ":0" + str(second) + "." + str(tenth_second)
    else:
        message = str(minute) + ":" + str(second) + "." + str(tenth_second)

    
# define handler function for timer
def tick():
    global time
    time = time + 0.1
    format_time(time)
   
def start_timer():
    timer.start()   
    
def stop_timer():
    global num_stop, num_win, tenth_second
    timer.stop()
    num_stop = num_stop + 1
    if (tenth_second == 0):
        num_win = num_win + 1
    else:
        num_win = num_win
    
def reset_timer():
    global time, num_stop, num_win, message
    time = 0
    num_stop = 0
    num_win = 0
    message = "0:00.0"
    timer.stop()

# define handler function for draw
def draw(canvas):
    canvas.draw_text(str(num_win) + "/" + str(num_stop), [190, 50], 36, "Green")
    canvas.draw_text(message, [60, 150], 80, "White")
    


# define frame
frame = simplegui.create_frame("Stop Watch Game", 300, 200)
timer = simplegui.create_timer(100, tick)

# register handler functions
frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_timer, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()