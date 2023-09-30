mylist = ["Ram","Amit",'Mohan',"Vikash","Suman","Radha","Krishan","Ram","Rohan","Mukesh","Prem","varsha",
          "Vilash","Kumar","suresh"]
# repl = [item.replace("Amit","Neeraj") for item in mylist]
# repl = lambda elm:str.replace(elm,"Ram","Verma")

mystr="Google"

try:
    print(f'First position of {mystr} is',mylist.index(mystr))

except ValueError as e:
    print(e)

    
# myFun = lambda x:str.replace(x,"20","200")

# mystr ="20"
# print(myFun(mystr))

# print(list(map(repl,mylist)))
# print(mylist)


def myfun(elm):
    return str.replace(elm,"Ram","Neeraj")





