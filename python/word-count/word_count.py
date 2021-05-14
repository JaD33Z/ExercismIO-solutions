import re

def count_words(sentence):
    str = re.findall(r"[a-zA-Z0-9]+(?:'\w+)?", sentence.lower())
    freq = [str.count(word) for word in str]
    return dict(zip(str, freq))
    return str
