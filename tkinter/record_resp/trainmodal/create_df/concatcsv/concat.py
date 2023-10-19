import pandas as pd
import os,pathlib

class Files ():
    def __init__(self,path,newfilename):
        self.path = path
        self.newfilename = newfilename
    
    def createcsv(self):
        files = os.listdir(self.path)
        self.dfs=[]
        
        for file in files:
            f= pathlib.Path(file).suffix
            if f ==".csv":
                self.dfs.append(pd.read_csv(self.path+"/"+file))
                
            
        

        return self.concat(self.dfs)
        
    def concat(self,dfs):
        df = pd.concat(dfs,ignore_index=True)
        df.reset_index()
        df = df.sort_values(by=['label_id'])
        df.to_csv(self.path+"/"+self.newfilename,index=False)
        return print(f"{self.newfilename} file has been created")
