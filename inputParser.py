
def parseTValues(inp):
    tValues = inp.split('|')
    knots = list(map(float, tValues))
    return knots

def parseCValues(inp):
    cValues = inp.split('|')
    coefficients = list(map(float, cValues))
    return coefficients

def parseKValue(inp):
    degree = int(inp)
    return degree

def parsePoints(inp):
    points = inp.split('|')
    x = []
    y = []
    for point in points:
        point = point.split(',')
        x.append(int(point[0][1:]))
        y.append(int(point[1][:-1]))
    return x, y
