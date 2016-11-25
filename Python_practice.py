# we can run 'simplegui' in CodeSkulptor(http://www.codeskulptor.org/)
'''
'rock spock paper lizard scissors' game
'''


def rpsls(name):
    print''
    player_number = name_to_number(name)
    import random
    computer_number = random.randrange(0, 5)
    computer_name = number_to_name(computer_number)
    print"Player chooses ", name
    print"Computer chooses", computer_name
    n = (player_number - computer_number) % 5
    if n == 0:
        print "Nobody wins!"
    elif n >= 3:
        print "Computer wins!"
    else:
        print "Player wins!"


def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print"input incorrect name"
        return None
    return number


def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print"input incorrect number"
        return None
    return name


rpsls('paper')

#################################################################
'''
gusee the number
'''
# input will come from bottons and an input field
# all output in the game will be printed in the console
import simplegui
# we can import simplegui in CodeSkulptor
import math
import random

# initialize global variables used in your code
high = 100
low = 0


# helper function to initial game
def new_game():
    # define event handlers for control panel
    global secret_number, low, high, rem
    secret_number = random.randrange(low, high)
    rem = int(math.ceil(math.log(high - low + 1, 2)))
    print "New game. Range is from " + str(low) + " to " + str(high)
    print"Number of remaining guesses is " + str(rem) + "\n"


def range100():
    # button that changes range to range [0,100) and restarts
    global high
    high = 100
    new_game()


def range1000():
    # button that changes range to range [0,1000) and restarts
    global high
    high = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    print "Guess was", guess
    global secret_number, rem
    input_number = int(guess)
    rem = rem - 1
    print"Number of remaining guesses is", rem

    if rem != 0:
        if input_number > secret_number:
            print "Lower\n"
        elif input_number < secret_number:
            print "Higher\n"
        else:
            print "Correct\n"
    else:
        print"You run out of guesses. The number was ", secret_number


# create window(s)
f = simplegui.create_frame("Guess the number", 200, 200)

# create control elements for window
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
# always remember to check your completed program against the grading rubric


########################################################
# first example if drawing on the canvas:
import simplegui


# define drawhandler

def draw(canvas):
    canvas.draw_text("Hello!", [100, 100], 24, "White")
    canvas.draw_circle([100, 100], 2, 2, "Red")


# creat frame
frame = simplegui.create_frame("Test", 300, 200)

# register drawhandler
frame.set_draw_handler(draw)

# start frame
frame.start()


################################################################
# handle single quantity
def convert_units(val, name):
    val = int(val)
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result


# convert xx.yy to xx dollars and yy cents
def convert(val):
    # split into dollars and cents
    dollars = int(val)
    cents = round(100 * (val - dollars))

    # convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string


# tests
print convert(11.23)
print convert(12.01)
print convert(1.12)
print convert(0.15)
print convert(0.0)

#######################################################################
# interactive application to convert a float in dollars and cents
import simplegui

# define a global value
value = 3.12


# handle single quantity
def convert_units(val, name):
    val = int(val)
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result


# convert xx.yy to xx dollars and yy cents
def convert(val):
    # split into dollars and cents
    dollars = int(val)
    cents = round(100 * (val - dollars))

    # convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string


# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value), [60, 100], 24, "White")


# define an input field handler
def input_handler(text):
    global value
    value = float(text)


