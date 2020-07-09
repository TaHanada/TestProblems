# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 03:16:49 2020

@author: taiki
"""

import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D​

def cal_f1(x1, x2, x3, x4):
    ans = (1.10471 * x1 * x1 * x2) + (0.04811 * x3 * x4) * (14.0 + x2)
    return ans

def cal_f2(x1, x2, x3, x4):
    ans = 2.1952 / ((x3 ** 3) * x4)
    return ans

def is_feasible(x1, x2, x3, x4):
    ans = False
    P = 6000
    L = 14
    E = 30 * (10 ** 6)
    G = 12 * (10 ** 6)
    tauMax = 13600
    sigmaMax = 30000
    M = P * (L + (x2 / 2))
    R = (((x2 * x2) / 4.0) + ((x1 + x3) / 2.0) ** 2) ** 0.5
    J = 2 * (2 ** 0.5) * x1 * x2 * (((x2 * x2) / 12.0) + ((x1 + x3) / 2.0) ** 2)
    tauDashDash = (M * R) / J
    tauDash = P / ((2 ** 0.5) * x1 * x2)
    tau = (tauDash * tauDash + ((2 * tauDash * tauDashDash * x2) / (2 * R)) + (tauDashDash * tauDashDash)) ** 0.5
    sigma = (6 * P * L) / (x4 * x3 * x3)
    tmpVar = 4.013 * E * (((x3 ** 2) * (x4 ** 6)) / 36.0) ** 0.5 / (L ** 2)
    tmpVar2 = (x3 / (2 * L)) * (E / (4 * G)) ** 0.5
    PC = tmpVar * (1 - tmpVar2)
    if (tauMax - tau >= 0) and (sigmaMax - sigma >= 0) and (x4 - x1 >= 0) and (
            PC - P >= 0):
        ans = True
    return ans

gridSize = 20

arr = []

for x1_ind in range(gridSize + 1):
    for x2_ind in range(gridSize + 1):
        for x3_ind in range(gridSize + 1):
            for x4_ind in range(gridSize + 1):
                x1 = (5.0 - 0.123) * x1_ind / (gridSize) + 0.123
                x2 = (10 - 0.1) * x2_ind / (gridSize) + 0.1
                x3 = (10 - 0.1) * x3_ind / (gridSize) + 0.1
                x4 = (5.0 - 0.123) * x4_ind / (gridSize) + 0.123
                
                sol = is_feasible(x1, x2, x3, x4)
                f1 = cal_f1(x1, x2, x3, x4)
                f2 = cal_f2(x1, x2, x3, x4)

                #print(f'{x1}, {x2}, {x3}, {x4}, {f1}, {f2}, {sol}')
                arr.append([x1, x2, x3, x4, f1, f2, sol])
                
file_feasible = open('solution_feasible.csv', 'w')
file_infeasible = open('solution_infeasible.csv', 'w')
file_x1min = open('solution_x1min.csv', 'w')
file_x1max = open('solution_x1max.csv', 'w')
file_x2min = open('solution_x2min.csv', 'w')
file_x2max = open('solution_x2max.csv', 'w')
file_x3min = open('solution_x3min.csv', 'w')
file_x3max = open('solution_x3max.csv', 'w')
file_x4min = open('solution_x4min.csv', 'w')
file_x4max = open('solution_x4max.csv', 'w')

for l in range(len(arr)):
    mapped_arr = map(str, arr[l])
    strTemp = ','.join(mapped_arr) + ",\n"
    if arr[l][6] is True:
        file_feasible.write(strTemp)
        if arr[l][0] == 0.123:
            file_x1min.write(strTemp)
        elif arr[l][0] == 5.0:
            file_x1max.write(strTemp)
        if arr[l][1] == 0.1:
            file_x2min.write(strTemp)
        elif arr[l][1] == 10:
            file_x2max.write(strTemp)
        if arr[l][2] == 0.1:
            file_x3min.write(strTemp)
        elif arr[l][2] == 10:
            file_x3max.write(strTemp)
        if arr[l][3] == 0.123:
            file_x4min.write(strTemp)
        elif arr[l][3] == 5.0:
            file_x4max.write(strTemp)
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
file_x4min.close()
file_x4max.close()

data_feasible = np.genfromtxt("solution_feasible.csv", delimiter=",")
X = list(data_feasible[:, 4])
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
        if (data_feasible[i, 4] >= data_feasible[j, 4]) and (data_feasible[i, 5] >= data_feasible[j, 5]):
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
    x1 = (5.0 - 0.123) * x1_ind / (gridSize) + 0.123
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
    x2 = (10 - 0.1) * x2_ind / (gridSize) + 0.1
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
    x3 = (10 - 0.1) * x3_ind / (gridSize) + 0.1
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

analy_x4 = np.array([])
for x4_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x4 = (5.0 - 0.123) * x4_ind / (gridSize) + 0.123
    for i in range(len(data_infeasible[:, 3])):
        if data_infeasible[i, 3] == x4:
            count += 1
    for i in range(len(data_nondominated[:, 3])):
        if data_nondominated[i, 3] == x4:
            countn += 1
    for i in range(len(data_dominated[:, 3])):
        if data_dominated[i, 3] == x4:
            countd += 1
    analy_x4 = np.append(analy_x4, (x4, countn, countd, count))
analy_x4 = np.reshape(analy_x4, (gridSize + 1, 4))
analy_x4 = np.transpose(analy_x4)
np.savetxt('x4.csv', analy_x4, delimiter=',')
