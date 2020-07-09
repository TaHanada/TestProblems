# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:38:14 2020

@author: taiki
"""
import math
#import numpy as np

class C1DTLZ1:

    def __init__(self, numobj, numvar):
        self.numobj = numobj
        self.numvar = numvar
        self.f = [0] * numobj
        self.v = [0] * numvar
     

    def func_con(self, lists):
        sumc = 0
        for i in range(self.numobj):
            self.f[i] = lists[i]
        if self.numobj > 2:
            for i in range(self.numobj - 2):
                sumc += self.f[i] / 0.5
        else:
            sumc = self.f[0] / 0.5
        
        conv = 1.0 - self.f[self.numobj -1] / 0.6 - sumc
                
        return conv
