'''
Combine all elements from one dictionary to another
 '''
d1 = {'Name': 'Yaryna', 'Second Name': 'Yavorska', 'Age': 2}
d2 = {'Second Name': 'Yavorska', 'Hight': 92, 'Weight': 1.3, 'Eye color': 'brown'}


def merge_dicts(a,b):

    result = {}
    for dict in dict_1, dict_2:
        result.update(dict)
    return result


if __name__ == "__main__":
    z = merge_dicts(d1,d2)
    print 'Combined dict:', z
