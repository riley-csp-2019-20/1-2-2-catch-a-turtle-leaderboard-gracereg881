# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb 

#-----game configuration---- # define shape, size, color
shape = "turtle"
size = 5
color = "limegreen"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name:")


#-----initialize turtle----- # events
jack = trtl.Turtle(shape = shape)
jack.color(color)
jack.shapesize(size)
jack.speed(0)
counter =  trtl.Turtle()


score_writer = trtl.Turtle()
# this is one of my customizations where I customized the score writer
score_writer.pencolor("lightgreen")
score_writer.shape("turtle")
score_writer.penup()
score_writer.goto(-370,270)
font = ("Arial" , 50 , "bold")
score_writer.write(score, font = font)


#-----game functions-------- #
def turtle_clicked(x,y):
    print("jack was clicked!")
    change_position()
    score_counter()

def change_position():
    jack.penup()
    jack.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    jack.goto(new_xpos, new_ypos)
    jack.st()

def score_counter():
    global score
    score+=1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font)

def countdown():
    global timer, timer_up
    counter.up()
    counter.goto(250, 320)
    counter.down()
    counter.clear()
    if timer <= 0:
        counter.up()
        counter.goto(0,0)
        counter.write("Time's Up!", font=font_setup)
        timer_up = True
        manage_leaderboard()
        
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

def game_over():
    # this is a customization I have where I made the background a specific color
    wn.bgcolor("teal")
    jack.ht()
    jack.goto(500,500)
    counter.goto(0,0)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global jack

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, jack, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, jack, score)


    


#-----events----------------
jack.onclick(turtle_clicked)

wn=trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()