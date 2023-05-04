import turtle
import random


def tree(branch_len, t):
    if branch_len > 5:
        t.pensize(branch_len//10)
        t.color("brown")
        if branch_len < 25:
            t.color("green")
        len_short = branch_len
        len_long = (branch_len * 1.25)//1
        rand_len = random.randrange(len_short, len_long)
        rand_angle = random.randrange(15, 45)
        t.forward(branch_len)
        t.right(rand_angle)
        tree(rand_len - 15, t)
        t.left(rand_angle*2)
        tree(rand_len - 15, t)
        t.right(rand_angle)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(0)
    tree(100, t)
    my_win.exitonclick()


main()
