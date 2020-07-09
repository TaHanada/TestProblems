# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:20:51 2020

@author: taiki
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

gridSize = 6
# data_infeasible = np.genfromtxt("solution_infeasible.csv", delimiter=",")
data_nondominated = np.genfromtxt("solution_nondominated.csv", delimiter=",")
data_dominated = np.genfromtxt("solution_dominated.csv", delimiter=",")

X = list(data_nondominated[:, 7])
Y = list(data_nondominated[:, 8])
Z = list(data_nondominated[:, 9])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='black', s=5)
ax.view_init(30, 60)
ax.set_xlabel("f1")
ax.set_ylabel("f2")
ax.set_zlabel("f3")
plt.show()

analy_x1 = np.array([])
for x1_ind in range(gridSize + 1):
    # count = 0
    countn = 0
    countd = 0
    x1 = x1_ind / (gridSize)
    """
    for i in range(len(data_infeasible[:, 0])):
        if data_infeasible[i, 0] == x1:
            count += 1
    """
    for i in range(len(data_nondominated[:, 0])):
        if data_nondominated[i, 0] == x1:
            countn += 1
    for i in range(len(data_dominated[:, 0])):
        if data_dominated[i, 0] == x1:
            countd += 1
    analy_x1 = np.append(analy_x1, (x1, countn, countd))
analy_x1 = np.reshape(analy_x1, (gridSize + 1, 3))
analy_x1 = np.transpose(analy_x1)
np.savetxt('x1.csv', analy_x1, delimiter=',')

analy_x2 = np.array([])
for x2_ind in range(gridSize + 1):
    # count = 0
    countn = 0
    countd = 0
    x2 = x2_ind / (gridSize)
    """
    for i in range(len(data_infeasible[:, 1])):
        if data_infeasible[i, 1] == x2:
            count += 1
    """
    for i in range(len(data_nondominated[:, 1])):
        if data_nondominated[i, 1] == x2:
            countn += 1
    for i in range(len(data_dominated[:, 1])):
        if data_dominated[i, 1] == x2:
            countd += 1
    analy_x2 = np.append(analy_x2, (x2, countn, countd))
analy_x2 = np.reshape(analy_x2, (gridSize + 1, 3))
analy_x2 = np.transpose(analy_x2)
np.savetxt('x2.csv', analy_x2, delimiter=',')

analy_x3 = np.array([])
for x3_ind in range(gridSize + 1):
    # count = 0
    countn = 0
    countd = 0
    x3 = x3_ind / (gridSize)
    """
    for i in range(len(data_infeasible[:, 2])):
        if data_infeasible[i, 2] == x3:
            count += 1
    """
    for i in range(len(data_nondominated[:, 2])):
        if data_nondominated[i, 2] == x3:
            countn += 1
    for i in range(len(data_dominated[:, 2])):
        if data_dominated[i, 2] == x3:
            countd += 1
    analy_x3 = np.append(analy_x3, (x3, countn, countd))
analy_x3 = np.reshape(analy_x3, (gridSize + 1, 3))
analy_x3 = np.transpose(analy_x3)
np.savetxt('x3.csv', analy_x3, delimiter=',')

analy_x4 = np.array([])
for x4_ind in range(gridSize + 1):
    # count = 0
    countn = 0
    countd = 0
    x4 = x4_ind / (gridSize)
    """
    for i in range(len(data_infeasible[:, 3])):
        if data_infeasible[i, 3] == x4:
            count += 1
    """
    for i in range(len(data_nondominated[:, 3])):
        if data_nondominated[i, 3] == x4:
            countn += 1
    for i in range(len(data_dominated[:, 3])):
        if data_dominated[i, 3] == x4:
            countd += 1
    analy_x4 = np.append(analy_x4, (x4, countn, countd))
analy_x4 = np.reshape(analy_x4, (gridSize + 1, 3))
analy_x4 = np.transpose(analy_x4)
np.savetxt('x4.csv', analy_x4, delimiter=',')

analy_x5 = np.array([])
for x5_ind in range(gridSize + 1):
    # count = 0
    countn = 0
    countd = 0
    x5 = x5_ind / (gridSize)
    """
    for i in range(len(data_infeasible[:, 4])):
        if data_infeasible[i, 4] == x5:
            count += 1
    """
    for i in range(len(data_nondominated[:, 4])):
        if data_nondominated[i, 4] == x5:
            countn += 1
    for i in range(len(data_dominated[:, 4])):
        if data_dominated[i, 4] == x5:
            countd += 1
    analy_x5 = np.append(analy_x5, (x5, countn, countd))
analy_x5 = np.reshape(analy_x5, (gridSize + 1, 3))
analy_x5 = np.transpose(analy_x5)
np.savetxt('x5.csv', analy_x5, delimiter=',')

analy_x6 = np.array([])
for x6_ind in range(gridSize + 1):
    # count = 0
    countn = 0
    countd = 0
    x6 = x6_ind / (gridSize)
    """
    for i in range(len(data_infeasible[:, 5])):
        if data_infeasible[i, 5] == x6:
            count += 1
    """
    for i in range(len(data_nondominated[:, 5])):
        if data_nondominated[i, 5] == x6:
            countn += 1
    for i in range(len(data_dominated[:, 5])):
        if data_dominated[i, 5] == x6:
            countd += 1
    analy_x6 = np.append(analy_x6, (x6, countn, countd))
analy_x6 = np.reshape(analy_x6, (gridSize + 1, 3))
analy_x6 = np.transpose(analy_x6)
np.savetxt('x6.csv', analy_x6, delimiter=',')

analy_x7 = np.array([])
for x7_ind in range(gridSize + 1):
    # count = 0
    countn = 0
    countd = 0
    x7 = x7_ind / (gridSize)
    """
    for i in range(len(data_infeasible[:, 6])):
        if data_infeasible[i, 6] == x7:
            count += 1
    """
    for i in range(len(data_nondominated[:, 6])):
        if data_nondominated[i, 6] == x7:
            countn += 1
    for i in range(len(data_dominated[:, 6])):
        if data_dominated[i, 6] == x7:
            countd += 1
    analy_x7 = np.append(analy_x7, (x7, countn, countd))
analy_x7 = np.reshape(analy_x7, (gridSize + 1, 3))
analy_x7 = np.transpose(analy_x7)
np.savetxt('x7.csv', analy_x7, delimiter=',')
