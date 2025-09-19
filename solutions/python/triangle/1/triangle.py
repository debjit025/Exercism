def equilateral(sides):
    if not sides or any(i <= 0 for i in sides):
        return False
    return all(i == sides[0] for i in sides)

def isosceles(sides):
    if not sides or any(i <= 0 for i in sides):
        return False
    a, b, c = sides
    return (a == b or b == c or a == c) and (a + b >= c and b + c >= a and a + c >= b)

def scalene(sides):
    if not sides or any(i <= 0 for i in sides):
        return False
    a, b, c = sides
    return (a + b >= c and b + c >= a and a + c >= b) and len(set(sides)) == 3