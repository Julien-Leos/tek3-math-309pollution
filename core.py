import operator
import copy
import sys
import math

def binomialCoeff(n, i):
    return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

def bernsteinPolynomial(n, i, u):
    a = binomialCoeff(n, i)
    b = math.pow(u, i)
    c = pow(1 - u, n - i)
    return a * b * c

class Core:
    def __init__(self, args):
        [self.n, self.map_, self.x, self.y] = args
        self.n -= 1
        self.x /= self.n
        self.y /= self.n
        self.result = 0

    def bezierSurface(self):
        for i in range(self.n + 1):
            for j in range(self.n + 1):
                bernX = bernsteinPolynomial(self.n, i, self.x)
                bernY = bernsteinPolynomial(self.n, j, self.y)
                self.result += bernX * bernY * self.map_[i][j]

    def displayResult(self):
        print("%.2f" % self.result)