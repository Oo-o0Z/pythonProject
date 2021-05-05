"""
read adult data set
"""

# !/usr/bin/env python
# coding=utf-8

# Read data and read tree functions for INFORMS data
# attributes ['age', 'work_class', 'final_weight', 'education', 'education_num',
# 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain',
# 'capital_loss', 'hours_per_week', 'native_country', 'class']
# 数据类型有以上这些
# QID ['age', 'work_class', 'education', 'marital_status', 'race', 'sex', 'native_country']
# 准标识符数据的类型有以上这些
# SA ['occupation']
# SA是敏感数据


ATT_NAME = ['age', 'work_class', 'final_weight', 'education',
            'education_num', 'marital_status', 'occupation', 'relationship',
            'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
            'native_country', 'class']
QI_INDEX = [0, 1, 4, 5, 6, 8, 9, 13]#准标识符数据对应的所在行位置，即下文所说数字属性
IS_CAT = [False, True, False, True, True, True, True, True]#？
SA_INDEX = -1#？
__DEBUG = False


def read_data():
    """
    read microdata for *.txt and return read data

    # Note that Mondrian can only handle numeric attribute
    # So, categorical attributes should be transformed to numeric attributes
    # before anonymization. For example, Male and Female should be transformed
    # to 0, 1 during pre-processing. Then, after anonymization, 0 and 1 should
    # be transformed to Male and Female.
    # 请注意，Mondrian只能处理数字属性，
    # 因此，应在匿名化之前将分类属性转换为数字属性。 
    # 例如，在预处理期间，应将“男性”和“女性”转换为0、1。 
    # 然后，在匿名化之后，应将0和1转换为Male和Female。
    """
    QI_num = len(QI_INDEX)
    data = []
    # oder categorical attributes in intuitive order
    # here, we use the appear number
    # 在此以直观的顺序提供分类属性，我们使用显示数字
    intuitive_dict = []
    intuitive_order = []
    intuitive_number = []
    for i in range(QI_num):
        intuitive_dict.append(dict())
        intuitive_number.append(0)
        intuitive_order.append(list())
    data_file = open('data/adult.data', 'rU')
    for line in data_file:
        line = line.strip()
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        # remove empty and incomplete lines
        # only 30162 records will be kept
        # 删除空行和不完整的行，将仅保留30162条记录
        if len(line) == 0 or '?' in line:
            continue
        # remove double spaces
        line = line.replace(' ', '')
        temp = line.split(',')
        # 通过指定分隔符对字符串进行切片，返回各个片段的列表
        ltemp = []
        for i in range(QI_num):
            index = QI_INDEX[i]
            if IS_CAT[i]:
                try:
                    ltemp.append(intuitive_dict[i][temp[index]])
                except KeyError:
                    intuitive_dict[i][temp[index]] = intuitive_number[i]
                    ltemp.append(intuitive_number[i])
                    intuitive_number[i] += 1
                    intuitive_order[i].append(temp[index])
            else:
                ltemp.append(int(temp[index]))
        ltemp.append(temp[SA_INDEX])
        data.append(ltemp)
    return data, intuitive_order
