import keyboard
from record import category
import joblib
html_model = joblib.load('./models/html_model')
html_vocab = joblib.load('./models/html_vocab')
web_lang_model= joblib.load('./models/select_web_lang_model')
web_lang_vocab= joblib.load('./models/select_web_lang_vocab')
question = "write the script tag"

def start(btn):
        record = keyboard.record(until='enter',)
        record_txt = list(keyboard.get_typed_strings(record))
        while("" in record_txt):
            record_txt.remove("")
            
        question = record_txt[0] 
        answer = category.Embedd(web_lang_model,web_lang_vocab,html_model,html_vocab,question).selectWebLang()
        
        keyboard.write(answer,delay=0.03)

    

