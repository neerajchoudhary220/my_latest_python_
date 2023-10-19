from webcategory import tags
class htmlTag():
    def __init__(self,htmlmodel,htmlvocab,question):
        self.htmlmodel = htmlmodel
        self.htmlvocab = htmlvocab
        self.question = question
    
    def getTag(self):
        """
        1==>all_input
        2==>check_input
        3==>script_tag
        4==>button
        """
        tag_id = self.htmlmodel.predict(self.htmlvocab.transform([self.question]))[0]
        if tag_id==1:
            return tags.AllTag().AllInputList()
        elif tag_id==2:
            return tags.AllTag().InputTypeCheckbox()
        elif tag_id==3:
            return tags.AllTag().ScriptTag()
        else:
            return tags.AllTag().Button()
    

    



