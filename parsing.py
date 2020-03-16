import sys
import numpy as np

def isInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def isFloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def checkUsage(arg):
    if arg == "-h" or arg == "--help":
        print("USAGE:\t./309pollution n file x y\n\nDESCRIPTION")
        print("\tn\tnumber of points on the grid axis")
        print("\tfile\tcsv file containing the data points x;y;p")
        print("\tx\tabscissa of the point whose pollution level we want to know")
        print("\ty\tordinate of the point whose pollution level we want to know")
        sys.exit(0)

def checkArgs(args):
    if len(args) != 4:
        print("Invalid number of arguments. Try ./309pollution -h for usage")
        sys.exit(84)
    if not isInt(args[0]) or int(args[0]) < 1:
        print("Argument 1 must be integer and strictly positives. Try ./309pollution -h for usage")
        sys.exit(84)

    for arg in args[2:]:
        if not isFloat(arg) or float(arg) < 0 or float(arg) > int(args[0]) - 1:
            print("Argument 2 and 3 must be decimals, greater or equal than 0 and inferior or equal to n - 1. Try ./309pollution -h for usage")
            sys.exit(84)
    return [int(args[0]), args[1], float(args[2]), float(args[3])]

def parseFile(fileName, mapLength):
    try:
        fd = open(fileName, 'r')
    except IOError:
        print("File does not exist. Try ./309pollution -h for usage")
        sys.exit(84)
    data = fd.read()
    data = data.split('\n')
    if len(data[-1]) == 0:
        data.pop()
    
    map_ = [[0 for y in range(mapLength)] for x in range(mapLength)]
    for y in data:
        point = y.split(';')
        if len(point) != 3:
            print("Invalid file. Try ./309pollution -h for usage")
            sys.exit(84)
        for coord in point[:2]:
            if not isInt(coord):
                print("Invalid file. Try ./309pollution -h for usage")
                sys.exit(84)
        if not isInt(point[2]) or int(point[2]) < 0 or int(point[2]) > 100:
            print("Invalid file. Try ./309pollution -h for usage")
            sys.exit(84)
        map_[int(point[0])][int(point[1])] = int(point[2])

    return map_

def parse(args):
    if len(args) == 1:
        checkUsage(args[0])
    [n, filename, x, y] = checkArgs(args)
    map_ = parseFile(filename, n)
    return [n, map_, x, y]
