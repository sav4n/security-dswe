import  fun
import string

key =3 
lang = {
}
decmap = {
}
c = 0  
for alpha in string.ascii_lowercase:
    lang[alpha] = c
    c+=1
c=0
for alpha in string.ascii_lowercase:
    decmap[c] = alpha
    c+=1

text = input("Enter Message: ")
key = input("Enter Key: ")

cipher = ""
for i in text:
    cipher = cipher + decmap[fun.enc(lang[i],int(key))]
print(cipher)

cipher = input("Enter Cipher: ")
key = input("Enter Key: ")

text  = ""
for i in cipher:
    text = text + decmap[fun.dec(lang[i],int(key))]
print(text)


print('brute - force')
cipher = input("Enter Cipher: ")
key = input("Enter Key: ")


     
text  = ""
for i in range(0,26):
    for c in cipher:
        text = text + decmap[fun.dec(lang[c],int(i))]
    print('\n'+ f" text : {text} , key {i}") 
    text=""



    # key 16  focus

    