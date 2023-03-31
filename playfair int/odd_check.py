
# check whether the number of characters of the plain text odd or even.
# if even we leave it
# if odd, we should add a letter at the last of the plaintext for example (x), but if the last letter is x,we should add another letter for example (y)


def oddNumber(plaintext):
    if (len(plaintext) % 2 != 0):
        if (plaintext[-1] == 'x'):
            plaintext += 'y'
        else:
            plaintext += 'x'
    return plaintext

