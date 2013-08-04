alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 
'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 
'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 
'X', 'x', 'Y', 'y', 'Z', 'z', ' ', '.', ',']
lenghtAlph = len(alphabet)
key = input("Input key: ")
text = raw_input("Input text: ")
lenghtText = len(text)

#cipher - array with encrypted text
cipher = []
i = 0
while i < lenghtText:
	cipher += alphabet[ (alphabet.index( text[i] ) + key) % lenghtAlph ]
	i = i + 1

print cipher