# create frame
frame = simplegui.create_frame("Coverter", 400, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_input("Enter value", input_handler, 100)

# start frame
frame.start()

##############################################################
# Simple "screensaver" program.

# import modules
import simplegui
import random

# Global state
message = "Python is fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000


# handler for text box
def update(text):
    global message
    message = text


# handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y


# handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")


# create a frame
frame = simplegui.create_frame("Home", width, height)

# register event handlers
text = frame.add_input("Message", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
timer.start()

###############################################################
# draw a circle and change it
import simplegui

size = 10
radius = 10


# define event handlers

def incr_button_handler():
    """increment the size."""
    global size
    size += 1
    label.set_text("Value: " + str(size))


def decr_button_handler():
    """decrement the size."""
    global size
    if size > 0:
        size -= 1
        label.set_text("Value: " + str(size))


def change_circle_handler():
    """change the circle radius."""
    global radius
    radius = size
    label_values.set_text("Radius:" + str(radius))


def draw_handler(canvas):
    """draw the circle"""
    canvas.draw_circle([100, 100], radius, 5, "Red")


# create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 200, 200)
label = frame.add_label("Value: " + str(size))
frame.add_button("Increase", incr_button_handler)
frame.add_button("Decrease", decr_button_handler)
label_values = frame.add_label("Radius:" + str(radius))
frame.add_button("Change circle", change_circle_handler)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

#############################################################
# template for "Stopwatch: the Game"
import simplegui

# define global variables
tick = 0
win = 0
total = 0


# counting tenths of seconds into formatted string A:BC.D
def format(t):
    A = str(t // 600)
    BC = str((t % 600) // 100) + str((t % 100) // 10)
    D = str(t % 10)
    return A + ":" + BC + "." + D


# define event handlers for buttons: "Start""Stop""Reset"
def Start_handler():
    timer.start()


def Stop_handler():
    global win, total
    if timer.is_running():
        timer.stop()
        total += 1
        if (tick % 10) == 0 and tick != 0:
            win += 1


def Reset_handler():
    global win, total, tick
    win = 0
    total = 0
    tick = 0


# define timer handler
def timer_handler():
    global tick
    tick += 1


# define draw handlers
def draw_handler(canvas):
    canvas.draw_text(format(tick), [150, 100], 40, "White")
    canvas.draw_text(str(win) + '/' + str(total), [310, 30], 30, "Green")


# create frame and timer
frame = simplegui.create_frame("Stopwatch: the Game", 400, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", Start_handler, 100)
frame.add_button("Stop", Stop_handler, 100)
frame.add_button("Reset", Reset_handler, 100)

# start frame and timer
frame.start()
# remember to review the grading rubric


##################################################
# Ball motion with an implicit timer
import simplegui

# initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 1]  # pixels per update (1/60) seconds


# define event handlers
def draw(canvas):
    # update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")


# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handler
frame.set_draw_handler(draw)
# start frame
frame.start()

########################################################
# control the velocity of a ball using the arrow keys  

import simplegui

# Initialize globals  
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
Vel = [-3, 1]
color = "Brown"


# define event handlers  
def draw(canvas):
    global color
    # update ball positon
    ball_pos[0] += Vel[0]
    ball_pos[1] += Vel[1]

    # collide and reflect off of left
    if ball_pos[0] <= BALL_RADIUS:
        Vel[0] = -Vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        Vel[0] = -Vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        Vel[1] = -Vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        Vel[1] = -Vel[1]
        # draw ball  
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, color, color)
    # draw text
    canvas.draw_text("Current Velocity:" + str(Vel), [20, 30], 15, "White")


def keydown(key):
    acc = 1

    if key == simplegui.KEY_MAP["left"]:
        Vel[0] -= acc
    elif key == simplegui.KEY_MAP["right"]:
        Vel[0] += acc
    elif key == simplegui.KEY_MAP["up"]:
        Vel[1] -= acc
    elif key == simplegui.KEY_MAP["down"]:
        Vel[1] += acc


    # create frame


frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers  
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# frame start
frame.start()

###############################################################
'''
create a game Pong
'''
# implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = 0
RIGHT = 1

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors sorted as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(2, 4), random.randrange(1, 3)]
    if direction == 0:
        ball_vel[0] = - ball_vel[0]

    # define event handlers


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(random.randrange(-1, 1))


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, HEITGHT, HALF_PAD_HEIGHT

    # draw middle line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # reflection if the ball hits the up or down sides
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    # if the ball hits the gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT)) and (ball_pos[1] >= (paddle1_pos[1] - HALF_PAD_HEIGHT)):
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball(1)
            score2 += 1
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if (ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT)) and (ball_pos[1] >= (paddle2_pos[1] - HALF_PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0]
        else:
            spawn_ball(0)
            score1 += 1

            # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Yellow", "Yellow")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] >= HALF_PAD_HEIGHT and paddle1_pos[1] <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    else:
        paddle1_vel = 0

    if paddle2_pos[1] >= HALF_PAD_HEIGHT and paddle2_pos[1] <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    else:
        paddle2_vel = 0

    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT],
                     [paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT],
                     [paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2 - 100, HEIGHT / 5], 24, "White")
    canvas.draw_text(str(score2), [WIDTH / 2 + 100, HEIGHT / 5], 24, "White")


def keydown(key):
    global paddle1_vel, paddle2_vel
    original_vel = 2

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = - original_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = original_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = - original_vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = original_vel


def keyup(key):
    global paddle1_vel, paddle2_vel

    if (key == simplegui.KEY_MAP["w"]) or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif (key == simplegui.KEY_MAP["up"]) or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

button = frame.add_button('Restart', new_game, 180)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()

###################################################################
# Examples of mouse input_create a ball
import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
ball_color = "Red"


# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# define event handler for mouse click, draw
def click(pos):
    global ball_pos, ball_color
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Green"
    else:
        ball_pos = list(pos)
        ball_color = "Red"


def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Black", ball_color)


# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()


##################################################################
# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count


def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False


def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)


