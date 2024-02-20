import tkinter as tk
from tkinter.filedialog import askopenfiles,ask
#In order to initialize the class, we use the __init__ function.
#This creates a method that runs itself when we form an object from the class.
#we are initializing the class through the tk.Tk __init__ as well.it allow us to work in it 
class Notepad(tk.Tk):
    def __init__(self,*args, **kwargs):
      #we will pass “tk. Tk” which will create the root object for our GUI application. 
      #Under this, we will define a “__init__” constructor with self,*args,**kwargs as parameters.
      tk.Tk.__init__(self, *args, **kwargs)
        
      self.text=tk.Text(self,font="lucida 20",undo=True)
      self.text.pack(side="top", fill="both", expand=True)
      self.wm_iconbitmap()
      self.menu = tk.Menu(self)
      self.config(menu=self.menu)
      self.title("Notepad")
    
      filemenu=tk.Menu(self.menu,tearoff=0)
      self.menu.add_cascade(label='File',menu=filemenu)
      filemenu.add_command(label='New',command=self.new_file,accelerator="Ctrl+N")
      filemenu.add_command(label='New Window',command=self.new_window,accelerator="Ctrl+Shift+N")
      filemenu.add_command(label='Open file',command=self.open_file,accelerator="Ctrl+O")
      filemenu.add_command(label='Save file',command=self.save_file,accelerator="Ctrl+S")
      filemenu.add_command(label='Save as',command=self.save_as,accelerator="Ctrl+Shift+S")
      filemenu.add_separator()
      filemenu.add_command(label='Page Setup',command=self.Page_setup)
      filemenu.add_command(label='Print',command=self.print,accelerator="Ctrl+P")
      filemenu.add_separator()
      filemenu.add_command(label='Exit',command=self.Exit)
 
      editmenu=tk.Menu(self.menu,tearoff=0)
      self.menu.add_cascade(label="Edit",menu=editmenu)

      editmenu.add_command(label='Undo',command=self.Undo,accelerator="Ctrl+Z")
      editmenu.add_separator()
      editmenu.add_command(label='Cut',command=self.cut,accelerator="Ctrl+X")
      editmenu.add_command(label='Copy',command=self.copy,accelerator="Ctrl+C")
      editmenu.add_command(label='Paste',command=self.paste,accelerator="Ctrl+V")
      editmenu.add_command(label='Delet',command=self.Delet,accelerator="Ctrl+D")
      editmenu.add_separator()
      editmenu.add_command(label='Replace',command=self.Replace,accelerator="Ctrl+H")
      editmenu.add_command(label='Go To',command=self.go_to,accelerator="Ctrl+G")
      editmenu.add_separator()
      editmenu.add_command(label='Select All',command=self.Select,accelerator="Ctrl+A")
      editmenu.add_command(label='Time/Date',command=self.time_date,accelerator="f5")

      formatmenu=tk.Menu(self.menu,tearoff=0)
      self.menu.add_cascade(label="Format",menu=formatmenu)

      formatmenu.add_command(label='word Wrap',command=self.word)
      formatmenu.add_command(label='Font',command=self.font)

      viewmenu=tk.Menu(self.menu,tearoff=0)
      self.menu.add_cascade(label="View",menu=viewmenu)
   
    def new_window(self):
      
        self.title("Notepad")

    def new_file(self):
        self.text.delete("1.0", "end")
        self.title("Notepad")

    def open_file(self):
        file = filedialog.askopenfile( self,mode="read", title="Open a file")
        if file:
            contents = file.read()
            self.text.delete("0.1", "end")
            self.text.insert("0.1", contents)
            file.close()
            self.title(file.name + "- Notepad")

    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            contents = self.text.get("0.1", "end")
            file.write(contents)
            file.close()
            self.title(file.name + " - Notepad")

    def Page_setup(self):
      pass
        

    def save_as(self):
        pass

    def Delet(self):
        self.text.event_generate("<<Delet>>")


    def print(self):
       self.text.event_generate("<<print>>")

    def Exit(self):
      self.text.event_generate("<<Exit>>")

    def Undo(self):
        self.text.event_generate("<<Undo>>")          

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")
    
    def Replace(self):
        self.text.event_generate("<<Replace>>")

    def go_to(self):
        self.text.event_generate("<<goto>>")

    def Select(self):
        self.text.event_generate("<<Select>>")

    def time_date(self):
        self.text.event_generate("<<time_date>>")
    
    def word(self):
      pass
   
    def font(self):
       pass

notepad= Notepad()
notepad.mainloop()