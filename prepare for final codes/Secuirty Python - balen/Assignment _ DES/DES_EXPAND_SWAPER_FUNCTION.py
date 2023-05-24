import numpy as np
import operator as op

"""
Spyder Editor

This is a temporary script file.
"""


"""
convertTextToarray to convert 32 bit  to matrix shape 8 * 6ex.
text : string
matrix :[[s,t,r][i,n,g]]

"""





def convertTextToBinary(text):
    b = ' '.join(map(bin, bytearray(text, 'utf8')))
    b = b.replace("b", "")
    return b


def isBinary(txt):
    binary = "10"
    for char in txt:
        if char not in binary:
            return False
    return True

def checkBinaryAndText(text):
    if len(text) != 4 and not isBinary(text):
        print('Text must be 4 character')
        return False
    elif len(text) != 32 and isBinary(text):
        print('digits must be 32 bit')
        return False
    return True


def convertTextToarray(txt):
    if not checkBinaryAndText(txt):
        return
    checkBinaryAndText(txt)
    array = np.empty((8, 4), dtype='<U10')
    count = 0
    binary = txt
    if not isBinary(txt):
        binary = convertTextToBinary(txt).replace(' ', '')

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            array[i][j] = binary[count]
            count = count + 1
    return array


def d_expansion_box(text):
    if not checkBinaryAndText(text):
        return
    array = convertTextToarray(text)
    exp_array = np.empty((8, 6), dtype="<U10")

    exp_array[:, 1:exp_array.shape[1] - 1] = array
    exp_array[:, 0] = np.roll(array[:, array.shape[1] - 1], 1)
    exp_array[:, exp_array.shape[1] - 1] = np.roll(array[:, 0], 1)
    exp_array = exp_array.flatten();
    return exp_array



def swap_xor(left, right):
    if not checkBinaryAndText(left) or not checkBinaryAndText(right):
        return
    le = left
    ri = right
    if not isBinary(left) and not isBinary(right):
        le = convertTextToBinary(left)
        ri = convertTextToBinary(right)

    new_arr = ""
    for i in range(len(le)):
        if le[i] == ri[i]:
            new_arr += "0"
        else:
            new_arr += "1"
    return new_arr


# swap_xor('10011001100110011001100110011010', '10011001100110011001100110011010')
# d_expansion_box('10011001100110011001100110011010')

