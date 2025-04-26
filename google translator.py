from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = com_sor.get()
    d = com_dest.get()
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)  # Missing line to insert the translated text

root = Tk()
root.title("TRANSLATOR")
root.geometry("500x600")
root.config(bg='pink')

lab_txt = Label(root, text='TRANSLATOR', font=("Times New Roman", 20, "bold"), bg="Pink")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt1 = Label(root, text='SOURCE TEXT', font=("Times New Roman", 20, "bold"), fg="Black", bg="red")
lab_txt1.place(x=100, y=100, height=20, width=300)

sor_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)

list_text = list(LANGUAGES.values())

com_sor = ttk.Combobox(frame, values=list_text)
com_sor.place(x=10, y=300, height=40, width=150)
com_sor.set("english")

button_change = Button(frame, text="TRANSLATE", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

com_dest = ttk.Combobox(frame, values=list_text)
com_dest.place(x=330, y=300, height=40, width=150)
com_dest.set("english")

lab_txt1 = Label(root, text='DESTINATION TEXT', font=("Times New Roman", 20, "bold"), fg="Black", bg="red")
lab_txt1.place(x=100, y=360, height=20, width=300)

dest_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
