def case_converter(text, seperator = "_"):
    new_text = []
    for index, letter in enumerate(text):
        if letter.isupper():
            if not index == 0:
                new_text.append(seperator)
            new_text.append(letter.lower())
        else:
            new_text.append(letter)

    return "".join(new_text)


name = "ThisIsCamelCased"

snake_case = case_converter(name)
kebab_case = case_converter(name, "-")

print(snake_case)
print(kebab_case)