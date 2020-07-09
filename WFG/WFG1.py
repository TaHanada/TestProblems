# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:38:14 2020

@author: taiki
"""
import math
#import numpy as np

class WFG1:

    def __init__(self, numvarp, numvard, numobj):
        self.numobj = numobj
        self.numvarp = numvarp
        self.numvard = numvard
        self.d = 1
        self.epsilon = 1e-10
        self.s = [0] * numobj
        self.a = [0] * (numobj - 1)
        for i in range(numobj):
            self.s[i] = 2 * (i + 1)
        for i in range(numobj - 1):
            self.a[i] = 1
     

    def func_obj(self, lists):
        def convex(x, m):
            result = 1.0
            M = len(x)
            #print('m:', m)
            for i in range(M - m):   
              result *= (1 - math.cos(x[i - 1] * math.pi * 0.5))
              #print('a')M-m=1でも行われる
            if m != 1:
              result *= (1 - math.sin(x[M - m] * math.pi * 0.5))
        
            return result
    
        def mixed(x, A, alpha):
            tmp = math.cos(2.0 * A * math.pi * x[0] + math.pi * 0.5)
        
            tmp /= (2.0 * A * math.pi)
    
            return (1.0 - x[0] - tmp) ** alpha
        
        def sLinear(y, A):
            return correctTo01(abs(y - A) / (abs(math.floor(A - y) + A)))
        
        def bFlat(y, A, B, C):
            tmp1 = min(0, math.floor(y - B)) * A * (B - y) / B
            tmp2 = min(0, math.floor(C - y)) * (1 - A) * (y - C) / (1 - C)
        
            return correctTo01(A + tmp1 - tmp2)
        
        def bPoly(y, alpha):
            return correctTo01(y ** alpha)
        
        def rSum(y, w):
            tmp1 = 0.0
            tmp2 = 0.0
            #print('rSum:', len(y))
            for i in range(len(y)):
              tmp1 += y[i] * w[i]
              tmp2 += w[i]
        
            return correctTo01(tmp1 / tmp2)
        
        def subVector(z, head, tail):
            size = tail - head + 1
            #print(head)
            result = [0] * int(size)
            #System.arraycopy(z, head, result, head - head, tail + 1 - head)
            for i in range(int(size)):
                for j in range(int(head), int(size)):
                    result[i] = z[j]
                    #print('a:', j)
            return result
        
        def normalize(z):
            result = z
            
            for i in range(len(z)):
              bound = 2.0 * (i + 1)   
              result[i] = z[i] / bound
              result[i] = correctTo02(result[i])   
        
            return result
        
        def correctTo01(a):
            minv = 0.0
            maxv = 1.0
            minEpsilon = minv - self.epsilon    
            maxEpsilon = maxv + self.epsilon
     
            if (minEpsilon <= a <= minv) or (minv <= a <= minEpsilon):   
              return minv
            elif (maxv <= a <= maxEpsilon) or (maxv >= a >= maxEpsilon):
              return maxv
            else:
              return a
          
        def correctTo02(a):
            minv = 0.0
            maxv = 1.0
            minEpsilon = minv - 1e-7   
            maxEpsilon = maxv + 1e-7
     
            if ((a <= minv and a >= minEpsilon) or (a >= minv and a <= minEpsilon)):   
              return minv
            elif ((a >= maxv and a <= maxEpsilon) or (a <= maxv and a >= maxEpsilon)):
              return maxv
            else:
              return a
        
        def calculateX(t):
            x = [0] * self.numobj
    
            for i in range(self.numobj - 1):    
                x[i] = max(t[self.numobj - 1], self.a[i]) * (t[i] - 0.5) + 0.5
                
            x[self.numobj - 1] = t[self.numobj - 1];
      
            return x
      
        def t1(z, k):
            result = [0] * len(z)
            for i in range(k):
                result[i] = z[i]
     
            for i in range(k, len(z)):
                result[i] = sLinear(z[i], 0.35)
    
            return result
        
        def t2(z, k):
            result = [0] * len(z)
            for i in range(k):
                result[i] = z[i]
        
            for i in range(k, len(z)):    
              result[i] = bFlat(z[i], 0.8, 0.75, 0.85)  
        
            return result
        
        def t3(z):
            result = [0] * len(z)
    
            for i in range(len(z)):  
              result[i] = bPoly(z[i], 0.02)
    
            return result
        
        def t4(z, k, M):
            result = [0] * M
            w = [0] * len(z)
    
            for i in range(len(z)): 
              w[i] = 2.0 * (i + 1)
       
            for i in range(1, M):   #i = 1 ~ M-1
              head = (i - 1) * k / (M - 1) + 1 
              tail = i * k / (M - 1)
              subZ = subVector(z, head - 1, tail - 1)
              subW = subVector(w, head - 1, tail - 1)    
              result[i - 1] = rSum(subZ, subW)
        
            head = k + 1 - 1
            tail = len(z) - 1
            subZ = subVector(z, head, tail)
            subW = subVector(w, head, tail)
            result[M - 1] = rSum(subZ, subW)   
        
            return result
        y = normalize(lists)
        y = t1(y, self.numvarp)
        y = t2(y, self.numvarp)
        y = t3(y)
        y = t4(y, self.numvarp, self.numobj)   
    
        result = [0] * self.numobj
        x = calculateX(y);

        for i in range(1, self.numobj):
            result[i - 1] = self.d * x[self.numobj - 1] + self.s[i - 1] * convex(x, i)

        result[self.numobj - 1] = self.d * x[self.numobj - 1] + self.s[self.numobj - 1] * mixed(x, 5, 1.0)

        return result
    