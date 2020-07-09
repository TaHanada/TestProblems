# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:38:14 2020

@author: taiki
"""
import math
#import numpy as np

class C2DTLZ2:

    def __init__(self, numobj, numvar):
        self.numobj = numobj
        self.numvar = numvar
        self.f = [0] * numobj
        self.v = [0] * numvar
        if self.numobj == 3:
            self.rValue = 0.4
        else:
            self.rValue = 0.5
     

    def func_con(self, lists):
        for i in range(self.numobj):
            self.f[i] = lists[i]
        sum2 = 0
        minSum1 = 100
        for i in range(self.numobj):
          sum1 = (self.f[i] - 1.0) ** 2.0 - self.rValue ** 2.0
          for j in range(self.numobj):
            if i != j:
              sum1 += self.f[j] ** 2.0

          minSum1 = min(minSum1, sum1)
          sum2 += (self.f[i] - 1.0/math.sqrt(self.numobj)) ** 2.0
        sum2 = sum2 - self.rValue ** 2.0
        conv = min(minSum1, sum2)
                
        return -conv
