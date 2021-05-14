
def abbreviate(words):
    return "".join([letter[0].upper() for letter in words.replace('-', ' ').replace('_', ' ').split()])

