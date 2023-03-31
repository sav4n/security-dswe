# -*- coding: utf-8 -*-

import numpy as np
"""
Spyder Editor

This is a temporary script file.
"""

key = np.array([['a', 'b', 'c', 'd', 'e'],
               ['f', 'g', 'h', 'i', 'k'], ['l', 'm', 'n', 'o', 'p'], ['q', 'r', 's', 't', 'u'], ['v', 'w', 'x', 'y', 'z']])


def isContain(element, array):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


def onTheSameColumn(pair, matrix):
    matrix = np.array(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if pair[0] == matrix[j][i] and isContain(pair[1], matrix[:, i]) > -1:
                cipher = matrix[(j+1) % 5][i] + \
                    matrix[(isContain(pair[1], matrix[:, i])+1) % 5][i]
                return cipher

    return False


def list2dToLowerCase(list):
    empty_list = []
    for i in range(len(list)):
        sub_list = []
        for j in list[i]:
            sub_list.append(j.lower())
        empty_list.append(sub_list)
    return empty_list


def onTheSameRow(pair, matrix):
    matrix = np.array(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if pair[0] == matrix[i][j] and isContain(pair[1], matrix[i, :]) > -1:
                cipher = matrix[i][(
                    j + 1) % 5] + matrix[i][(isContain(pair[1], matrix[i, :]) + 1) % 5]
                return cipher

    return False


# print(onTheSameColumn("wb", key))
# print(onTheSameRow("qu", key))
