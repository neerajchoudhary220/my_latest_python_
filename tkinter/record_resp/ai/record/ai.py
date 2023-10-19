import joblib
model = joblib.load('../models/select_web_lang_model')
html_model = joblib.load('../models/html_model')
html_vocab = joblib.load('../models/html_vocab')

v = joblib.load('../models/select_web_lang_vocab')
question =["write script tag"]

def get_web_lang(lang):
    if lang ==1:
        html = html_model.predict(html_vocab.transform(question))[0]
        return get_html(html)
    elif lang==2:
        return 'Bootstrap'
    elif lang==3:
        return 'Js'
    else:
        return 'CSS'

def get_html(html):
    if html==1:
        return 'all_input'
    elif html==2:
        return 'check_input'
    elif html==3:
        return 'script_tag'
    else:
        return 'button'

choose_web_lang= model.predict(v.transform(question))[0]
result = get_web_lang(choose_web_lang)
print(result)