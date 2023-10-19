from webcategory import html
from bootstrap import main
class Embedd():
    def __init__(self,langModel,langVocab,htmlModel,htmlVocab,question):
            self.langModel = langModel
            self.langVocab = langVocab
            self.htmlModel = htmlModel
            self.htmlVocab = htmlVocab
            self.question = question
    
    def selectWebLang(self):
          """
          1==>html
          2==>bootstrap
          3==>js
          4==>css
          """
          lang_id = self.langModel.predict(self.langVocab.transform([self.question]))[0]
          if lang_id==1:
                return self.html_()
          elif lang_id==2:
                return self.bootstrap()
          elif lang_id==3:
                return print('js')
          elif lang_id==4:
                return print('css')
        

    def html_(self):
          htmlTags = html.htmlTag(self.htmlModel,self.htmlVocab,self.question)
          return htmlTags.getTag()
    def bootstrap(self):
          return main.btsp(self.question).prediction()

          


