import numpy as np

########################################## Functions
def create_key(secretKey = []):
    # we are replacing 'J' with 'I' in all our cases
    matrix = [[""]* 5 for i in range(5)] # 2-d matrix
    increment = 0
    if(secretKey == []): # without key >> simply from A to Z 
        for  i in range(5):
             for  j in range(5):
                 if(chr(ord('A')+increment) == 'J'):
                      increment = increment+1
                 matrix[i][j] = chr(ord('A')+increment)
                 increment = increment+1
    else: # with key
        incrementSecretKey = 0
        for  i in range(5):
             for  j in range(5): 
                 while incrementSecretKey < len(secretKey) and any(secretKey[incrementSecretKey] in x for x in matrix): # check for duplicate characters in secretKey, if found go to next one
                    incrementSecretKey = incrementSecretKey+1                   
                 if(incrementSecretKey < len(secretKey)): # use all characters from secretKey 
                     if(secretKey[incrementSecretKey]  == 'J' ):
                         incrementSecretKey = incrementSecretKey+1
                     matrix[i][j] = secretKey[incrementSecretKey]
                     incrementSecretKey = incrementSecretKey+1
                 else: # Go from A to Z after using all secretKey characters
                     while chr(ord('A')+increment) in secretKey:
                         increment = increment+1
                     if(chr(ord('A')+increment) == 'J'):
                        increment = increment+1
                     matrix[i][j] = chr(ord('A')+increment)
                     increment = increment+1
    return matrix

def playfair_converter(text):
    array=list(text)
    for i in range (0,len(array)):
        if(array[i]=='J'):
            array[i]='I'
    text = ""
    for character in array: #@# ADDED THIS
        text += character
    return text

def oddNumber (plaintext): 
    if(len(plaintext)%2!=0):
        if(plaintext[-1]=='X'):
           plaintext+='Y'
        else:
            plaintext+='X'
    return plaintext

def check_adjacent_letters(message):
  message=message.upper()
  message = [x for x in message]
  i = 0
  while(i<len(message)-1):
    if(message[i]==message[i+1]):
        if(message[i]=='X'):
           message.insert(i+1,'Y')
        else:
           message.insert(i+1,'X')       
    i=i+2
  if(len(message)%2 !=0):
     if(message[len(message)-1]=='X'):
      message.append('Y')
  return ''.join(message)

def pairNumbers(text):
    pairs = []
    leng = len(text)
    for i in range(0,leng,2):
        pairs.append(text[i] + text[i+1])
    return pairs
 
    
 
#@# CREATED this function
# checks if characters of each pair are on the same row, column or neither, then gets the correspodning ciphered character 
def encrypt(keyMatrix, pairs): 
    cipher = []
    for k in range(0, len(pairs)):
        for i in range(5):
            for j in range(5): # find i and j for each character in the given pair
                if(keyMatrix[i][j] == pairs[k][0]):
                    position_x_1 = i
                    position_y_1 = j
                if(keyMatrix[i][j] == pairs[k][1]):
                    position_x_2 = i
                    position_y_2 = j
        character1 = ""
        character2 = ""
        # if same row
        if position_x_1 == position_x_2: 
            if position_y_1 == 4:
                character1 = keyMatrix[position_x_1][0]
            else:
                character1 = keyMatrix[position_x_1][position_y_1+1]
            if position_y_2 == 4:
                character2 = keyMatrix[position_x_2][0]
            else:
                character2 = keyMatrix[position_x_2][position_y_2+1]
        # if same column
        elif position_y_1 == position_y_2: 
            if position_x_1 == 4:
                character1 = keyMatrix[0][position_y_1]
            else:
                character1 = keyMatrix[position_x_1+1][position_y_1]
            if position_x_2 == 4:
                character2 = keyMatrix[0][position_y_2]
            else: 
                character2 = keyMatrix[position_x_2+1][position_y_2]
        # neither row or column, then it forms a rectangle
        else: 
            character1 = keyMatrix[position_x_1][position_y_2]
            character2 = keyMatrix[position_x_2][position_y_1]
        cipher.append(character1 + character2)
    return cipher
########################################## Functions

################# Integration 
secretKey = input("Secret key: ").upper() # get secret key
keyMatrix = create_key(secretKey) # create secret key alphabet matrix
print("Key Matrix: ",keyMatrix) 

message = input("Message: ").upper() # get message
message = message.replace(" ","") # remove space
modifiedMessage = playfair_converter(message) # replace all j with i
modifiedMessage = check_adjacent_letters(modifiedMessage) # check adjacent characters if they are the same, add filler characters if they are
modifiedMessage = oddNumber(modifiedMessage) # if odd add filler charatcer at the end of the message 
pairs  = pairNumbers(modifiedMessage) # split message and form pairs
print("Pairs: ",pairs)

pairs_encryptedMessage = encrypt(keyMatrix, pairs) # does the encryption of all pairs using previously created secret key matrix

CipherText = ""
for i in pairs_encryptedMessage:
    CipherText += i
print("Cipher text: ",CipherText)
################# Integration 

########################################## Below functions were given but we didn't use
def makeEven(message): # not used
    if(len(message)%2 != 0):
        message=message+'x'
    return message


def diff_row_col(key,i1,j1,i2,j2): # not used
    result=key[i1][j2]+key[i2][j1]
    return result

def samerow(charA,charB): # not used
    matrix=[['E','X', 'A','M','P'],['L','B','C','D','F'],['G','H','I', 'K', 'N'],['O', 'Q', 'R','S','T'],['U','V','W','Y','Z']]
    for i in range (len(matrix)):
        for j in range(len (matrix[0])):
            if(matrix[i][j]==charA):
                a=[i,j]
            if(matrix[i][j]==charB):
                b=[i,j]
    print(a[1],b[1])             
    if(a[0]==b[0]):
        if(a[1]==4):
            matrix[a[0]][a[1]]=matrix[a[0]][0]
            matrix[b[0]][b[1]]=matrix[b[0]][b[1]+1]
        elif(b[1]==4):
            matrix[b[0]][b[1]]=matrix[b[0]][0]
            matrix[a[0]][a[1]]=matrix[a[0]][a[1]+1]
        else:
            matrix[a[0]][a[1]]=matrix[a[0]][a[1]+1]
            matrix[b[0]][b[1]]=matrix[b[0]][b[1]+1]
    return matrix


def isContain(element,array): # not used
    for i in range(len(array)):
        if array[i]==element:
            return i
    return -1


def onTheSameColumn(pair,matrix): # not used
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if pair[0]==matrix[j][i] and isContain(pair[1],matrix[:,i])>-1:
                cipher=matrix[(j+1)%5][i]+matrix[(isContain(pair[1],matrix[:,i])+1)%5][i]
                return cipher;
    
    return False
########################################## Above functions were given but we didn't use