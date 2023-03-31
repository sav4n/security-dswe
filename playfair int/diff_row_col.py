# this is assuming that indexes of both input characters are initialized,and defined previously.
# for the purpose of running this code, the key is statically defined.
# this code only works if, the charachters are set on different rows, and columns.
import same_col as con
import numpy as np

key = [['d', 'a', 't', 'b', 'c'],
       ['e', 'f', 'g', 'h', 'i'],
       ['k', 'l', 'm', 'n', 'o'],
       ['p', 'q', 'r', 's', 'u'],
       ['v', 'w', 'x', 'y', 'z']]


def diff_row_col(key, i1, j1, i2, j2):
    result = key[i1][j2]+key[i2][j1]
    return result


#  this code is overwrited of above code because they did not work well according to requirements
def different_row_col(key, pair):
    key = np.array(key)
    cipher = ""

    j = checkPairsWithKey(key, pair[1], isCol=True)
    i = checkPairsWithKey(key, pair[0])
    # cipher.append(key[i][j])
    cipher += key[i][j]
    j = checkPairsWithKey(key, pair[0], isCol=True)
    i = checkPairsWithKey(key, pair[1])
    cipher += key[i][j]

    return cipher


def checkPairsWithKey(key, char, isCol=False):
    key = np.array(key)
    for i in range(len(key)):
        if isCol:
            index = con.isContain(char, key[i, :])
            if index != -1:
                # print(index)
                # print(key[i][index])
                return index
        else:
            index = con.isContain(char, key[:, i])
            if index != -1:
                # print(index)
                # print(key[index][i])
                return index
