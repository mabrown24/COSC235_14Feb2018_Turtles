import turtle
'''
def draw_square(bob,size):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    for i in range(4):
      bob.forward (size)
      bob.left(90)
t= turtle.Turtle()
draw_square(80, 60,)
'''
def draw_triangle (mitch,side):
  colors = ['red', 'blue','green']
  for i in range (3):
    mitch.color(colors[i])
    mitch.forward(side)
    mitch.left(120)
  
def draw_spiral (jane): 
  for i in range(1,51):
    jane.forward(i)
    jane.left(20)

t=turtle.Turtle()
draw_triangle(t, 60)