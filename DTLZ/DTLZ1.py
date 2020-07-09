# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:38:14 2020

@author: taiki
"""
import math
#import numpy as np

class DTLZ1:

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
            g += (self.v[i] - 0.5) * (self.v[i] - 0.5) - math.cos(20.0 * math.pi * (self.v[i] - 0.5))
        
        g = 100 * (self.k + g)
        
        for i in range(self.numobj):
            self.f[i] = (1.0 + g) * 0.5
        
        for i in range(self.numobj):
            for j in range(self.numobj - (i + 1)):
                self.f[i] *= self.v[j]
            if i != 0:
                aux = self.numobj - (i + 1);
                self.f[i] *= 1 - self.v[aux]
                
        return self.f
