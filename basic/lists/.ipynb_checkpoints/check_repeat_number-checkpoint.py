mynumblist =[]
mynumber = input("Enter your number:")
mynumber_length = len(str(mynumber))
mynumblist[:mynumber_length]=mynumber
newlist = mynumblist.copy()
newlist.sort()

def removeDupllicateItem(data):
    for n in data:
        if data.count(n)>1:
            data.remove(n)          
    return data

#Check,How many time repeat every item
def repeatCount(data):
    print(f"Your list is: {mynumblist} \n")
    for n in data:
        print(f"{mynumblist.count(n)} time is repeating of {n}")


newlist = removeDupllicateItem(newlist)

repeatCount(newlist)
