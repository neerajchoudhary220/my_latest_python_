import random
class RandomText():
    def __init__(self, name=[], verbs=[], nouns=[]):
        self.name = name
        self.verbs = verbs
        self.nouns = nouns
        self.data =[]
        self.range_=len(self.name)+len(self.verbs)+len(self.nouns)

    def generate_randome_sentence(self):
        names = self.name
        verbs = self.verbs
        nouns = self.nouns
        return random.choice(names)+" "+random.choice(verbs)+" "+random.choice(nouns)
    
    def CreateList(self):
        for gen in range(self.range_):
            output = self.generate_randome_sentence()
            self.data.append(output)
            
        return self.uniqueList(self.data)
    
    def uniqueList(self, list):
        newlist=[]
        for n in list:
            if n not in newlist:
                newlist.append(n)
           
        return newlist
