# -*- coding: utf-8 -*-

import turtle

def main():
    Window = turtle.Screen()
    dave = turtle.Turtle()

    make_rectangle(dave)

def make_rectangle(dave):
    #raw_input()
    make_line_and_turn(dave, 100)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()