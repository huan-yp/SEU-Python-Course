# • 二维数组操作
# – 对一个二维数组按照行的中心线翻转，输出新的数组
# – 对一个二维数组按照列的中心线翻转，输出新的数组
# – 假设二维数组的行数和列数相等，输出其对角线上元素组成的数组
# • 二维数组和 Numpy 转化
# – 假设二维数组的元素均为数字，将该二维数组转成 Numpy 向量
# – 将 Numpy 向量转换成二维数组
a = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10],
    [10, 11, 12, 13]
]
print(a[::-1])  # 按行翻转
print([row[::-1] for row in a])  # 按列翻转
print([a[i][i] for i in range(len(a))])  # 对角线元素
import numpy as np
print(np.array(a))  # 转成 Numpy 向量
print(np.array(a).tolist())  # 转成二维数组