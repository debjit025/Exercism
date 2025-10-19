def label(colors):
    code = {'black': 0,
            'brown': 1,
            'red': 2,
            'orange': 3,
            'yellow': 4,
            'green': 5,
            'blue': 6,
            'violet': 7,
            'grey': 8,
            'white': 9}
    
    suffixes = [
        (1_000_000_000, "gigaohms"),
        (1_000_000, "megaohms"),
        (1_000, "kiloohms"),
    ]

    value = int(f"{code[colors[0]]}{code[colors[1]]}") * (10 ** code[colors[2]])
    for factor, label in suffixes:
        if value >= factor:
            return f"{value//factor} {label}"
    return f"{value} ohms"