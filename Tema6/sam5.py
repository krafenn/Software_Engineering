def average_time_per_day(data):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    day_times = {day: [] for day in days}

    for item in data:
        if item[0] in days:
            day_times[item[0]].append(item[1])

    average_per_day = [(day, sum(times) / len(times)) if times else (day, 0) for day, times in day_times.items()]
    return average_per_day

user_data = [
    ("Понедельник", 60),
    ("Понедельник", 90),
    ("Вторник", 120),
    ("Среда", 80),
    ("Среда", 100),
    ("Среда", 120),
    ("Четверг", 60),
    ("Четверг", 90),
    ("Пятница", 100)
]

result = average_time_per_day(user_data)
for day, average_time in result:
    print(f"{day}: {average_time}")