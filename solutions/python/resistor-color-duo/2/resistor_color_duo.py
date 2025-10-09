def value(colors):
    color = ["black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"]
    number = ''
    for i in colors[:2]:
        if i in color:
            number += str(color.index(i))
    return int(number)