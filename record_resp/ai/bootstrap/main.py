import joblib
from bootstrap import buttons
class btsp():
    def __init__(self,question):
        self.bootmodel = joblib.load('./models/bootstrap/main/boot_main_model')
        self.bootvocab = joblib.load('./models/bootstrap/main/boot_main_vocab')
        self.question = question
    
    def prediction(self):
        result =self.bootmodel.predict(self.bootvocab.transform([self.question]))[0]
        if result==1:
            return self.button()
        elif result==2:
            return self.modal()
        elif result==3:
            return self.card()
        elif result==4:
            return print('color')
        elif result==5:
            return print('badge')
        elif result==6:
            return self.buttonlist()
    def modal(self):
        return '''<div class="modal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary">Save changes</button>
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>'''
    
    def card(self):
        return '''<div class="card" style="width: 18rem;">
<img class="card-img-top" src="..." alt="Card image cap">
    <h5 class="card-title">Card title</h5>
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>'''

    def buttonlist(self):
        return '''
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>
<button type="button" class="btn btn-link">Link</button>'''

    def button(self):
        return buttons.primary(self.question).prediction()
        
        

