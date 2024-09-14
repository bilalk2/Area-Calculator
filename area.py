import math
def area_of_circle (radius ) :
    return  math.pi*radius**2
def area_of_square(side) : 
    return side**2
def area_of_rectangle(length,width) : 
    return length*width
while True : 
    help = """
    choise : 
    c => area of circle
    s => area of square
    r => area of  rectangle
    e => Exiting the calculator
    """

    print(help)
    choise =  input("Choise : ")
    if choise =="c" :
        rad=float(input("what is the radius ? : "))
        print(f"the area of circle of radius {rad} is {area_of_circle(rad)}")
    if choise =="s" :
        side=float(input("what is the side ? : "))
        print(f"the area of square of side {side} is {area_of_square(side)}")
    if choise =="r" :
        length=float(input("what is the length ? : "))
        width=float(input("what is the width ? : "))
        print(f"the area of rectangle of length {length} and width {width} is {area_of_rectangle(length,width)}")
    if choise == "e" :
        break