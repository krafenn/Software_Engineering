def removeelement(tuple, element):
    if element in tuple:
        index = tuple.index(element)
        new_tuple = tuple[:index] + tuple[index+1:]
        return new_tuple
    else:
        return tuple

origtuple = (1, 2, 3, 4, 2, 5)
element = 2
newtuple = removeelement(origtuple, element)
print(newtuple)
