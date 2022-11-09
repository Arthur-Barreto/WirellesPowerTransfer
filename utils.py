# arquivo de metodos auxiliares 
# calculo de reatancia em serie e paralelo

import cmath
import numpy as np
from numpy import pi
from numpy import sqrt

def serie(*args):
    return np.sum(args)

def paralelo(*args):
    return 1/np.sum(1/arg for arg in args)

def retangular(zeq):
    return cmath.rect(abs(zeq),cmath.phase(zeq)*180/pi)

def polarGrau(zeq):
    return abs(zeq),cmath.phase(zeq)*180/pi

def eficaz(a):
    return a/sqrt(2)