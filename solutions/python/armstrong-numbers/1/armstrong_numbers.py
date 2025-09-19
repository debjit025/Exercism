def is_armstrong_number(number):
    num = number
    size = len(str(num))
    add = 0
    while number>0:
        add += (number % 10) ** size
        number //= 10
    if add == num: 
        return True
    else:
        return False
