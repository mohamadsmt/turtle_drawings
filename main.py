import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.pencolor('white')
t.speed(0)
a = 0
b = 0

# t.penup()
# t.goto(0, 200)
# t.pendown()
# while True:
#     t.forward(a)
#     t.right(b)
#     a += 3
#     b += 1
#     if b == 210:
#         break
#     t.hideturtle()

# while True:
#     for i in range(4):
#         t.forward(80)
#         t.right(90)
#     t.right(15)
#     a += 1
#     if a >= 390/15:
#         t.forward(50)
#         a = 0
#         b += 1
#         if b >= 12:
#             break
# t.hideturtle()

t.left(90)
def draw(n):
    if n < 10:
        return
    else:
        t.forward(n)
        t.left(30)
        draw(3*n/4)
        t.right(60)
        draw(3*n/4)
        t.left(30)
        t.backward(n)
draw(100)



turtle.done()

