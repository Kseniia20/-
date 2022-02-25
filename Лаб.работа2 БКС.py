key_ = 'СИСТЕМА' 
step = 14 
key = ''
for w in key_:
    if w not in key:
        key += w 
        
phrases = 'КОМПЬЮТЕРНАЯ СЕТЬ' 
alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
 
tmp = ''
for w in alpha:
    if w not in key:
        tmp += w 
 
alpha_new = tmp[-step:] + key + tmp[:-step]
 
print(phrases.translate(str.maketrans(alpha, alpha_new)))

step = 14
phrases = ("КОМПЬЮТЕРНАЯ СЕТЬ")
alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '

result = []
len_alpha = len(alpha)
symb = ' .,:?!'

for i in phrases:
if not i in symb:
result.append ( alpha [( alpha.find(i) + step ) % len_alpha ]) #
else:
result.append(i)
print('Result: ', '"', ''.join(result) , '"', sep='')
