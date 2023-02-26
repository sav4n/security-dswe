# keygenrate step 3
def divide(string):
    return [string[0:32], string[32:64] ] 

print(divide("12345678901234567890123456789012345678901234567890123456789012345678901234"))

# DES 4.a
def drop_parity(string):
    result = string
    for i in range(1,8):
        result = result[:i*8] + result[8*i+1:] 
        print(result+'\n')
    return result
drop_parity("12345678901234567890123456789012345678901234567890123456789012345678901234")