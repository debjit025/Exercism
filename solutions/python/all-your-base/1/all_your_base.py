def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    elif output_base < 2:
        raise ValueError('output base must be >= 2')
    elif digits == []:
        return [0]
    elif any(d < 0 or d >= input_base for d in digits):
        raise ValueError('all digits must satisfy 0 <= d < input base')

    # Convert input digits to base 10
    base10 = 0
    for digit in digits:
        base10 = base10 * input_base + digit

    # Special case for zero
    if base10 == 0:
        return [0]

    # Convert base 10 to output base
    output_digits = []
    while base10 > 0:
        output_digits.insert(0, base10 % output_base)
        base10 //= output_base

    return output_digits