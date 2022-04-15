from pycipher import Beaufort

print(" ________________________________________________________________________________")
print("|                                                                                |")
print("| Alfabeti : |a|b|c|d|e|f|g|h|i|j|k |l |m |n |o |p |q |r |s |t |u |v |w |x |y |z |")
print("| Numrat   : |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|")
print("|________________________________________________________________________________|\n")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+ Enkriptimi => Cipher Teksti = Celsi - Plain Teksti  mod(26)                          +")
print("+ Dekriptimi => Plain Teksti  = Celsi - Cipher Teksti mod(26)                          +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("\n---------------------------------")

def beaufortCipher(key,message):
	cipher = ''
	for letter in message:
		if(letter != ' '):
			cipher += Beaufort(key).encipher(letter)		
		else:
			cipher += ' '
	return cipher

def beaufortDecipher(key,message):
	decipher = ''
	for letter in message:
		if(letter != ' '):
			decipher += Beaufort(key).decipher(letter)
		else:
			decipher += ' '
	return decipher
