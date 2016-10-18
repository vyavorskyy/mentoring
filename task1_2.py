'''
Calculate numbers of chars in string
'''
def string_leng(a, b):
    return len(a + b)


if __name__ == "__main__":
    print "Calculate nums of chars in two strings"
    a = str(raw_input('input first string:'))
    b = str(raw_input('input second string:'))
    print "Length of result string: ", string_leng(a, b)
