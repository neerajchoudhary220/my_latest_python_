filename = input("Enter you file name:")
f = open(f"./files/{filename}.txt")
mylist = f.readlines()
length_ = len(mylist)

def AddStartString(txt,char):
        return char+txt

#Add number
def addNumber(list,total_lines):
    j=1
    for x in range(0,total_lines,2):
            add_txt = str(j)+'.'
            list[x]=AddStartString(list[x],add_txt)
            j+=1
    return list


def addNewLine(list,total_lines):
    for x in range(1,total_lines,2):
            list[x]=list[x]+'\n'
    return list

f.close()


mylist=addNumber(mylist,length_)
mylist = addNewLine(mylist,length_)
txt= ''.join(mylist)

new_file = open(f"./files/{filename}_updated.txt",'w')
new_file.write(txt)
print("done")
