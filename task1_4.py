'''
Reverse whole string
'''
def reverse_string(string):
    result_strings = []
    n = len(string)
    while n:
        n -= 1
        result_strings.append(string[n])
    return ''.join(result_strings)



if __name__ == "__main__":
    print "Reverse whole string"
    string  = str(raw_input('input string:'))
    print "Reversed string: ", reverse_string(string)