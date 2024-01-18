import csv, json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    row_list = []
    with open(INPUT_FILENAME, 'r') as input_file:
        with open(OUTPUT_FILENAME, 'w') as output_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                row_list.append(row)

            json.dump(row_list, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
