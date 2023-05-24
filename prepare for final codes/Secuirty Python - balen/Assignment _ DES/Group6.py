import binascii
 

def convert_bits_to_character(bits):
    characters = ""
    for i in range(8):
        characters+=chr(int(bits[(i*8):(i*8)+8],2))
    return(characters)


def convert_character_to_bits(characters):
    binary =''.join(format(i, '08b') for i in bytearray(characters, encoding='utf-8'))
    return(binary)

#input >>  "abcdefgh" 
#output >> "11000011100010110001111001001100101110011011001111101000"
result = convert_character_to_bits("abcdefgh");
#print(result)




def shift_bits(bits, round_number):
    bits_after_shift = ""
    if(round_number in [1,2,9,16]):
        for i in range(len(bits) -1):
            bits_after_shift = bits_after_shift + bits[i+1]
        bits_after_shift  = bits_after_shift + bits[0]
    else:
        for i in range(len(bits) - 2):
            bits_after_shift = bits_after_shift + bits[i+2]
        bits_after_shift = bits_after_shift + bits[0]
        bits_after_shift = bits_after_shift +  bits[1]
    return bits_after_shift
    

#input >>  "11000011100010110001111001001100101110011011001111101000" 
#output >> "00001110001011000111100100110010111001101100111110100011"
result = shift_bits(result, 3)






