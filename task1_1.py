'''
Calculate rectangular side(hypotenuse?)
'''
def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5


if __name__ == "__main__":
    print "Calculate rectangular side"
    a = float(raw_input('a:'))
    b = float(raw_input('b:'))
    print "The Length of the Hypotenuse is", hypotenuse(a, b)
