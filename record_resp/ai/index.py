import tkinter as tk
from tkinter import ttk
from record import action
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x50")
        self.title("record")
        self.resizable(False, False)
        self.s = ttk.Style()
        self.s.theme_use('alt')
        self.s.configure('TButton',background="#DC3545", foreground="#fff", borderwidth=2, focusthickness=0)
        self.s.map('TButton', background=[('active','#DC3545')])

        self.startBtn = tk.Button(self,text="Start",background="#DC3545", foreground="#fff",
                             padx=30,command=self.startBtnClick)
        self.startBtn.place(x=50,y=8)

        # self.stopBtn = tk.Button(self,text="Stop",background="#DC3545", foreground="#fff",
        #                      padx=15,state="disabled",command=self.stopBtnClick)
        # self.stopBtn.place(x=100,y=8)

    
    def startBtnClick(self):
        action.start(self)
    
    # def stopBtnClick(self):
    #     action.stop(self)
        

          
        
if __name__=="__main__":
    app =App()
    app.mainloop()