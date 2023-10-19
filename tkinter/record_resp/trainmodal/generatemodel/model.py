import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

class Generate():
    def __init__(self,csvfile,randomState,vocabname,modelname):
        self.csvfile = csvfile
        self.randomState =randomState
        self.vocabname =vocabname
        self.modelname=modelname
    
    def ModelCreateProcess(self):
        df = pd.read_csv(self.csvfile)
        x_train,x_test,y_train,y_test = train_test_split(df.question,df.label_id,random_state=self.randomState)
        v = CountVectorizer()
        model = MultinomialNB()
        model.fit(v.fit_transform(x_train), y_train.values)
        model_score= model.score(v.transform(x_test),y_test.values)
        if model_score==1:
            joblib.dump(v,self.vocabname)
            joblib.dump(model,self.modelname)
            return f"Model successfully build with {model_score} score"
        else:
            return model_score
            


