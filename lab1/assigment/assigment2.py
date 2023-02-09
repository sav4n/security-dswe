import  assigmentFun

text = input("Enter Message: ")
key = input("Enter Key: ")

cipher = ""
for i in text:
    cipher = cipher + chr(assigmentFun.enc(ord(i),int(key)))
print(cipher)

cipher = input("Enter Cipher: ")
key = input("Enter Key: ")

text  = ""
for i in cipher:
    text = text + chr(assigmentFun.dec(ord(i),int(key)))
print(text)


print('brute - force')
cipher = input("Enter Cipher: ")
     
text  = ""
for i in range(0,256):
    for c in cipher:
        text = text + chr(assigmentFun.dec(ord(c),int(i)))
    print('\n'+ f" text : {text} , key {i}") 
    text=""
