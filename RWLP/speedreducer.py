# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 03:16:49 2020

@author: taiki
"""

import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D​

def cal_f1(x1, x2, x3, x4, x5, x6, x7):
    ans = 0.7854 * x1 * (x2 ** 2) * (((10.0 * x3 ** 2) / 3.0) + (14.933 * x3) - 43.0934) - 1.508 * x1 * (x6 ** 2 + x7 ** 2) + 7.477 * (x6 ** 3 + x7 ** 3) + 0.7854 * (x4 * x6 ** 2 + x5 * x7 ** 2)
    return ans

def cal_f2(x1, x2, x3, x4, x5, x6, x7):
    ans = ((745 * x4 / (x2 * x3)) ** 2 + 1.69 * (10 ** 7)) ** 0.5 / (0.1 * (x6 ** 3))
    return ans

def is_feasible(x1, x2, x3, x4, x5, x6, x7):
    ans = False
    if (-(1.0 / (x1 * x2 * x2 * x3)) + 1.0 / 27.0 >= 0) and (
            -(1.0 / (x1 * x2 * x2 * x3 * x3)) + 1.0 / 397.5 >= 0) and (
                    -(x4 ** 3) / (x2 * x3 * (x6 ** 4)) + 1.0 / 1.93 >= 0) and (
                            -(x5 ** 3) / (x2 * x3 * (x7 ** 4)) + 1.0 / 1.93 >= 0) and (
                                    -(x2 * x3) + 40.0 >= 0) and (-(x1 / x2) + 12.0 >= 0) and (
                                            -5.0 + (x1 / x2) >= 0) and (-1.9 + x4 - 1.5 * x6 >= 0) and (
                                                    -1.9 + x5 - 1.1 * x7 >= 0) and (
                                                            ((745 * x4 / (x2 * x3)) ** 2 + 1.69 * (10 ** 7)) ** 0.5 / (0.1 * (x6 ** 3)) <= 1300) and (
                                                                    ((745 * x5 / (x2 * x3)) ** 2 + 1.575 * (10 ** 8)) ** 0.5 / (0.1 * (x7 ** 3)) <= 1100):
        ans = True
    return ans

gridSize = 5

arr = []

for x1_ind in range(gridSize + 1):
    for x2_ind in range(gridSize + 1):
        for x3_ind in range(17, 29):
            for x4_ind in range(gridSize + 1):
                for x5_ind in range(gridSize + 1):
                    for x6_ind in range(gridSize + 1):
                        for x7_ind in range(gridSize + 1):
                            x1 = (3.6 - 2.6) * x1_ind / (gridSize) + 2.6
                            x2 = (0.8 - 0.7) * x2_ind / (gridSize) + 0.7
                            x3 = x3_ind
                            x4 = (8.3 - 7.3) * x4_ind / (gridSize) + 7.3
                            x5 = (8.3 - 7.3) * x5_ind / (gridSize) + 7.3
                            x6 = (3.9 - 2.9) * x6_ind / (gridSize) + 2.9
                            x7 = (5.5 - 5.0) * x7_ind / (gridSize) + 5.0
                            
                            sol = is_feasible(x1, x2, x3, x4, x5, x6, x7)
                            f1 = cal_f1(x1, x2, x3, x4, x5, x6, x7)
                            f2 = cal_f2(x1, x2, x3, x4, x5, x6, x7)

                            #print(f'{x1}, {x2}, {x3}, {x4}, {f1}, {f2}, {sol}')
                            arr.append([x1, x2, x3, x4, x5, x6, x7, f1, f2, sol])
                
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
file_x5min = open('solution_x5min.csv', 'w')
file_x5max = open('solution_x5max.csv', 'w')
file_x6min = open('solution_x6min.csv', 'w')
file_x6max = open('solution_x6max.csv', 'w')
file_x7min = open('solution_x7min.csv', 'w')
file_x7max = open('solution_x7max.csv', 'w')

for l in range(len(arr)):
    mapped_arr = map(str, arr[l])
    strTemp = ','.join(mapped_arr) + ",\n"
    if arr[l][9] is True:
        file_feasible.write(strTemp)
        if arr[l][0] == 2.6:
            file_x1min.write(strTemp)
        elif arr[l][0] == 3.6:
            file_x1max.write(strTemp)
        if arr[l][1] == 0.7:
            file_x2min.write(strTemp)
        elif arr[l][1] == 0.8:
            file_x2max.write(strTemp)
        if arr[l][2] == 17:
            file_x3min.write(strTemp)
        elif arr[l][2] == 28:
            file_x3max.write(strTemp)
        if arr[l][3] == 7.3:
            file_x4min.write(strTemp)
        elif arr[l][3] == 8.3:
            file_x4max.write(strTemp)
        if arr[l][4] == 7.3:
            file_x5min.write(strTemp)
        elif arr[l][4] == 8.3:
            file_x5max.write(strTemp)
        if arr[l][5] == 2.9:
            file_x6min.write(strTemp)
        elif arr[l][5] == 3.9:
            file_x6max.write(strTemp)
        if arr[l][6] == 5.0:
            file_x7min.write(strTemp)
        elif arr[l][6] == 5.5:
            file_x7max.write(strTemp)
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
file_x5min.close()
file_x5max.close()
file_x6min.close()
file_x6max.close()
file_x7min.close()
file_x7max.close()

data_feasible = np.genfromtxt("solution_feasible.csv", delimiter=",")
X = list(data_feasible[:, 7])
"""
Y = list(data_feasible[:, 8])
data_target_min = np.genfromtxt("solution_x1min.csv", delimiter=",")
data_target_max = np.genfromtxt("solution_x1max.csv", delimiter=",")
X_target_min = list(data_target_min[:, 7])
Y_target_min = list(data_target_min[:, 8])
X_target_max = list(data_target_max[:, 7])
Y_target_max = list(data_target_max[:, 8])
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
        if (data_feasible[i][7] >= data_feasible[j][7]) and (data_feasible[i][8] >= data_feasible[j][8]):
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
    x1 = (3.6 - 2.6) * x1_ind / (gridSize) + 2.6
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
    x2 = (0.8 - 0.7) * x2_ind / (gridSize) + 0.7
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
for x3_ind in range(17, 29):
    count = 0
    countn = 0
    countd = 0
    x3 = x3_ind
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
analy_x3 = np.reshape(analy_x3, (12, 4))
analy_x3 = np.transpose(analy_x3)
np.savetxt('x3.csv', analy_x3, delimiter=',')

