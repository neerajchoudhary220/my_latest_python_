import random
import pandas as pd
import os
class Createcsv():
    def __init__(self, path,label, label_id, name=[], verbs=[], nouns=[]):
        self.path = path
        self.label = label
        self.label_id = label_id
        self.name = name
        self.verbs = verbs
        self.nouns = nouns
        self.data= []
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

    def creatingcsv(self):
        data = self.CreateList()
        df = pd.DataFrame({"question":data})
        df['label_id']=df.question.apply(lambda x:self.label_id)
        df['label'] = df.label_id.apply(lambda x:self.label if x==self.label_id else 0)
        fileNmae = os.path.join(self.path,self.label+".csv")
        df.to_csv(fileNmae, index=False,)
        return print(f"{self.label}.csv file has been created")


   




