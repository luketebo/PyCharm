import pandas as pd
# import matplotlib
import numpy as np
from collections import Counter


# 处理数据
def read_file():
    df = pd.read_excel('data.xlsx')
    df_li = df.values.tolist()
    result_1 = []
    result_2 = []
    result_3 = []
    for s_li in df_li:
        result_1.append(s_li[3])
        result_2.append(s_li[10])
        result_3.append(s_li[17])
    del result_1[0]
    del result_2[0]
    del result_3[0]
    return result_1, result_2, result_3


# 数据处理
def deal_data():
    a, b, c = read_file()
    count = set()

    list_new = []
    for item in a:
        list_new.append(item)
    for item in b:
        list_new.append(item)
    for item in c:
        list_new.append(item)
    print(Counter(list_new))


    pass


if __name__ == '__main__':
    # read_file()
    deal_data()
    pass
