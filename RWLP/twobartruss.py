# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 03:16:49 2020

@author: taiki
"""

import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D​

def cal_f1(x1, x2, x3):
    ans = x1 * (16 + x3 ** 2) ** 0.5 + x2 * (1 + x3 ** 2) ** 0.5
    return ans

def cal_f2(x1, x2, x3):
    ans = (20 * (16 + x3 ** 2) ** 0.5) / (x3 * x1)
    return ans

def is_feasible(x1, x2, x3):
    ans = False
    fv = x1 * (16 + x3 ** 2) ** 0.5 + x2 * (1 + x3 ** 2) ** 0.5
    fsa = (20 * (16 + x3 ** 2) ** 0.5) / (x3 * x1)
    fsb = (80 * (1 + x3 ** 2) ** 0.5) / (x3 * x2)
    if (fv <= 0.1) and (fsa <= 100000) and (fsb <= 100000):
        ans = True
    return ans

gridSize = 50

arr = []

for x1_ind in range(gridSize + 1):
    for x2_ind in range(gridSize + 1):
        for x3_ind in range(gridSize + 1):
            x1 = (0.07 - 0.0001) * x1_ind / (gridSize) + 0.0001
            x2 = (0.03 - 0.0001) * x2_ind / (gridSize) + 0.0001
            x3 = (3 - 1) * x3_ind / (gridSize) + 1
            sol = is_feasible(x1, x2, x3)
            f1 = cal_f1(x1, x2, x3)
            f2 = cal_f2(x1, x2, x3)
            
            #print(f'{x1}, {x2}, {x3}, {x4}, {f1}, {f2}, {sol}')
            arr.append([x1, x2, x3, f1, f2, sol])
                
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
    if arr[l][5] is True:
        file_feasible.write(strTemp)
        if arr[l][0] == 0.0001:
            file_x1min.write(strTemp)
        elif arr[l][0] == 0.07:
            file_x1max.write(strTemp)
        if arr[l][1] == 0.0001:
            file_x2min.write(strTemp)
        elif arr[l][1] == 0.03:
            file_x2max.write(strTemp)
        if arr[l][2] == 1:
            file_x3min.write(strTemp)
        elif arr[l][2] == 3:
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
        if (data_feasible[i][3] >= data_feasible[j][3]) and (data_feasible[i][4] >= data_feasible[j][4]):
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
    x1 = (0.07 - 0.0001) * x1_ind / (gridSize) + 0.0001
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
    x2 = (0.03 - 0.0001) * x2_ind / (gridSize) + 0.0001
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
    x3 = (3 - 1) * x3_ind / (gridSize) + 1
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
