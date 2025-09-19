def is_armstrong_number(number):
    num = number 
    add = 0
    while number>0:
        add += (number % 10) ** len(str(num))
        number //= 10
    return add == num
        
