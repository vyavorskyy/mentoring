"""
Check if word belongs to string
"""


def word_belong(word, string):
    if string.find(word) != -1:
        return True
    else: return False

if __name__ == "__main__":
    w = str(raw_input('Type word:'))
    s = str(raw_input('Type string:'))
    check = word_belong(w.lower(),s.lower())
    print check
