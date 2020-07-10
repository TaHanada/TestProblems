# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:17:54 2020

@author: taiki
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

os.chdir("C:\\Users\\taiki\\Documents\\GitHub\\TestProblems\\RWLP")
data_feasible = np.genfromtxt("solution_feasible.csv", delimiter=",")
data_infeasible = np.genfromtxt("solution_infeasible.csv", delimiter=",")

X = list(data_feasible[:, 4])
Y = list(data_feasible[:, 5])
# Z = list(data_feasible[:, 9])
X_i = list(data_infeasible[:, 4])
Y_i = list(data_infeasible[:, 5])
# Z_i = list(data_infeasible[:, 9])

data_target_min = np.genfromtxt("solution_x1min.csv", delimiter=",")
data_target_max = np.genfromtxt("solution_x1max.csv", delimiter=",")
X_target_min = list(data_target_min[:, 4])
Y_target_min = list(data_target_min[:, 5])
X_target_max = list(data_target_max[:, 4])
Y_target_max = list(data_target_max[:, 5])
plt.scatter(X, Y, c='grey', s=2)
plt.scatter(X_i, Y_i, c='grey', s=2)
plt.scatter(X_target_min, Y_target_min, c='red', s=5)
plt.scatter(X_target_max, Y_target_max, c='blue', s=5)

# plt.scatter(X, Y, c='red', s=2)

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
'''
