def test():
    print("YES >> clicked....'")

import tkinter
from tkinter import ttk

form =tkinter.Tk()

form.geometry("700x500")
form.config(background ="#ffffff")

fnt=("tahoma",20)

lbls=ttk.Style()
lbls.configure("TLabel",font =fnt ,background ="#00ff00")
tbns =ttk.Style()
tbns.configure("TButton",font =fnt)

lblname = ttk.Label(form , text="Enter you name" ,style = "TLabel")
txtname = ttk.Entry(form , font = fnt)
lbladdress = ttk.Label(form, text ="Enter your address:",style = "TLabel")
txtaddress = ttk.Entry(form,font =fnt )
btn =ttk.Button(form , text ="click here",style ="TButton" ,command =test)
 

lblname.pack()
txtname.pack()
lbladdress.pack()
txtaddress.pack()
btn.pack()

form.mainloop()
