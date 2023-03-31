import playfire_convert_j_to_i
import odd_check
import Playfair_Check_Adjacent_2a
import create_key
import pairs
import same_col
import diff_row_col

# This is the main function

# message = "datasecurityjournal"
message = input("enter the message: ")

# check if there are two adjacent letters
adj = Playfair_Check_Adjacent_2a.check_adjacent_letters(message)


# we check if the message is odd or even and we add X if it is odd
odd = odd_check.oddNumber(adj)


#  we change all the J's to I's and we conver it to array
array, text = playfire_convert_j_to_i.playfair_converter(odd)


# create the key matrix
x = input("with key, yes or no: ")
key = []
if (x == "yes"):
    y = input("enter the key: ")
    key = create_key.create_key(y.upper())
else:
    key = create_key.create_key(array)


# make pairs of the message
pairs = pairs.pairNumbers(text)


# loop through the pairs
def encryption(pairs, key):
    cipher = []
    for i in range(len(pairs)):
        if same_col.onTheSameColumn(pairs[i], key) != False:
            cipher.append(same_col.onTheSameColumn(pairs[i], key))
        elif same_col.onTheSameRow(pairs[i], key) != False:
            cipher.append(same_col.onTheSameRow(pairs[i], key))
        else:
            cipher.append(
                diff_row_col.different_row_col(key, pairs[i]))
    return cipher


print(encryption(pairs, key))
