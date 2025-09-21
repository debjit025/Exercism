def rotate(text, key):
    new = ''
    if key in (0, 26): return text
    for x in text:
        if 'a' <= x <= 'z':
            new += chr((ord(x) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= x <= 'Z':
            new += chr((ord(x) - ord('A') + key) % 26 + ord('A'))
        else:
            new += x
    return new
            