import re
def removejsComment(txt):
    result = re.sub('[//]','',txt)
    print(result)
    

def onlystring(txt):
    result = re.sub('[^a-zA-Z ]','',txt)
    print(result)

def onlydigit(txt):
    result = re.sub('[^0-9]','',txt)
    print(result)
def onlyspecialcharacter(txt):
    result = re.sub("[^$&+,:;=?@#|'<>.^*()%!-]",'',txt)
    print(result)

def removejsconsolelog():
    txt = re.sub('console\.log\((.|\n)*?\);?','',txt)
    print(txt)