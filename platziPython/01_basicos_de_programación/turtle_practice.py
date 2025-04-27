import turtle


def main():
    window = turtle.Screen()
    vetdy03 = turtle.Turtle()

    make_square(vetdy03)
    turtle.mainloop()

def make_square(vetdy03):
    length = int(input("Escribe algo: "))
    
    for i in range(4):
        make_line_and_turn(vetdy03, length)
        make_line_and_turn(vetdy03, length)
    
def make_line_and_turn(vetdynuevo, length):
    vetdynuevo.forward(length)
    vetdynuevo.left(90)

    


if __name__ == '__main__':
    main()