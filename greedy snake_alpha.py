# create a keyboard motion
import simplegui

# define globals
# radius of the circle
radius = 20    
# the width and height of the frame
frame_size = [400, 400]  
# the location of the center point of the circle
center_position = [frame_size[0]/2, frame_size[1]/2]  
# the size of step motion
step_size = 10
# the system value assigned to each of the directional arrows
key_value = [37, 38, 39, 40] # 38-up; 40-down; 37-left; 39-right
key_name =['left','up','right','down']

time = 0 
key = 0
message = ""

# define event handlers
def shift(inp):
    """change the center location according to the value of inp by step_size"""
    global center_position
    if (inp in key_value):
        if (inp % 2 == 0):
            center_position[1] += (inp - key_value[2]) * step_size
        else:
            center_position[0] += (inp - key_value[1]) * step_size
    else:
        pass

def key_down(inp):
    """when the directional key is pressed down, change message and start timer"""
    global key, message
    key = inp
    for i in range(len(key_value)):
        if key == key_value[i]:
            message = key_name[i]
        else:
            pass
    

def tick():
    """After the timer is started, change the center location every 5 times"""
    global time, key
    if (time % 5 == 0):
        shift(key)
    time = time + 1
       
def draw(canvas):
    """direction instruction + timer + center location + circle"""
    canvas.draw_text(message, [frame_size[0]-70, 70], 24, "White")
    canvas.draw_text("Timer: "+str(time), [frame_size[0]-100, frame_size[1]-40],15, "Green")
    canvas.draw_text("[ "+str(center_position[0])+" , "+str(center_position[1])+" ]", [150, frame_size[1]-40], 24, "Yellow")
    canvas.draw_circle(center_position, radius, 4, "White","Red") 


# create frame and timer
frame = simplegui.create_frame("Keyboard Motion", frame_size[0], frame_size[1])
timer = simplegui.create_timer(50, tick)

# register handlers
frame.set_keydown_handler(key_down)
frame.set_draw_handler(draw)

# start
frame.start()
timer.start()