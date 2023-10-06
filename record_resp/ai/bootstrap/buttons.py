import joblib


class primary():
    def __init__(self, question):
        self.question = question
        self.model = joblib.load(
            './models/bootstrap/buttons/primary_button_model')
        self.vocab = joblib.load(
            './models/bootstrap/buttons/primary_button_vocab')

    def prediction(self):
        result = self.model.predict(self.vocab.transform([self.question]))[0]
        if result == 1:
            return self.simple()

        elif result == 2:
            return self.sm()
        elif result == 3:
            return self.smoutline()
        elif result == 4:
            return self.lg()
        elif result == 5:
            return self.outlinelg()
        else:
            return self.button()

    def simple(self):
        return '''<button type="button" class="btn btn-primary">Button</button>'''

    def sm(self):
        return '''<button type="button" class="btn btn-primary btn-sm">Small button</button>'''

    def smoutline(self):
        return '''<button type="button" class="btn btn-outline-primary btn-sm">Small Outline button</button>'''

    def lg(self):
        return '''<button type="button" class="btn btn-primary btn-lg">Large button</button>'''

    def outlinelg(self):
        return '''<button type="button" class="btn btn-outline-primary btn-lg">Large Outline button</button>'''

    
      
