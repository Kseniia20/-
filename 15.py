m = "LIFE"
k = "WORD"
k*= len(m)//len(k)+1
c = ""
for i, j in enumerate(m):
	gg =(ord(j)+ord(k[i]))
	c+=chr(gg%26+65)
	print("Encrypted message: "+str(c))
c = "HWWH"
k = "WORD"
d = ""
for i, j in enumerate(c):
	gg =(ord(j)-ord(k[i]))
	print(chr(gg%26+65))
	d+=chr(gg%26+65)
	print("Decrypted message: "+str(d))	
	

