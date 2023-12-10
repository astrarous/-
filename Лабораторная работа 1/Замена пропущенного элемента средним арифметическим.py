numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

indx = 0

for i in range(len(numbers)):
    if type(numbers[i]) != int:
        indx = i
summary = sum(numbers[:indx]) + sum(numbers[indx + 1:])
approximate = summary / len(numbers)
numbers[indx] = approximate

print("Измененный список:", numbers)
