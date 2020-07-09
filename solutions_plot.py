# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:17:54 2020

@author: taiki
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_feasible = np.genfromtxt('ドキュメント/GitHub/TestProblems/DTLZ/solution_feasible.csv', delimiter=",")
data_infeasible = np.genfromtxt('ドキュメント/GitHub/TestProblems/DTLZ/solution_infeasible.csv', delimiter=",")

X = list(data_feasible[:, 7])
Y = list(data_feasible[:, 8])
Z = list(data_feasible[:, 9])
X_i = list(data_infeasible[:, 7])
Y_i = list(data_infeasible[:, 8])
Z_i = list(data_infeasible[:, 9])

'''
plt.scatter(X_i, Y_i, c='grey', s=2)
plt.scatter(X, Y, c='red', s=2)

plt.show()
'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X_i, Y_i, Z_i, c='grey', s=2)
ax.scatter(X, Y, Z, c='red', s=5)
ax.set_xlabel("f1")
ax.set_ylabel("f2")
ax.set_zlabel("f3")
ax.view_init(30, 60)
plt.show()

