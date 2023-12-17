symbol = 4
string = 25 * symbol
page = 50 * string
book = 100 * page

volume = 1.44 * 1024 * 1024

number = int(volume // book)

print("Количество книг, помещающихся на дискету:", number)
