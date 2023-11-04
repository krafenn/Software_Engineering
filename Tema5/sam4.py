gradeslists = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
]

for grades in gradeslists:
    updgrades = []
    for grade in grades:
        if grade != 2:
            if grade == 3:
                updgrades.append(4)
            else:
                updgrades.append(grade)
    print(updgrades)
