def removeRepeatWord(txt):
    mylist = txt.split(" ")
    mylist = list(dict.fromkeys(mylist))
    return " ".join(mylist)


mywords="Apple is my fav fruit. Apple is very good for health. Our health should be good"
print(removeRepeatWord(mywords))