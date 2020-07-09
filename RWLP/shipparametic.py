# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 03:16:49 2020

@author: taiki
"""

import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D​

def cal_f1(x1, x2, x3, x4, x5, x6):
    x_L = x1
    x_B = x2
    x_D = x3
    x_T = x4
    x_Vk = x5
    x_CB = x6
    displacement = 1.025 * x_L * x_B * x_T * x_CB
    V = 0.5144 * x_Vk
    pg = 9.8065
    Fn = V / (pg * x_L) ** 0.5
    a = (4977.06 * x_CB * x_CB) - (8105.61 * x_CB) + 4456.51
    b = (-10847.2 * x_CB * x_CB) + (12817.0 * x_CB) - 6960.32
    
    power = ((displacement ** (2.0/3.0)) * (x_Vk ** 3.0)) / (a + (b * Fn))
    outfit_weight = 1.0 * (x_L ** 0.8) * (x_B ** 0.6) * (x_D ** 0.3) * (x_CB ** 0.1)
    steel_weight = 0.034 * (x_L ** 1.7) * (x_B ** 0.7) * (x_D ** 0.4) * (x_CB ** 0.5)
    machinery_weight = 0.17 * (power ** 0.9)
    light_ship_weight = steel_weight + outfit_weight + machinery_weight
    
    ship_cost = 1.3 * ((2000.0 * (steel_weight ** 0.85))  + (3500.0 * outfit_weight) + (2400.0 * (power ** 0.8)))
    capital_costs = 0.2 * ship_cost
    DWT = displacement - light_ship_weight
    running_costs = 40000.0 * (DWT ** 0.3)
    round_trip_miles = 5000.0
    sea_days = (round_trip_miles / 24.0) * x_Vk
    handling_rate = 8000.0
    
    daily_consumption = ((0.19 * power * 24.0) / 1000.0) + 0.2
    fuel_price = 100.0
    fuel_cost = 1.05 * daily_consumption * sea_days * fuel_price
    port_cost = 6.3 * (DWT ** 0.8)
    fuel_carried = daily_consumption * (sea_days + 5.0)
    miscellaneous_DWT = 2.0 * (DWT ** 0.5)
    
    cargo_DWT = DWT - fuel_carried - miscellaneous_DWT
    port_days = 2.0 * ((cargo_DWT / handling_rate) + 0.5)
    RTPA = 350.0 / (sea_days + port_days)
    voyage_costs = (fuel_cost + port_cost) * RTPA
    annual_costs = capital_costs + running_costs + voyage_costs
    annual_cargo = cargo_DWT * RTPA
    ans = annual_costs / annual_cargo
    return ans

def cal_f2(x1, x2, x3, x4, x5, x6):
    x_L = x1
    x_B = x2
    x_D = x3
    x_T = x4
    x_Vk = x5
    x_CB = x6
    displacement = 1.025 * x_L * x_B * x_T * x_CB
    V = 0.5144 * x_Vk
    pg = 9.8065
    Fn = V / (pg * x_L) ** 0.5
    a = (4977.06 * x_CB * x_CB) - (8105.61 * x_CB) + 4456.51
    b = (-10847.2 * x_CB * x_CB) + (12817.0 * x_CB) - 6960.32
    
    power = ((displacement ** (2.0/3.0)) * (x_Vk ** 3.0)) / (a + (b * Fn))
    outfit_weight = 1.0 * (x_L ** 0.8) * (x_B ** 0.6) * (x_D ** 0.3) * (x_CB ** 0.1)
    steel_weight = 0.034 * (x_L ** 1.7) * (x_B ** 0.7) * (x_D ** 0.4) * (x_CB ** 0.5)
    machinery_weight = 0.17 * (power ** 0.9)
    light_ship_weight = steel_weight + outfit_weight + machinery_weight
    ans = light_ship_weight
    return ans

def cal_f3(x1, x2, x3, x4, x5, x6):
    x_L = x1
    x_B = x2
    x_D = x3
    x_T = x4
    x_Vk = x5
    x_CB = x6
    displacement = 1.025 * x_L * x_B * x_T * x_CB
    V = 0.5144 * x_Vk
    pg = 9.8065
    Fn = V / (pg * x_L) ** 0.5
    a = (4977.06 * x_CB * x_CB) - (8105.61 * x_CB) + 4456.51
    b = (-10847.2 * x_CB * x_CB) + (12817.0 * x_CB) - 6960.32
    
    power = ((displacement ** (2.0/3.0)) * (x_Vk ** 3.0)) / (a + (b * Fn))
    outfit_weight = 1.0 * (x_L ** 0.8) * (x_B ** 0.6) * (x_D ** 0.3) * (x_CB ** 0.1)
    steel_weight = 0.034 * (x_L ** 1.7) * (x_B ** 0.7) * (x_D ** 0.4) * (x_CB ** 0.5)
    machinery_weight = 0.17 * (power ** 0.9)
    light_ship_weight = steel_weight + outfit_weight + machinery_weight
    
    DWT = displacement - light_ship_weight
    round_trip_miles = 5000.0
    sea_days = (round_trip_miles / 24.0) * x_Vk
    handling_rate = 8000.0
    
    daily_consumption = ((0.19 * power * 24.0) / 1000.0) + 0.2
    fuel_carried = daily_consumption * (sea_days + 5.0)
    miscellaneous_DWT = 2.0 * (DWT ** 0.5)
    
    cargo_DWT = DWT - fuel_carried - miscellaneous_DWT
    port_days = 2.0 * ((cargo_DWT / handling_rate) + 0.5)
    RTPA = 350.0 / (sea_days + port_days)
    annual_cargo = cargo_DWT * RTPA
    ans = -annual_cargo
    return ans

def is_feasible(x1, x2, x3, x4, x5, x6):
    ans = False
    x_L = x1
    x_B = x2
    x_D = x3
    x_T = x4
    x_Vk = x5
    x_CB = x6
    displacement = 1.025 * x_L * x_B * x_T * x_CB
    V = 0.5144 * x_Vk
    pg = 9.8065
    Fn = V / (pg * x_L) ** 0.5
    a = (4977.06 * x_CB * x_CB) - (8105.61 * x_CB) + 4456.51
    b = (-10847.2 * x_CB * x_CB) + (12817.0 * x_CB) - 6960.32
    
    power = ((displacement ** (2.0/3.0)) * (x_Vk ** 3.0)) / (a + (b * Fn))
    outfit_weight = 1.0 * (x_L ** 0.8) * (x_B ** 0.6) * (x_D ** 0.3) * (x_CB ** 0.1)
    steel_weight = 0.034 * (x_L ** 1.7) * (x_B ** 0.7) * (x_D ** 0.4) * (x_CB ** 0.5)
    machinery_weight = 0.17 * (power ** 0.9)
    light_ship_weight = steel_weight + outfit_weight + machinery_weight
    
    DWT = displacement - light_ship_weight

    KB = 0.53 * x_T
    BMT = ((0.085 * x_CB - 0.002) * x_B * x_B) / (x_T * x_CB)
    KG = 1.0 + 0.52 * x_D
    if ((x_L / x_B) - 6.0 >= 0) and (-(x_L / x_D) + 15.0 >= 0) and (
                    -(x_L / x_T) + 19.0 >= 0) and (0.45 * (DWT ** 0.31) - x_T >= 0) and (
                                    0.7 * x_D + 0.7 - x_T >= 0) and (
                                            50000.0 - DWT >= 0) and (
                                                    DWT - 3000.0 >= 0) and (
                                                           0.32 - Fn >= 0) and (
                                                                   (KB + BMT - KG) - (0.07 * x_B) >= 0):
        ans = True
    return ans

gridSize = 6

arr = []

for x1_ind in range(gridSize + 1):
    for x2_ind in range(gridSize + 1):
        for x3_ind in range(gridSize + 1):
            for x4_ind in range(gridSize + 1):
                for x5_ind in range(gridSize + 1):
                    for x6_ind in range(gridSize + 1):
                        x1 = (274.32 - 150) * x1_ind / (gridSize) + 150
                        x2 = (32.31 - 20) * x2_ind / (gridSize) + 20
                        x3 = (25 - 13) * x3_ind / (gridSize) + 13
                        x4 = (11.71 - 10) * x4_ind / (gridSize) + 10
                        x5 = (18 - 14) * x5_ind / (gridSize) + 14
                        x6 = (0.75 - 0.63) * x6_ind / (gridSize) + 0.63
                            
                        sol = is_feasible(x1, x2, x3, x4, x5, x6)
                        f1 = cal_f1(x1, x2, x3, x4, x5, x6)
                        f2 = cal_f2(x1, x2, x3, x4, x5, x6)
                        f3 = cal_f3(x1, x2, x3, x4, x5, x6)
                        #print(f'{x1}, {x2}, {x3}, {x4}, {f1}, {f2}, {sol}')
                        arr.append([x1, x2, x3, x4, x5, x6, f1, f2, f3, sol])
                
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

for l in range(len(arr)):
    mapped_arr = map(str, arr[l])
    strTemp = ','.join(mapped_arr) + ",\n"
    if arr[l][9] is True:
        file_feasible.write(strTemp)
        if arr[l][0] == 150:
            file_x1min.write(strTemp)
        elif arr[l][0] == 274.32:
            file_x1max.write(strTemp)
        if arr[l][1] == 20:
            file_x2min.write(strTemp)
        elif arr[l][1] == 32.31:
            file_x2max.write(strTemp)
        if arr[l][2] == 13:
            file_x3min.write(strTemp)
        elif arr[l][2] == 25:
            file_x3max.write(strTemp)
        if arr[l][3] == 10:
            file_x4min.write(strTemp)
        elif arr[l][3] == 11.71:
            file_x4max.write(strTemp)
        if arr[l][4] == 14:
            file_x5min.write(strTemp)
        elif arr[l][4] == 18:
            file_x5max.write(strTemp)
        if arr[l][5] == 0.63:
            file_x6min.write(strTemp)
        elif arr[l][5] == 0.75:
            file_x6max.write(strTemp)
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

data_feasible = np.genfromtxt("solution_feasible.csv", delimiter=",")
X = list(data_feasible[:, 6])
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
        if (data_feasible[i][6] >= data_feasible[j][6]) and (data_feasible[i][7] >= data_feasible[j][7]) and (data_feasible[i][8] >= data_feasible[j][8]):
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
    x1 = (274.32 - 150) * x1_ind / (gridSize) + 150
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
    x2 = (32.31 - 20) * x2_ind / (gridSize) + 20
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
    x3 = (25 - 13) * x3_ind / (gridSize) + 13
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
    x4 = (11.71 - 10) * x4_ind / (gridSize) + 10
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
    x5 = (18 - 14) * x5_ind / (gridSize) + 14
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
    x6 = (0.75 - 0.63) * x6_ind / (gridSize) + 0.63
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
