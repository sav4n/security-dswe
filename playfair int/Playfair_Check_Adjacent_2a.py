message = "HELLOWORRLLXX"


def check_adjacent_letters(message):
    message = message.upper()
    message = [x for x in message]
    i = 0
    while (i < len(message)-1):
        if (message[i] == message[i+1]):
            if (message[i] == 'X'):
                message.insert(i+1, 'Y')
            else:
                message.insert(i+1, 'X')
        i = i+2
    if (len(message) % 2 != 0):
        if (message[len(message)-1] == 'X'):
            message.append('Y')
    return ''.join(message)


# text = check_adjacent_letters(message)
# print(text)
