alpha = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
word = input()
for i in range(len(alpha)):
    word = word.replace(alpha[i], chr(ord("A")+i))
print(len(word))