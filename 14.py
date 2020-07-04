def read_csv(filename):
    file = open("test.txt")
    people = []
    all_lines = file.readlines()
    headers = all_lines[:1][0].replace("\n","").split(",")
    all_values = all_lines[1:]

    for line in all_values:
        values = line.replace("\n","").split(",")
        person = {}
        for i, header in enumerate(headers):
            person[header] = values[i]

        people.append(person)

    return people


print(read_csv("test.txt"))