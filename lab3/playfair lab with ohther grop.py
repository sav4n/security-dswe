# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
m = input("Message: ").upper()

def makeEven(message):
    if(len(message)%2 != 0):
        message=message+'x'
    return message

def pairNumbers(text):
    pairs = []
    leng = len(text)
    for i in range(0,leng,2):
        pairs.append(text[i] + text[i+1])
    return pairs
        
text = makeEven(m)
print(text)
pairs  = pairNumbers(text)
print(pairs)

#def checkAdj(array):
#    checked = []
#    flag = none
#    for i in range(0,leng):
#        if(array[i][0] ==  array[i][1] and array[i][1] !='x'):
#            checked.append(array[i][0]+'x')
#            
#    return pairs

# Other Group's code
def check_adjacent_letters(text):
    text = text.upper()
    k = len(text)
    if k % 2 == 0:
       
        for i in range(0, k, 2):
            if(text[i] == 'X' and text[i+1] == 'X'):
               new_word = text[0:i+1] + str('Y') + text[i+1:]
               new_word = check_adjacent_letters(new_word)
            else:
                    
              if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('X') + text[i+1:]
                new_word = check_adjacent_letters(new_word)
                break
              else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if(text[i] == 'X' and text[i+1] == 'X'):
               new_word = text[0:i+1] + str('Y') + text[i+1:]
               new_word = check_adjacent_letters(new_word)
            else:
             if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('X') + text[i+1:]
                new_word = check_adjacent_letters(new_word)
                break
             else:
                new_word = text
    return new_word

print(check_adjacent_letters("".join(pairs)))