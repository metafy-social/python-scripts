import turtle as t

t.bgcolor("black")
t.speed(0)
t.pensize(2)

colors=['red','yellow','blue','purple','green','#fe019a','black','white','red','yellow','blue','purple','green','#fe019a','black','white']

distance=170
t.hideturtle()

for color in colors:
  t.color(color)
  for j in range(8):
    t.left(45)
    for i in range (2):
      t.forward(distance)
      t.left(60)
      t.forward(distance)
      t.left(120)
t.done()
