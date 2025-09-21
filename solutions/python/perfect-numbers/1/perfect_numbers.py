from math import sqrt

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factors=[]
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return 'deficient'
    else:
        for i in range(1, int(sqrt(number))+1):
            if number % i == 0:
                factors.append(i)
                if i != 1 and i != number//i:
                    factors.append(number//i)
        if sum(set(factors)) == number:
            return 'perfect'
        return 'abundant' if sum(set(factors)) > number else 'deficient'