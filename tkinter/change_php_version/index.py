import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("record")
        self.resizable(False, False)
        self.s = ttk.Style()
        self.s.theme_use('alt')
        self.s.configure('TButton',background="#DC3545", foreground="#fff", borderwidth=2, focusthickness=0)
        self.s.map('TButton', background=[('active','#DC3545')])

        self.php_7 = tk.Button(self,text='Php 7.3',padx=20,background="#ff6347",foreground="#fff")
        self.php_7.place(x=30,y=40)

        self.php_8 = tk.Button(self,text='Default Php (8)',padx=20,background='#33b249',foreground='#fff')
        self.php_8.place(x=160,y=40)

        
      


        

          
        
if __name__=="__main__":
    app =App()
    app.mainloop()