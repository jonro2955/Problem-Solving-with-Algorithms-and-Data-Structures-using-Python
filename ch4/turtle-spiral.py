import turtle


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


t = turtle.Turtle()
t.speed(0)
wn = turtle.Screen()
draw_spiral(t, 100)
wn.exitonclick()

