import random

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print("Normal Alphabet",alphabet)

key = random.sample(alphabet, len(alphabet))#takes a string or list, shuffles it and then returns a list 
print("Randomized Alphabet",key)


def encrypt(listOfLines):
    cipherFile = open('Cipher.txt', 'w')
    for line in listOfLines:
        for character in line:
            if(character==" "):#When encountering space, we write it as it is
                cipherFile.write(character)
            for i in range(len(alphabet)):
                if(character==alphabet[i]):
                    cipherFile.write(key[i])
                elif(character==alphabet[i].lower()):#using .lower will make sure characters from both cases are accounted for
                    cipherFile.write(key[i].lower())
        cipherFile.write('\n')
    cipherFile.close()



namesFile = open('Names.txt', 'r')
lines = namesFile.readlines()#real all lines at once
encrypt(lines)

