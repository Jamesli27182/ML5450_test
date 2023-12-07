import numpy as np
import pandas
df = pandas.read_csv('music_dataset.csv')
df = pandas.DataFrame(df)
V_1 = np.array(df.V1)
V_2 = np.array(df.V2)
V_3 = np.array(df.V3)
V_4 = np.array(df.V4)
V_tot = np.add(np.add(V_1,V_2),np.add(V_3,V_4))
V_tot = V_tot/4
A_1 = np.array(df.A1)
A_2 = np.array(df.A2)
A_3 = np.array(df.A3)
A_4 = np.array(df.A4)
A_tot = np.add(np.add(A_1,A_2),np.add(A_3,A_4))
A_tot = A_tot/4
# len(A_tot)
A_tot = A_tot.reshape(len(A_tot),1)
V_tot = V_tot.reshape(len(V_tot),1)
# print(A_tot)
# print(V_tot)
A_V_point = np.concatenate((V_tot,A_tot),axis=1)
print(A_V_point)
def cal_dis(A , B) -> float:# 2x1 array input
    dis = ((A[0]-B[0])**2+(A[1]-B[1])**2)**0.5
    return dis

def to_get_ave(A_): #input a x b array
    a,b = A_.shape
    New_A = np.zeros(a)
    for i in range(a):
        for j in range(b):
            New_A[i] = 1/b*A_[i][j]+New_A[i]
    New_A = New_A.reshape(a,1)
    return New_A

def to_find_cloest(A,B) -> int: #A: 2 x 1,B; n x m
    b_r,b_c = B.shape
    dis_vec = np.zeros(b_r)
    index_num = 0
    for i in range(b_r):
        dis_vec[i] = cal_dis(A,B[i])
    min_dis = min(dis_vec)
    for i in range(b_r):
        if dis_vec[i] == min_dis:
            index_num = i
            break
    return index_num,min_dis

