
def create_key(secretKey=[]):
    # we are replacing 'J' with 'I' in all our cases

    matrix = [[""] * 5 for i in range(5)]  # 2-d matrix
    increment = 0
    if (secretKey == []):  # without key >> simply from A to Z
        for i in range(5):
            for j in range(5):
                if (chr(ord('A')+increment) == 'J'):
                    increment = increment+1
                matrix[i][j] = chr(ord('A')+increment)
                increment = increment+1
    else:  # with key
        incrementSecretKey = 0
        for i in range(5):
            for j in range(5):
                # check for duplicate characters in secretKey, if found go to next one
                while incrementSecretKey < len(secretKey) and any(secretKey[incrementSecretKey] in x for x in matrix):
                    incrementSecretKey = incrementSecretKey+1
                if (incrementSecretKey < len(secretKey)):  # use all characters from secretKey
                    if (secretKey[incrementSecretKey] == 'J'):
                        incrementSecretKey = incrementSecretKey+1
                    matrix[i][j] = secretKey[incrementSecretKey]
                    incrementSecretKey = incrementSecretKey+1
                else:  # Go from A to Z after using all secretKey characters
                    while chr(ord('A')+increment) in secretKey:
                        increment = increment+1
                    if (chr(ord('A')+increment) == 'J'):
                        increment = increment+1
                    matrix[i][j] = chr(ord('A')+increment)
                    increment = increment+1
    return matrix


# how to use
# without key >> [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']]
secret = create_key()
# with key >> [['Q', 'W', 'A', 'B', 'C'], ['D', 'E', 'F', 'G', 'H'], ['I', 'K', 'L', 'M', 'N'], ['O', 'P', 'R', 'S', 'T'], ['U', 'V', 'X', 'Y', 'Z']]
secret = create_key("QWQ")
# with key >> [['Q', 'W', 'A', 'B', 'C'], ['D', 'E', 'F', 'G', 'H'], ['I', 'K', 'L', 'M', 'N'], ['O', 'P', 'R', 'S', 'T'], ['U', 'V', 'X', 'Y', 'Z']]
secret = create_key(['Q', 'W', 'Q'])
# print(secret)
