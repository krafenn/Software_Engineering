def findoffice(officetuple, target_id):
    first_index = None
    second_index = None

    for index, item in enumerate(officetuple):
        if item == target_id:
            if first_index is None:
                first_index = index
            else:
                second_index = index

    if first_index is None:
        return ()
    elif second_index is None:
        return officetuple[first_index:]
    else:
        return officetuple[first_index:second_index + 1]

office = (1, 3, 5, 7, 3, 9, 2, 3, 6)
result = findoffice(office, 3)
print(result)
