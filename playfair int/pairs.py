def pairNumbers(text):
    pairs = []
    leng = len(text)
    for i in range(0, leng, 2):
        pairs.append(text[i] + text[i+1])
    return pairs