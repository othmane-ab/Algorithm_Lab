from random import random,randint
import math

K = 0.01
def sa(f, x0, Ti, Tf, l, c, dx):
    k = 0
    x = x0
    T = Ti
    while T>Tf:
        print(x,f(x))
        for i in range(l(k)):
            x_new = x + randint(-50,50)*dx 
            df = f(x_new) - f(x)
            if df>0:
                x = x_new
            else:
                if math.exp(df/(T*K))>random():
                    x = x_new
        T *= c
        k += 1
    return x

f = lambda x: -x**2+1
Ti = 10000
Tf = 1
c = 1.0 - 0.01
dx = 0.1
l = lambda k:5

x = sa(f, 200, Ti, Tf, l, c, dx)
print(x)


