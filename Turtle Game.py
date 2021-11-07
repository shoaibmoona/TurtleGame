#importing required modules and functions:
import turtle
from random import *
import time

# handling errors if any
try:

# Creating turtle screen

    turtle.title("Turtle Race-Designed By Shoaib") #Title of the game at the top of the window
    s=turtle.Screen()
    s.cv._rootwindow.resizable(False,False) #Disables user to resize the window.
    s.setup(700,700) #Screen/window size of the game.
    s.bgcolor("green") #Background color of the game window.
    turtle.penup()
    turtle.speed(0)
    turtle.goto(-100,250) # Placing heading at the top of the window
    turtle.write("Turtle Race- Bet on Turtle",align="center",font=("Arial",20,"bold")) #Heading

# Creating Dirt/ Chocolate color racing course

    turtle.setpos(-290,210)
    turtle.pendown()
    turtle.color("chocolate") #Fill the dirt ground with chocolate like brown  color
    turtle.begin_fill() #begin filling chocolate color
    turtle.forward(580) #Dirt ground creation (making a rectangle) move forward 580 pixels
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(400) # Move forward 400 pixels
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(580) # Move forward 580 pixels
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(400) # Move forward 400 pixels
    turtle.end_fill() #End filling chocolate color

# Finish line
    turtle.penup()
    turtle.shape("square") # Square shaped finish line
    turtle.color("white") # White colored Squares
# Loop to create Finish line squares
    for i in range(10):
        turtle.setpos(200,200-(i*20*2))
        turtle.stamp() # print the turtle shape (ie. White colored Square)
    for j in range(10):
        turtle.setpos(200+20,200-20-(j*20*2))
        turtle.stamp() # print the turtle shape (ie. White colored Square)
    turtle.pendown()

# Creating turtles
    # Turtle1
    turtle1 = turtle.Turtle()
    turtle1.speed(0)
    turtle1.shape("turtle")
    turtle1.color("yellow")
    turtle1.penup()
    turtle1.setpos(-250,0) # (x-axis, y-axis)
    turtle1.pendown()
    turtle1.pensize(3)

    # Turtle2
    turtle2 = turtle.Turtle()
    turtle2.speed(0)
    turtle2.shape("turtle")
    turtle2.color("pink")
    turtle2.penup()
    turtle2.setpos(-250,80) # (x-axis, y-axis)
    turtle2.pendown()
    turtle2.pensize(3)

    # Turtle3
    turtle3 = turtle.Turtle()
    turtle3.speed(0)
    turtle3.shape("turtle")
    turtle3.color("red")
    turtle3.penup()
    turtle3.setpos(-250,150) # (x-axis, y-axis)
    turtle3.pendown()
    turtle3.pensize(3)

    # Turtle4
    turtle4 = turtle.Turtle()
    turtle4.speed(0)
    turtle4.shape("turtle")
    turtle4.color("black")
    turtle4.penup()
    turtle4.setpos(-250,-80) # (x-axis, y-axis)
    turtle4.pendown()
    turtle4.pensize(3)
    
# Race
    line=180
    while turtle1.xcor() < line or turtle2.xcor() < line or turtle3.xcor() < line or turtle4.xcor() < line:
        turtle1.forward(randint(1,5))
        turtle2.forward(randint(1,5))
        turtle3.forward(randint(1,5))
        turtle4.forward(randint(1,5))

# Decide ranking
    finals_list = [turtle1.xcor(),turtle2.xcor(),turtle3.xcor(),turtle4.xcor()]
    finals_dict = {turtle1.xcor():'Yellow', turtle2.xcor():'Pink', turtle3.xcor():'Red',turtle4.xcor():'Black'}
    finals_list = sorted(finals_list,reverse=True) 

# Ranking board
    turtle.hideturtle()
    turtle.penup() 
    turtle.color('Black')
    turtle.setposition(-250,-190)
    turtle.write('Ranking Board',align='left', font=("Arial",20,"bold"))

# 1st
    turtle.setposition(-270,-228)
    rank = finals_list[0]
    turtle.write(f'1st place: {finals_dict[rank]} Turtle',font=("Arial",15,"bold"))

# 2nd
    turtle.setposition(-270,-248)
    rank = finals_list[1]
    turtle.write(f'2nd place: {finals_dict[rank]} Turtle',font=("Arial",15,"bold"))

# 3rd
    turtle.setposition(-270,-268)
    rank = finals_list[2]
    turtle.write(f'3rd place: {finals_dict[rank]} Turtle',font=("Arial",15,"bold"))

# 4th
    turtle.setposition(-270,-288)
    rank = finals_list[3]
    turtle.write(f'4th place: {finals_dict[rank]} Turtle',font=("Arial",15,"bold"))
    
# Add a little pause (5 seconds pause)
    time.sleep(5) # Pause the game for few seconds when starting the game.
    
#Exit on click message
    turtle.setposition(110,-250)
    turtle.write("Click to Exit..",font=("Arial",17,"bold"))
    turtle.exitonclick() # Game exits on mouse click.
except Exception:
    print('Something went wrong..')
finally:
    print("Thanks for Playing Turtle Game!")
