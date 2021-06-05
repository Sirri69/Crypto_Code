inp = input('Enter plaintext >>> ')
KEY = int(input('Enter the key >>> '))

def shift_encrypt(plain_text: str, key: int):
	cipher_text = []
	plain_text = plain_text.lower().replace(' ','')
	for i in list(plain_text):
		cipher_text.append(chr((ord(i)-97 + key)%26 + 97))

	return "".join(cipher_text)

def shift_decrypt(cipher_text: str, key: int):
	plain_text = []
	cipher_text = cipher_text.lower().replace(' ','')
	for i in cipher_text:
		plain_text.append(chr((ord(i)-97 - key)%26 + 97))

	return "".join(plain_text)



print()

opt = int(input("Press 1 to encrypt your text, 2 to decrypt:> "))

if opt == 1:
	print(shift_encrypt(inp, KEY))

elif opt == 2:
	print(shift_decrypt(inp,KEY))

else:
	print("Dude, your only options are 1 and 2 !")