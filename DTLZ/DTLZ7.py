# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:38:14 2020

@author: taiki
"""
import math
#import numpy as np

class DTLZ7:

    def __init__(self, numobj, numvar):
        self.numobj = numobj
        self.numvar = numvar
        self.f = [0] * numobj
        self.v = [0] * numvar
        self.k = self.numvar - self.numobj + 1
     

    def func_obj(self, lists):
        g = 0
        for i in range(self.numvar):
            self.v[i] = lists[i]
        for i in range(self.numvar - self.k, self.numvar):
            g += self.v[i]
        
        g = 1 + (9.0 * g) / self.k
        
        for i in range(self.numobj - 1):
            self.f[i] = self.v[i]
        
        h = 0
        for i in range(self.numobj - 1):
            h += (self.f[i] / (1.0 + g)) * (1 + math.sin(3.0 * math.pi * self.f[i]))
        
        h = self.numobj - h
        
        self.f[self.numobj - 1] = (1 + g) * h
                
        return self.f
