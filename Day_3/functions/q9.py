import csv


def process_csv(file_name):

    numbers = []

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            numbers.append(int(row[1]))

    print("Average =", sum(numbers) / len(numbers))

    print("Maximum =", max(numbers))

    print("Minimum =", min(numbers))


process_csv("data.csv")