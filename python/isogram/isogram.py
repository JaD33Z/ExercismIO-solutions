
def is_isogram(string):
    string = string.lower()
    ns = "".join(c for c in string if c.isalpha())
    return len(ns) == len(set(ns))
