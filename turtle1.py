import turtle
from turtle import Turtle,Screen
import random
timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# # timmy.forward(100)
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for i in range(15):
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     timmy.pendown()

# colors = ["green", "blue", "pink", "yellow", "orange", "turquoise", "lime", "violet"]
# n = 11
# for i in range(3, n):
#     angle = ((i - 2) * 180) / i
#     sides = i
#     timmy.color(random.choice(colors))
#
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(180 - angle)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
#
#
# angles = [0, 90, 180, 270, 360]
# for i in range(100):
#     angle = random.choice(angles)
#     timmy.color(random_color())
#     timmy.width(20)
#     timmy.forward(40)
#     timmy.setheading(angle)
#     timmy.speed(40)

# method1
# timmy.speed("fastest")
# dist = 1
# for i in range(90):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.right(-4)
#     dist += 1

#method2
timmy.speed("fastest")
def draw_spiro(gap):
    for i in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap)

draw_spiro(1)


screen = Screen()
screen.exitonclick()