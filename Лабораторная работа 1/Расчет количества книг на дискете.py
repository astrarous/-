BYTES_PER_SYMBOL = 4
symbols = 25
lines = 50
pages = 100

disk_volume = 1.44 * 1024 * 1024
book_volume = BYTES_PER_SYMBOL * symbols * lines * pages

number = int(disk_volume // book_volume)

print("Количество книг, помещающихся на дискету:", number)
