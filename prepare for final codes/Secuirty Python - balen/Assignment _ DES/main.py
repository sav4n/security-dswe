from DES_EXPAND_SWAPER_FUNCTION import swap_xor ,d_expansion_box
from conversion_32_to_48 import sbox_calculation, compression_box_calc
from Initial_Final_Permutation import initalPermutation, finalPermutation
from DES_functions import des_test, divide_key
from Group6 import convert_character_to_bits,shift_bits,convert_bits_to_character
from functions import kxor,divide_32_bits,straight_permutation,drop_parity


def encrypt_aes(message, key):
    #KEY USED FOR ENCRYPTION
    print("\n\key",key)
    
    #CONVERT (8 CHARACTERS) TO (64 BITS)
    string_64bits = convert_character_to_bits(key);
    print("len(string_64bits)",len(string_64bits),string_64bits)
    
    #DROP PARITY BIT (64 BITS) TO (58 BITS)
    key_afterDroping_parityBit_58bit = drop_parity(string_64bits)
    print("len(key_afterDroping_parityBit_58bit)",len(key_afterDroping_parityBit_58bit),key_afterDroping_parityBit_58bit)
    print()
    arrayOf_subkeys = []
    for roundNumber in range(16):
        print("roundNumber",roundNumber)
        
        #SPLIT (56 BITS) TO TWO (28 BITS)
        arrayOf_28bits = divide_key(key_afterDroping_parityBit_58bit)
        key_1_28bit = arrayOf_28bits[0]
        key_2_28bit = arrayOf_28bits[1]
        print("len(key_1_28bit)",len(key_1_28bit),key_1_28bit)
        print("len(key_2_28bit)",len(key_2_28bit),key_2_28bit)
        
        #SHIFT TWO (28 BITS)
        shifted_key_1_28bit = shift_bits(key_1_28bit, roundNumber)
        shifted_key_2_28bit = shift_bits(key_2_28bit, roundNumber)
        print("len(shifted_key_1_28bit)",len(shifted_key_1_28bit),shifted_key_1_28bit)
        print("len(shifted_key_2_28bit)",len(shifted_key_2_28bit),shifted_key_2_28bit)
        
        
        #COMPRESSION BOX (56 BITS) TO (48 BITS)
        compression_box = [39, 2, 29, 13, 23, 1, 53, 43, 38, 5, 19, 37, 3, 20, 24, 50, 22, 35, 42, 10, 32, 21, 8, 30, 55, 25, 26, 9, 4, 54, 16, 27, 49, 41, 45, 6, 51, 46, 31, 15, 0, 47, 17, 36, 14, 44, 48, 7, 12, 18, 40, 28, 34, 11, 52, 33]
        compressed_key_48bits = compression_box_calc(shifted_key_1_28bit + shifted_key_2_28bit,compression_box)
        print("len(compressed_key_48bits)",len(compressed_key_48bits),compressed_key_48bits)
        arrayOf_subkeys.append(compressed_key_48bits)
        print()
    
    
    print("len(arrayOf_subkeys)",len(arrayOf_subkeys),arrayOf_subkeys)
    
    
    
    
    #message to be encrypted
    print("\n\nmessage",message)
    
    #SPLIT MESSAGE INTO "8 CHARACTER BLOCKS", FILL THE REST WITH 0 IF LESS OR MORE
    blocksOf_8_characters = des_test(message)
    print("len(blocksOf_8_characters)",len(blocksOf_8_characters),blocksOf_8_characters)
    print()
    for blockNumber in range(len(blocksOf_8_characters)):
        print("blockNumber",blockNumber)
        
        blocksOf_8_character = blocksOf_8_characters[blockNumber]
        
        #CONVERT (8 CHARACTERS) TO (64 BITS)
        string_64bits = convert_character_to_bits(blocksOf_8_character);
        print("len(string_64bits)",len(string_64bits),string_64bits)
    
        #INITAL PERMUTATION
        inital_permutated_64bits, arrayOfNumbers, arrayOfNumbersShuffled = initalPermutation(string_64bits)
        print("len(inital_permutated_64bits)",len(inital_permutated_64bits),inital_permutated_64bits)
        print()
        string_64bits = inital_permutated_64bits
        for roundNumber in range(1):
            print("roundNumber",roundNumber)
            
            #SPLIT (64 BITS) TO TWO (32 BITS)
            arrayOf_32bits = divide_32_bits(string_64bits)
            left_32bit = arrayOf_32bits[0]
            right_32bit = arrayOf_32bits[1]
            print("len(left_32bit)",len(left_32bit),left_32bit)
            print("len(right_32bit)",len(right_32bit),right_32bit)
            
      
            ########START OF F          
            #Expansion D-box
            string_48bits_expanded = d_expansion_box(right_32bit)
            print("len(string_48bits_expanded)",len(string_48bits_expanded),string_48bits_expanded)
            
            #XOR (rightPart48 and sub-key48)
            string_48bits_xor = kxor(string_48bits_expanded,arrayOf_subkeys[roundNumber]) 
            print("len(string_48bits_xor)",len(string_48bits_xor),string_48bits_xor)
            
            #S-Box (48 BITS) TO (32 BITS)
            sbox = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
            string_32bits_after_SBOX = sbox_calculation(string_48bits_xor,sbox)
            print("len(string_32bits_after_SBOX)",len(string_32bits_after_SBOX),string_32bits_after_SBOX)
            
            #Straight D-box
            p_box = [
                  16, 7, 20, 21, 29, 12, 28, 17,
                  1, 15, 23, 26, 5, 18, 31, 10,
                  2, 8, 24, 14, 32, 27, 3, 9,
                  19, 13, 30, 6, 22, 11, 4, 25]
            string_32bits_afterStraighPermutation = output_block = straight_permutation(string_32bits_after_SBOX,p_box)
            print("len(string_32bits_afterStraighPermutation)",len(string_32bits_afterStraighPermutation),string_32bits_afterStraighPermutation)        
            ########END OF F
            
            #XOR (left_32bit and 'F' result32bit)
            string_32bits_xor = kxor(left_32bit,string_32bits_afterStraighPermutation) 
            print("len(string_32bits_xor)",len(string_32bits_xor),string_32bits_xor)
            
            left_32bit = right_32bit
            right_32bit = string_32bits_xor
            string_64bits = left_32bit + right_32bit
            print()
            
        #FINAL PERMUTATION
        inital_permutated_64bits = string_64bits
        final_permutated_64bits = finalPermutation(inital_permutated_64bits, arrayOfNumbersShuffled)
        print("len(final_permutated_64bits)",len(final_permutated_64bits),final_permutated_64bits)
        
        encryptedBlock =convert_bits_to_character(final_permutated_64bits)
        print("len(encryptedBlock)",len(encryptedBlock),encryptedBlock)
        print()
        return(encryptedBlock)




message = "abcdefgh"
key = "kurdkurd"
encrypted_text = encrypt_aes(message, key)
print(encrypted_text)



