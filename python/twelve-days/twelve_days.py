
def recite(start_verse, end_verse):
    with open('xmas-song.txt', 'r') as f:
        return [line.strip() for line in f.readlines()[start_verse - 1:end_verse]]
