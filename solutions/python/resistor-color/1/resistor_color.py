def color_code(color):
    colors = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
    color = color.lower().strip()
    if color in colors:
        return colors.index(color)

def colors():
    return [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white",
    ]
