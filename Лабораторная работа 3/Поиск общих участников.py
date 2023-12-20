def find_common_participants(first_group, second_group, divisor=','):
    first_group = set(first_group.split(divisor))
    second_group = set(second_group.split(divisor))
    common = first_group.intersection(second_group)
    common = list(common)
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, divisor='|'))
