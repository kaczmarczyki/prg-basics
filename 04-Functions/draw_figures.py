import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# figures.draw_square(100)
# figures.draw_trangle(80)
figures.draw_rectangle(100,50)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
