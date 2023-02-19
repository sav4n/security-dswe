import string
import random
#print(string.ascii_lowercase)
asci_map = {}
dec_asci_map = {}
c=0
for i in string.ascii_lowercase:
    asci_map[c]= i 
    c = c+1
c=0

for i in string.ascii_lowercase:
    dec_asci_map[i]= c 
    c = c+1
    
# print(dec_asci_map)
def genrateKey():
    keys = list(range(0,26))
    random.shuffle(keys)
    return keys

def openReadFileText(filename):
    f= open(filename,'r')
    lines= f.read().split('\n')
    # print(lines)
    return lines

def openWriteFileText(filename,lines):
    f= open(filename,'w+')
    lines= f.writelines(lines)
    # print(lines)
    return lines

lines = openReadFileText('names.txt')
key = genrateKey()
# print(key)

def encMono(lines,key):
    output = ""
    for line in lines:
        line.replace('\n','')
        for char in line:
           output=output+ asci_map[key[dec_asci_map[char]]]
        output = output+'\n'
    return output

enc =  encMono(lines,key)

print(enc)
# openWriteFileText('ciphertext.txt',enc)

lines = openReadFileText('names.txt')
key = [10, 6, 21, 24, 1, 22, 11, 4, 9, 0, 25, 19, 18, 14, 15, 7, 20, 5, 12, 8, 13, 2, 16, 3, 17, 23]
enc =  encMono(lines,key)

print(enc)
openWriteFileText('ciphertext1.txt',enc)

# enc = enc.split('\n')
# def decMono(cipher,key):   
#     output= ""
#     for cline in cipher:
#         for char in cline:
#            output=output + asci_map[key.index(dec_asci_map[char])]
#         output = output+'\n'
#     return output

# dec = decMono(enc,key)
# print(dec)