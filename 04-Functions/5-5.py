###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

# Draw figures
figures.draw_square(100)
figures.move_to(-200,0)
figures.draw_square(100)
figures.move_to(100,0)
figures.draw_rectangle(100,300)
figures.move_to(-100, 0)
figures.draw_rectangle(100,300)
figures.move_to(-300,0)
figures.draw_rectangle(100,300)
figures.move_to(0,-100)
figures.draw_trangle(100)
figures.move_to(-200,-100)
figures.draw_trangle(100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
