import simplegui
import random

# define globals
# keyboard control values
key_value = [38, 40] # system values for directional arrows
key_name = ['left', 'up','right','down'] 

key = 0

# frame parameters
frame_size = [600, 400]

# paddle parameters
paddle_width = 10
paddle_height = 40
paddle_shift_size = 10

paddle_northwest_point = 0 # draw the paddle based on its northwest point

# ball parameters
ball_radius = 10
ball_shift_size = 10

ball_vector = [-1, -1]
ball_pos = [frame_size[0]/2, frame_size[1]/2]
ball_time = 0

# the time that left player has lost
time_lose = 0


# define vector calculation
def add_vector(p1, p2):
    """Add two-dimensional vectors p1, p2 and return a new vector"""
    p = [p1[0]+p2[0], p1[1]+p2[1]]
    return p    

def multiply_vector(p1, v):
    """one vector p1, one double v
    multiply each elements of the p1 by v
    """
    p = [p1[0]*v, p1[1]*v]
    return p

# define helper functions
def ball_collision():
    """determine if the player lost the game when the ball hits the left side of the border"""
    global ball_vector, time_lose, ball_shift_velocity
    if ball_pos[0] <= paddle_width + ball_radius:
        ball_vector[0] = - ball_vector[0]
        if ball_pos[1] - paddle_northwest_point <= ball_radius or ball_pos[1] - paddle_northwest_point >= paddle_height + ball_radius:
            time_lose += 1
            ball_shift_size = 10
        else:
            pass

def ball_reflection():
    """change the ball_vector if the ball hits the upper/lower and right side of the boarder"""
    global ball_vector
    if ball_pos[1] <= ball_radius or ball_pos[1] >= frame_size[1] - ball_radius:
        ball_vector[1] = - ball_vector[1]
    elif ball_pos[0] >= frame_size[0] - ball_radius:
        ball_vector[0] = - ball_vector[0]               

# define draw handler
def draw(canvas):
    canvas.draw_line([frame_size[0]/2,0],[frame_size[0]/2, frame_size[1]],2, "White")
    canvas.draw_line([paddle_width,0], [paddle_width, frame_size[1]],2, "White")
    canvas.draw_polygon([[0, paddle_northwest_point],[paddle_width, paddle_northwest_point], [paddle_width, paddle_height+paddle_northwest_point], [0, paddle_height+paddle_northwest_point]], 2, "White", "White")
    canvas.draw_circle(ball_pos, ball_radius, 1, "Black", "White")
    canvas.draw_text(str(time_lose),[frame_size[0]/2-30, 30], 30,"White")

# define keyup and keydown handler
def paddle_shift(inp):
    """allow one press and presses of longer duration"""
    global key
    key = int(inp)
    if key == 38 or key == 40:
        paddle_timer.start()
        paddle_tick()
    else:
        pass

def stop_paddle_shift(inp):
    """control presses of longer duration"""
    global key
    key = int(inp)
    if key == 38 or key == 40:
        paddle_timer.stop()
    else:
        pass
        
# define timer handler
def paddle_tick():
    """belong to the package allowing presses of longer duration"""
    global paddle_northwest_point
    if key == 38:
        if paddle_northwest_point >= paddle_shift_size:
            paddle_northwest_point -= paddle_shift_size
        else:
            paddle_northwest_point = 0
    elif key == 40:
        if paddle_northwest_point <= frame_size[1] - paddle_height - paddle_shift_size:
            paddle_northwest_point += paddle_shift_size
        else:
            paddle_northwest_point = frame_size[1] - paddle_height
    else:
        pass
        
def ball_tick():
    """define ball movement based on timer"""
    global ball_pos, ball_time, ball_shift_size
    ball_time += 1
    if ball_time % 100 == 0:
        ball_shift_size += 5
    ball_pos = add_vector(ball_pos, multiply_vector(ball_vector,ball_shift_size))
    ball_collision()
    ball_reflection()        
        
# define frame
frame = simplegui.create_frame("Pong", frame_size[0], frame_size[1])
paddle_timer = simplegui.create_timer(100, paddle_tick)
ball_timer = simplegui.create_timer(200, ball_tick)

# register handler functions
frame.set_draw_handler(draw)
frame.set_keydown_handler(paddle_shift)
frame.set_keyup_handler(stop_paddle_shift)


# start frame
frame.start()
ball_timer.start()