import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel(io='F:\code\data\gene\\2_choose.xlsx')
data_name = np.array(data["all-gene_id"])
data_kongbai = np.array(pd.read_excel(io='F:\code\data\gene\\2_choose.xlsx',
                                      usecols=(1, 2, 3, 4, 5, 6, 13, 14 ,15, 16, 17, 18,
                                               25 ,26, 27, 28, 29, 30, 37, 38, 39, 40, 41, 42)))
data_moxing = np.array(pd.read_excel(io='F:\code\data\gene\\2_choose.xlsx',
                                     usecols=(7, 8, 9, 10, 11, 12, 19, 20, 21, 22, 23, 24,
                                              31, 32, 33, 34, 35, 36, 43, 44, 45, 46, 47, 48)))

k_label = [4, 6, 8, 10]
m_label = [4.4, 6.4, 8.4, 10.4]

# 计算均值
def qiujunzhi(x):
    data_mean = []
    for i in range(4):
        data = []
        data.append(x[i * 6: i * 6 + 6])
        data = np.array(data)
        data_mean.append(np.mean(data))

    return data_mean

def qiusandian(x, x_label):
    x_label = np.array(x_label)
    data_4 = x[0: 6]
    data_6 = x[6: 12]
    data_8 = x[12: 18]
    data_10 = x[18: 24]
    data = list(zip(data_4, data_6, data_8, data_10))
    data = np.array(data).T
    data = dict(zip(x_label, data))
    data = pd.DataFrame(data)
    return data

for i in range(len(data_name)):
    data_mean_kongbai = qiujunzhi(data_kongbai[i])
    data_mean_moxing = qiujunzhi(data_moxing[i])
    Kongbai = qiusandian(data_kongbai[i], k_label)
    Moxing = qiusandian(data_moxing[i], m_label)

    # M4, M6, M8, M10 = qiusandian(data_moxing[0])
    plt.title(data_name[i])

    plt.plot(k_label, data_mean_kongbai, color='red', markersize=8, marker='*', linestyle="--")
    plt.plot(m_label, data_mean_moxing, color='blue', markersize=6, marker='^', linestyle="--")
    for j in range(6):
        plt.scatter(k_label, Kongbai.values[j], color='red', s=15)
    for j in range(6):
        plt.scatter(m_label, Moxing.values[j], color='blue', s=15)

    a = max(np.max(data_mean_kongbai), np.max(data_mean_moxing))
    b = 0.14 * (np.mean(data_mean_kongbai)+np.mean(data_mean_moxing))
    c = min(np.min(data_mean_kongbai), np.min(data_mean_moxing))
    # plt.xlim((2, 12))
    plt.ylim((c-b, a+b))
    plt.xlabel("Time after infection (days)")
    plt.ylabel("Gene expression")
    plt.xticks(k_label)
    plt.savefig('F:\code\data\gene\\figure\youxian_{}.png'.format(data_name[i]))
    plt.clf()
    # plt.show()
