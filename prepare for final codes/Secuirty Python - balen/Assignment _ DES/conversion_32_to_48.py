
#BINARY AND DECIMAL CONVERSION (DECIMAL TO 4 BITS BINARY)
def bin2dec(n):
    return int(n,2)

def dec2bin(n):
    return bin(n).replace("0b","").rjust(4,'0')
    


#SBOX (48 BITS TO 32 BITS)

sbox = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]


def sbox_calculation(bits48,sbox):
            bits32 = ''
            for i in range(0,len(bits48),6):
                 row_index = bin2dec(bits48[i]+bits48[i+5])
                 col_index = bin2dec(bits48[i+1] + bits48[i+2] + bits48[i+3] + bits48[i+4])
                 num= sbox[row_index][col_index]
                 num = dec2bin(num)
                 bits32 += num   
            return bits32
                



#print("AFTER SBOX:" ,sbox_calculation('010110101101010101010101010101010101010001010100',sbox))







#COMPRESSION BOX (56 BITS TO 48 BITS)


def compression_box_calc(bits56,compression_box):
            bits56 = list(bits56)
            random_bits = list([])
            for i in range(len(bits56)):
                 random_bits.append(bits56[compression_box[i]])
            
            remove_bits_index = [50,41,34,25,22,16,10,7]
            for i in range(len(remove_bits_index)):
                 del random_bits[remove_bits_index[i]]

            return ''.join(random_bits)

            
#compression_box = [39, 2, 29, 13, 23, 1, 53, 43, 38, 5, 19, 37, 3, 20, 24, 50, 22, 35, 42, 10, 32, 21, 8, 30, 55, 25, 26, 9, 4, 54, 16, 27, 49, 41, 45, 6, 51, 46, 31, 15, 0, 47, 17, 36, 14, 44, 48, 7, 12, 18, 40, 28, 34, 11, 52, 33]
#print("AFTER COMPRESSION BOX:", compression_box_calc('01011010110101010101010101010101010101000101010010101101',compression_box))