analy_x4 = np.array([])
for x4_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x4 = (8.3 - 7.3) * x4_ind / (gridSize) + 7.3
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

analy_x5 = np.array([])
for x5_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x5 = (8.3 - 7.3) * x5_ind / (gridSize) + 7.3
    for i in range(len(data_infeasible[:, 4])):
        if data_infeasible[i, 4] == x5:
            count += 1
    for i in range(len(data_nondominated[:, 4])):
        if data_nondominated[i, 4] == x5:
            countn += 1
    for i in range(len(data_dominated[:, 4])):
        if data_dominated[i, 4] == x5:
            countd += 1
    analy_x5 = np.append(analy_x5, (x5, countn, countd, count))
analy_x5 = np.reshape(analy_x5, (gridSize + 1, 4))
analy_x5 = np.transpose(analy_x5)
np.savetxt('x5.csv', analy_x5, delimiter=',')

analy_x6 = np.array([])
for x6_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x6 = (3.9 - 2.9) * x6_ind / (gridSize) + 2.9
    for i in range(len(data_infeasible[:, 5])):
        if data_infeasible[i, 5] == x6:
            count += 1
    for i in range(len(data_nondominated[:, 5])):
        if data_nondominated[i, 5] == x6:
            countn += 1
    for i in range(len(data_dominated[:, 5])):
        if data_dominated[i, 5] == x6:
            countd += 1
    analy_x6 = np.append(analy_x6, (x6, countn, countd, count))
analy_x6 = np.reshape(analy_x6, (gridSize + 1, 4))
analy_x6 = np.transpose(analy_x6)
np.savetxt('x6.csv', analy_x6, delimiter=',')

analy_x7 = np.array([])
for x7_ind in range(gridSize + 1):
    count = 0
    countn = 0
    countd = 0
    x7 = (5.5 - 5.0) * x7_ind / (gridSize) + 5.0
    for i in range(len(data_infeasible[:, 6])):
        if data_infeasible[i, 6] == x7:
            count += 1
    for i in range(len(data_nondominated[:, 6])):
        if data_nondominated[i, 6] == x7:
            countn += 1
    for i in range(len(data_dominated[:, 6])):
        if data_dominated[i, 6] == x7:
            countd += 1
    analy_x7 = np.append(analy_x7, (x7, countn, countd, count))
analy_x7 = np.reshape(analy_x7, (gridSize + 1, 4))
analy_x7 = np.transpose(analy_x7)
np.savetxt('x7.csv', analy_x7, delimiter=',')
