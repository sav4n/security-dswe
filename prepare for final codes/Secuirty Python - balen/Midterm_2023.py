import numpy as np
#Balen abdulrahman
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
        if(array[i]=='F'):
            array[i]='H'
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
    
############
def caesar(message, secretKeyInt):
    secretKeyInt = secretKeyInt%26
    result = ""
    for i in range(len(message)):
        a = (ord(message[i])+secretKeyInt)
        if(a > ord("z")):
            a = a - ord("z") 
            a = a + ord("a") 
        if(a > ord("Z") and a < ord("a")):
            a = a - ord("Z") 
            a = a + ord("A") 
        result = result + chr(a)     
    return(result)   
############

################# Integration 
def encryptMessage(message, secretKey, secretKeyInt):
    message = caesar(message, secretKeyInt)
    print("c",message)

    secretKey = secretKey.upper() 
    keyMatrix = create_key(secretKey) # create secret key alphabet matrix
    print("keyMatrix: ",keyMatrix)
    message = message.upper()
    print(message)
    message = message.replace(" ","") # remove space
    modifiedMessage = playfair_converter(message) # replace all f with h
    print(modifiedMessage)
    modifiedMessage = check_adjacent_letters(modifiedMessage) # check adjacent characters if they are the same, add filler characters if they are
    print(modifiedMessage)
    modifiedMessage = oddNumber(modifiedMessage) # if odd add filler charatcer at the end of the message 
    print(modifiedMessage)
    pairs  = pairNumbers(modifiedMessage) # split message and form pairs
    print("Pairs: ",pairs)
    
    pairs_encryptedMessage = encrypt(keyMatrix, pairs) # does the encryption of all pairs using previously created secret key matrix
    
    CipherText = ""
    for i in pairs_encryptedMessage:
        CipherText += i
    return CipherText

message = "DDaxzZAXx"
secretKey = ""
secretKeyInt = 5
encryptedMessage = encryptMessage(message, secretKey, secretKeyInt)
print("Cipher text: ",encryptedMessage)

