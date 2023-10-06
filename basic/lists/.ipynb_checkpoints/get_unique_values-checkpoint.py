mylist = ["Mango","Apple","Grapes","Kiwi","Cherry","Orange","Mango","Cherry","Apple"]
mylist.sort()

def uniquelist(list):
    newlist=[]
    for n in list:
       if n not in newlist:
           newlist.append(n)
           
    return newlist

print(uniquelist(mylist))