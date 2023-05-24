keySize = 256

def text_To_Indexes(text):# 'ABC' agore bo [65, 66, 67]
    a = []
    for i in range(len(text)):
           a.append(ord(text[i]))
    return a
#print(text_To_Indexes('ABC'))



def indexes_to_text(number):# ['65','66','67'] agore bo 'ABC'
    a = []
    for i in range(len(number)):
        a.append(chr(int(number[i])))
    return a
#print(indexes_to_text(['65','66','67']))


 
def encrypt(message, key):# bo nmuna message = 'ABC' ,key = 1 >>> agordre bo 'BCD'
    a = []
    indexes = text_To_Indexes(message)
    for i in range(len(indexes)):
        a.append((int(indexes[i])+key) % keySize)
    return indexes_to_text(a)


def decrypt(message, key):# bo nmuna message = 'BCD' ,key = 1 >>> agordre bo 'ABC'
    a = []
    indexes = text_To_Indexes(message)
    for i in range(len(indexes)):
        a.append((int(indexes[i])-key) % keySize)
    return indexes_to_text(a)


def bruteForce(message):# hamu key akan print aka, ser akain bzanin kamayan ma3nai haya
    for key in range(keySize):
        decryptedText = decrypt(message, key)
        print("Decrypted text: ",decryptedText,", Key: ",key)
        