txt = input("Type your word: ")
txtlen = range(len(txt)-1,-1,-1)
newword=''
for n in txtlen:
    newword+=txt[n]
print(newword)