def is_isogram(string):
    letters = [x.lower() for x in string if x.isalpha()]
    return len(set(letters)) == len(letters)