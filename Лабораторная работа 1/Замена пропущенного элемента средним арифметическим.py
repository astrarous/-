numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

indx = 0

for i, number in enumerate(numbers):
    if number is None:
        indx = i
summary = sum(numbers[:indx]) + sum(numbers[indx + 1:])
average = summary / len(numbers)
numbers[indx] = average

print("Измененный список:", numbers)
