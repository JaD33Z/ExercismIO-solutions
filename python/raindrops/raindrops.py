raindrops = ((3,'Pling'), (5,'Plang'), (7,'Plong'))

def convert(number):
    return "".join(value for key, value in raindrops if number % key ==0) or str(number)
