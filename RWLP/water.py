# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 03:16:49 2020

@author: taiki
"""

import numpy as np
import math
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D​

def cal_f1(x1, x2, x3):
    ans = 106780.37 * (x2 + x3) + 61704.67
    return ans

def cal_f2(x1, x2, x3):
    ans = 3000 * x1
    return ans

def cal_f3(x1, x2, x3):
    ans = 305700 * 0.02289 * x2 / ((0.06 * 2289) ** 0.65)
    return ans

def cal_f4(x1, x2, x3):
    ans = 250 * 2289 * math.exp(-39.75 * x2 + 9.9 * x3 + 2.74)
    return ans

def cal_f5(x1, x2, x3):
    ans = 25 * (1.39 / (x1 * x2) + 4940 * x3 - 80)
    return ans

def is_feasible(x1, x2, x3):
    ans = False
    if (1 - (0.00139/(x1 * x2) + 4.94 * x3 - 0.08) >= 0) and (1 - (0.000306/(x1 * x2) + 1.082 * x3 - 0.0986) >= 0) and (
            50000 - (12.307/(x1 * x2) + 49408.24 * x3 + 4051.02) >= 0) and (16000 - (2.098/(x1 * x2) + 8046.33 * x3 - 696.71) >= 0) and (
                    10000 - (2.138/(x1 * x2) + 7883.39 * x3 - 705.04) >= 0) and (
                            2000 - (0.417 * x1 * x2 + 1721.26 * x3 - 136.54) >= 0) and (
                                    550 - (0.164/(x1 * x2) + 631.13 * x3 - 54.48) >= 0):
        ans = True
    return ans

gridSize = 50

arr = []

for x1_ind in range(gridSize + 1):
    for x2_ind in range(gridSize + 1):
        for x3_ind in range(gridSize + 1):
            x1 = (0.45 - 0.01) * x1_ind / (gridSize) + 0.01
            x2 = (0.10 - 0.01) * x2_ind / (gridSize) + 0.01
            x3 = (0.10 - 0.01) * x3_ind / (gridSize) + 0.01
            sol = is_feasible(x1, x2, x3)
            f1 = cal_f1(x1, x2, x3)
            f2 = cal_f2(x1, x2, x3)
            f3 = cal_f3(x1, x2, x3)
            f4 = cal_f4(x1, x2, x3)
            f5 = cal_f5(x1, x2, x3)

            #print(f'{x1}, {x2}, {x3}, {x4}, {f1}, {f2}, {sol}')
            arr.append([x1, x2, x3, f1, f2, f3, f4, f5, sol])
                
file_feasible = open('solution_feasible.csv', 'w')
file_infeasible = open('solution_infeasible.csv', 'w')
file_x1min = open('solution_x1min.csv', 'w')
file_x1max = open('solution_x1max.csv', 'w')
file_x2min = open('solution_x2min.csv', 'w')
file_x2max = open('solution_x2max.csv', 'w')
file_x3min = open('solution_x3min.csv', 'w')
file_x3max = open('solution_x3max.csv', 'w')

for l in range(len(arr)):
    mapped_arr = map(str, arr[l])
    strTemp = ','.join(mapped_arr) + ",\n"
    if arr[l][8] is True:
        file_feasible.write(strTemp)
        if arr[l][0] == 0.01:
            file_x1min.write(strTemp)
        elif arr[l][0] == 0.45:
            file_x1max.write(strTemp)
        if arr[l][1] == 0.01:
            file_x2min.write(strTemp)
        elif arr[l][1] == 0.10:
            file_x2max.write(strTemp)
        if arr[l][2] == 0.01:
            file_x3min.write(strTemp)
        elif arr[l][2] == 0.10:
            file_x3max.write(strTemp)
    else:
        file_infeasible.write(strTemp)
        
file_feasible.close()
file_infeasible.close()
file_x1min.close()
file_x1max.close()
file_x2min.close()
file_x2max.close()
file_x3min.close()
file_x3max.close()

data_feasible = np.genfromtxt("solution_feasible.csv", delimiter=",")
X = list(data_feasible[:, 3])
"""
Y = list(data_feasible[:, 5])
data_target_min = np.genfromtxt("solution_x1min.csv", delimiter=",")
data_target_max = np.genfromtxt("solution_x1max.csv", delimiter=",")
X_target_min = list(data_target_min[:, 4])
Y_target_min = list(data_target_min[:, 5])
X_target_max = list(data_target_max[:, 4])
Y_target_max = list(data_target_max[:, 5])
plt.scatter(X, Y, c='grey', s=2)
plt.scatter(X_target_min, Y_target_min, c='red', s=5)
plt.scatter(X_target_max, Y_target_max, c='blue', s=5)
plt.show()
"""
# Get nondominated solutions
file_nondominated = open('solution_nondominated.csv', 'w')
file_dominated = open('solution_dominated.csv', 'w')
for i in range(len(X)):
    mapped_data = map(str, data_feasible[i])
    strTemp = ','.join(mapped_data) + ",\n"
    count = 0
    for j in range(len(X)):
        if (data_feasible[i][3] >= data_feasible[j][3]) and (data_feasible[i][4] >= data_feasible[j][4]) and (
                data_feasible[i][5] >= data_feasible[j][5]) and (data_feasible[i][6] >= data_feasible[j][6]) and(
                        data_feasible[i][7] >= data_feasible[j][7]):
            count += 1
        if count == 2:
            break
    # print(count)
    if count == 1:
        file_nondominated.write(strTemp)
    else:
        file_dominated.write(strTemp)

file_nondominated.close()
file_dominated.close()

data_infeasible = np.genfromtxt("solution_infeasible.csv", delimiter=",")
data_nondominated = np.genfromtxt("solution_nondominated.csv", delimiter=",")
data_dominated = np.genfromtxt("solution_dominated.csv", delimiter=",")
print(len(data_infeasible[:, 0]))
print(len(data_nondominated[:, 0]))
print(len(data_dominated[:, 0]))

analy_x1 = np.array([])
for x1_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x1 = (0.45 - 0.01) * x1_ind / (gridSize) + 0.01
    for i in range(len(data_infeasible[:, 0])):
        if data_infeasible[i, 0] == x1:
            count += 1
    for i in range(len(data_nondominated[:, 0])):
        if data_nondominated[i, 0] == x1:
            countn += 1
    for i in range(len(data_dominated[:, 0])):
        if data_dominated[i, 0] == x1:
            countd += 1
    analy_x1 = np.append(analy_x1, (x1, countn, countd, count))
analy_x1 = np.reshape(analy_x1, (gridSize + 1, 4))
analy_x1 = np.transpose(analy_x1)
np.savetxt('x1.csv', analy_x1, delimiter=',')

analy_x2 = np.array([])
for x2_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x2 = (0.10 - 0.01) * x2_ind / (gridSize) + 0.01
    for i in range(len(data_infeasible[:, 1])):
        if data_infeasible[i, 1] == x2:
            count += 1
    for i in range(len(data_nondominated[:, 1])):
        if data_nondominated[i, 1] == x2:
            countn += 1
    for i in range(len(data_dominated[:, 1])):
        if data_dominated[i, 1] == x2:
            countd += 1
    analy_x2 = np.append(analy_x2, (x2, countn, countd, count))
analy_x2 = np.reshape(analy_x2, (gridSize + 1, 4))
analy_x2 = np.transpose(analy_x2)
np.savetxt('x2.csv', analy_x2, delimiter=',')

analy_x3 = np.array([])
for x3_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x3 = (0.10 - 0.01) * x3_ind / (gridSize) + 0.01
    for i in range(len(data_infeasible[:, 2])):
        if data_infeasible[i, 2] == x3:
            count += 1
    for i in range(len(data_nondominated[:, 2])):
        if data_nondominated[i, 2] == x3:
            countn += 1
    for i in range(len(data_dominated[:, 2])):
        if data_dominated[i, 2] == x3:
            countd += 1
    analy_x3 = np.append(analy_x3, (x3, countn, countd, count))
analy_x3 = np.reshape(analy_x3, (gridSize + 1, 4))
analy_x3 = np.transpose(analy_x3)
np.savetxt('x3.csv', analy_x3, delimiter=',')
