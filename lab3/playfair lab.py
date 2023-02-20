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
