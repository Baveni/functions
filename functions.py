
def to_celsius(fahrenheit):
    '''
    (number) -> float
    Return the number of Celsius degrees equivalent to
    Fahrenheit degrees.
    >> to_celsius(100)
    >> 37.777
    '''
    return (fahrenheit - 32) * 5 / 9


def area(base, height):
    '''
    (number, number) -> number
    Return the are of a triangle with given base
    and height.
    >> area(12, 22)
    >> 132.0
    '''
    return base * height / 2

def perimeter(side1, side2, side3):
    '''
    Return the perimeter of the triangle with sides of
    length side1, side2, side3.
    >> perimeter(3, 4, 5)
    >> 12
    >> perimeter(13.5, 33, 55.3)
    >> 101.8
    '''
    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    '''
    (numbbers, number, number) -> float
    Return the semiperimeter of a triangle with sides
    of length side1, side2, side3.
     >> semiperimeter(5, 6, 8)
     >> 9.5
     >> semiperimeter(22.4, 8, 19.7)
     >> 25.049999
    '''
    return perimeter(side1, side2, side3) / 2
