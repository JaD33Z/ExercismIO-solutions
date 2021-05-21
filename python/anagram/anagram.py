
# As list comprehension:

def find_anagrams(word, candidates):
    return [i for i in candidates if sorted(word.lower()) == sorted(i.lower()) and i.lower() != word.lower()]


# Or
# As for loop:

def find_anagrams(word, candidates):
    ls = []
    for i in candidates:
        if sorted(word.lower()) == sorted(i.lower()) and i.lower() != word.lower():
            ls.append(i)
    return ls

