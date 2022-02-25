A = 165
B = 5
M = 4096*4
Y0 = 3887
 
 
def Gamma(y):
    gamma_list = []
    for _ in range(8):
        y = (A * y + B) % M
        gamma_list.append(y)
    return gamma_list
 
 
def Crypt():
    gamma = Gamma(Y0)
    res = open("Result.txt", "w",encoding="utf-8")
    with open('Sourse.txt', 'r',encoding="utf-8") as f:
        r_int = ""
        r=""
        while True:
            temp = f.read(8)
            if temp:
                for i, item in enumerate(temp):
                    r_int = r_int + " "+str(ord(item) ^ gamma[i])
                    r = r +" "+chr(ord(item) ^ gamma[i])
                    res.write(chr(ord(item) ^ gamma[i]))
 
            else:
                break
    print(r_int)
    res.close()
 
Crypt()



from math import ceil
from random import shuffle
s = list('cистема безопастности')
s1 = round(len(s)**0.5)
s2 = ceil(len(s)**0.5)
a = [[s.pop(0) if s else ' ' for _ in range(s1)] for _ in range(s2)]
shuffle(a)
a = list(map(list,zip(*a)))
shuffle(a)
print(''.join([i for j in a for i in j]))


