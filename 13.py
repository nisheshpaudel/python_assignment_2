def create_csv(collection, header1, header2, header3):
    output = []
    output.append(tuple_to_comma_seperated((header1, header2, header3)))
    for line in collection:
        output.append(tuple_to_comma_seperated(line))

    return output


def tuple_to_comma_seperated(tuple):
    return ",".join(str(item) for item in tuple)


data = [('George', '4312 Abbey Road', 22),
        ('John', '54 Love Ave', 21)]

lines = create_csv(data, "name", "address", "age")

with open("test.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
