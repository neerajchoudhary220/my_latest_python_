from randomsentence import datasheetgen
import ast
class csv():
    def __init__(self,jsonfile,outputpath):
        self.jsonfile = jsonfile
        self.outputpath = outputpath
    
    def create(self):
        with open(self.jsonfile) as f:
            data = f.read()
        data = ast.literal_eval(data)
        labels = data['labels']
        for key in data['labels']:
            label_id = labels[key]['label_id']
            names=labels[key]['names']
            verbs=labels[key]['verbs']
            noun=labels[key]['noun']
            label = key
            datasheetgen.Createcsv(self.outputpath,label,label_id,names,verbs,noun).creatingcsv()