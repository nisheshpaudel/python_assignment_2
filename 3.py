paragraph = "There's an arc through which you can drive a car quickly.  That ant has a tan face." \
            "I have tons of snot fo you. And then ouch said the chou man.  I hit" \
            "the ram in his arm pit"

x = paragraph.split()


def findAnagram(x):

    dict = {}

    for word in x:
        key = ''.join(sorted(word))

        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = []
            dict[key].append(word)
        output = ""
        for key, value in dict.items():
            if len(value) > 1:
                output = output + ' '.join(value) + ' '

    return output


print(findAnagram(x))