import string

def is_pangram(sentence):
    chars = string.ascii_lowercase
    req = set(chars)
    return req <= set(sentence.lower())