def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))

    for idx in remove:
        numbers.pop(idx)


def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)

    for num in remove:
        numbers.remove(num)


def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums


def remove_last_odd(numbers):
    has_odd = False
    last_odd = []
    count = 0
    for num in numbers:
        if num % 2 == 1:
            has_odd = True
            last_odd.append(num)
            count += 1
    if has_odd:
        numbers.reverse()
        numbers.remove(last_odd.pop(count - 1))
        numbers.reverse()


def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd(numbers)
    print numbers


run()

##########################################################
# Simple task list

import simplegui

tasks = []


# Handler for button
def clear():
    global tasks
    tasks = []


# Handler for new task
def new(task):
    tasks.append(task)


# Handler for remove number
def remove_num(tasknum):
    n = int(tasknum)
    if n > 0 and n <= len(tasks):
        tasks.pop(n - 1)


# Handler for remove name
def remove_name(taskname):
    if taskname in tasks:
        tasks.remove(taskname)


# Handler to draw on canvas
def draw(canvas):
    n = 1
    for task in tasks:
        pos = 30 * n
        canvas.draw_text(str(n) + ": " + task, [5, pos], 24, "White")
        n += 1


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Task List", 600, 400)
frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_name, 200)
frame.add_button("Clear All", clear)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

################################################################
# Cipher
import simplegui

CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}

message = ""


# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg


# Decode button
def decode():
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg


# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)

# Start the frame animation
frame.start()

################################################################
# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)


# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image,
                      [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT],
                      [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])

    # Draw magnifier    
    map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    mag_center = mag_pos
    mag_rectangle = [MAG_SIZE, MAG_SIZE]
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)


# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# Start frame
frame.start()

############################################################
# create balls and change color
import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15


# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# define event handler for mouse click, draw
def click(pos):
    changed = False
    for ball in ball_list:
        if distance([ball[0], ball[1]], pos) < ball_radius:
            ball[2] = "Green"
            changed = True

    if not changed:
        ball_list.append([pos[0], pos[1], "Red"])


def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle(ball[0], ball[1], ball_radius, 1, "Black", ball[2])


# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

#############################################################################
# create balls remove them
import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"


# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# define event handler for mouse click, draw
def click(pos):
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            remove.append(ball)

    if remove == []:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))


