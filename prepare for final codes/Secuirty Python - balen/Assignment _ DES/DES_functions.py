
def key_generation_key_test(key):
    # this is checking if the key is 8 characters, if not then won't be accepted
    b = True
    if len(key) > 8:
        print("Size is bigger, please enter 8 chars only ")
        b = False
    elif len(key) < 8:
        print("Size is smaller, please enter 8 chars ")
        b = False
    if b is False:
        key = input("enter key again ")
        key_generation_key_test(key)
    else:
        return b



def des_split_data(msg):
    # splits a string for 8 characters each
    # this function should be called before the DES return function.
    n = 8
    data = [msg[i:i + n] for i in range(0, len(msg), n)]
    return data




def des_return(msg):
    # there is no case where the message is more than 8 characters
    # because the split function return data into 8 or less length each
    # this function is prepared to be run into another function
    # calling this function without splitting data first will return undesired output
    if len(msg) == 8:
        return msg
    elif len(msg) < 8:
        for i in range(8 - len(msg)):
            # Adding zeros to the data as a padding.
            # anything might be added
            msg += "0"
        return msg
    


def des_test(msg):
    # checks if the message is 8 chars, if not split and then return all parts each 8 character
    data = des_split_data(msg)
    length = len(data)
    for i in range(length):
        data[i] = des_return(data[i])
    return data




def divide_key(key):
    # this function is assuming that the key is 8 characters
    # this function is called after the key length is checked to be 8 characters.
    length = len(key)
    result = list(range(2))
    # first part
    result[0] = key[:length // 2]
    # second part
    result[1] = key[length // 2:]
    return result



