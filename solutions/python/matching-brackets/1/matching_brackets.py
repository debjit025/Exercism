def is_paired(code):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    openers = set(pairs.values())

    for char in code:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack

    
