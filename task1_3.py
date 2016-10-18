def reverse_string(string):
    splitted = string.split()
    reversed = splitted[::-1]
    return ' '.join(reversed)


if __name__ == "__main__":
    print "Return reversed string by whitespace"
    string  = str(raw_input('input string:'))
    print "Reversed string: ", reverse_string(string)
