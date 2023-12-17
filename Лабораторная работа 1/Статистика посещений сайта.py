users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

total = len(users)
unique_total = len(set(users))

attendance = {"Общее количество": 0,
              "Уникальные посещения": 0}

attendance["Общее количество"] = total
attendance["Уникальные посещения"] = unique_total

print(attendance)
