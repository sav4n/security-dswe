import file1 #caesar encryption # Online tool for verification https://www.dcode.fr/ascii-shift-cipher

message = 'ATTACK'
key = 510
print("Message: ",message)

encryptedText = file1.encrypt(message, key)
print("EncryptedText text: ",encryptedText)

decryptedText = file1.decrypt(encryptedText, key)
print("Decrypted text: ",decryptedText)

print("Brute Force Attack") 
challengeText = ('nxuglvwdqarvkd') #3 kurdistanxosha
file1.bruteForce(challengeText)