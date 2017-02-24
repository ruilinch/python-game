import simplegui

# define globals
task_list = []

# define event handler
def add_task(inp):
    task_list.append(inp)
    
def delete_task_number(inp):
    num = int(inp)
    if num > 0 and num <= len(task_list)+1:
        task_list.pop(num-1)

def delete_task_name(inp):
    if inp in task_list:
        task_list.remove(inp)
    
def draw(canvas):
    text_position = [25, 25]
    text_num = 1
    for task in task_list:
        text_message = str(text_num)+" : "+task
        canvas.draw_text(text_message, text_position, 25, "White")
        text_position[1] = text_position[1] + 25
        text_num += 1
    
# define frame
frame = simplegui.create_frame("Task Management", 500, 500)

# register handler functions
frame.set_draw_handler(draw)
frame.add_input("Enter a new task", add_task, 150)
frame.add_input("Delete task number", delete_task_number, 150)
frame.add_input("Delete task name", delete_task_name, 150)

# start frame
frame.start()