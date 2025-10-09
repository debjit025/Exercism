def value(colors):
    color = ["black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"]
    number = ''
    colors = colors[0:2]
    for i in colors:
        if i in color:
            number += str(color.index(i))
    return int(number)