def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle(ball[0], ball[1], ball_radius, 1, "Black", ball_color)


# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

###################################################################################
'''
practice how to use class 
'''


class Character:
    def __init__(self, name, initial_health):
        self.name = name
        self.health = initial_health
        self.inventory = []

    def __str__(self):
        s = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s

    def grab(self, item):
        self.inventory.append(item)

    def get_health(self):
        return self.health


def example():
    me = Character("Bob", 20)
    print str(me)
    me.grab("pencil")
    me.grab("pen")
    print str(me)
    print "Health:", me.get_health()


example()


###################################################################################
# Object creation and use
# Mutation with Aliasing

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, newx):
        self.x = newx

    def get_x(self):
        return self.x


p = Point1(4, 5)
q = Point1(4, 5)
r = p

p.set_x(10)

print p.get_x()
print q.get_x()
print r.get_x()


# Object shared state
# Mutation of shared state

class Point2:
    def __init__(self, coordinates):
        self.coords = coordinates

    def set_coord(self, index, value):
        self.coords[index] = value

    def get_coord(self, index):
        return self.coords[index]


coordinates = [4, 5]
p = Point2(coordinates)
q = Point2(coordinates)
r = Point2([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)


# Objects not sharing state

class Point3:
    def __init__(self, coordinates):
        self.coords = list(coordinates)

    def set_coord(self, index, value):
        self.coords[index] = value

    def get_coord(self, index):
        return self.coords[index]


coordinates = [4, 5]
p = Point3(coordinates)
q = Point3(coordinates)
r = Point3([4, 5])

p.set_coord(0, 10)

print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)

###################################################################################
# Particle class example used to simulate diffusion of molecules

import simplegui
import random

# global constants
WIDTH = 600
HEIGHT = 400
PARTICLE_RADIUS = 5
COLOR_LIST = ["Red", "Green", "Blue", "White"]
DIRECTION_LIST = [[1, 0], [0, 1], [-1, 0], [0, -1]]


# definition of Particle class
class Particle:
    # initializer for particles
    def __init__(self, position, color):
        self.position = position
        self.color = color

    # method that updates position of a particle    
    def move(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]

    # draw method for particles
    def draw(self, canvas):
        canvas.draw_circle(self.position, PARTICLE_RADIUS, 1, self.color, self.color)

    # string method for particles
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color


# draw handler
def draw(canvas):
    for p in particle_list:
        p.move(random.choice(DIRECTION_LIST))

    for p in particle_list:
        p.draw(canvas)


# create frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particles
particle_list = []
for i in range(100):
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(COLOR_LIST))
    particle_list.append(p)

# start frame
frame.start()

###################################################################################
'''
game memory
'''
import simplegui
import random

num = []
n = 8

click1 = 0
click2 = 0
turns = 0
exposed = []


# helper function to initialize globals
def new_game():
    global num, exposed, turns, state, n
    state = 0
    turns = 0
    num = range(0, 2 * n)
    exposed = [False for i in range(2 * n)]
    random.shuffle(num)
    pass


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, click1, click2, turns, num
    choice = int(pos[0] / 50)
    if state == 0:
        state = 1
        click1 = choice
        exposed[click1] = True
    elif state == 1:
        if not exposed[choice]:
            state = 2
            click2 = choice
            exposed[click2] = True
            turns += 1
    elif state == 2:
        if not exposed[choice]:
            if num[click1] == num[click2]:
                pass
            else:
                exposed[click1] = False
                exposed[click2] = False
            click1 = choice
            exposed[click1] = True
            state = 1
    pass


# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text("Turns = " + str(turns))
    for i in range(2 * n):
        if exposed[i]:
            canvas.draw_text(str(num[i]), (50 * i + 10, 60), 40, "White")
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * i, 100), (50 * i + 50, 100),
                                 (50 * i + 50, 0)],
                                1, "White", "Grey")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game, 150)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
# Always remember to review the grading rubric
