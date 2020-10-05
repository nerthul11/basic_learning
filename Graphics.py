from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

r=Tk()
r.title("Graphics")

f=Frame(r)
f.pack()

usuario = StringVar()
contraseña = StringVar()
pick = IntVar()

def Enviar():
    print(f"Username: {usuario.get()}\nPassword: {contraseña.get()}")
def choose():
    print(pick.get())
def openfile():
    archivo=filedialog.askopenfilename(title="Abrir",initialdir="/Users/Gabriel/Pycharm/Proyectos/venv",filetypes=(("Fichero de texto","*.txt"),("Hoja de cálculo de Excel","*.xlsx")))
def Luther():
    messagebox.showwarning("Luther","WALLOW IN DESPAIR")
def Exit():
    salir=messagebox.askokcancel("Salir","¿Deseas salir?")
    if salir:
        r.destroy()

m=Menu(r)
r.config(menu=m) # Compila Menu a Raiz
archivo=Menu(m,tearoff=0) # Tearoff ayuda a estética
archivo.add_command(label="New File")
archivo.add_command(label="Open File",command=openfile)
archivo.add_command(label="Save File")
archivo.add_separator()
archivo.add_command(label="Luther",command=Luther)
archivo.add_separator()
archivo.add_command(label="Exit",command=Exit)
edicion=Menu(m,tearoff=0)
edicion.add_command(label="TBA")
ayuda=Menu(m,tearoff=0)
ayuda.add_command(label="TBA")
m.add_cascade(label="File",menu=archivo)
m.add_cascade(label="Edit",menu=edicion)
m.add_cascade(label="Help",menu=ayuda)

user=Entry(f,textvariable=usuario).grid(row=0,column=1)
password=Entry(f,textvariable=contraseña)
password.grid(row=1,column=1)
password.config(show="*")
comment=Text(f,width=15,height=5)
comment.grid(row=2,column=1)
scroll=Scrollbar(f,command=comment.yview)
scroll.grid(row=2,column=2,sticky="nesw")
comment.config(yscrollcommand=scroll.set)
Radiobutton(f,text="Male",variable=pick,value=1,command=choose).grid(row=3,column=1,sticky="w")
Radiobutton(f,text="Female",variable=pick,value=2,command=choose).grid(row=4,column=1,sticky="w")
Radiobutton(f,text="Other",variable=pick,value=3,command=choose).grid(row=5,column=1,sticky="w")

u=Label(f,text="User: ").grid(row=0,column=0,sticky="e",pady=10)
pw=Label(f,text="Password: ").grid(row=1,column=0,sticky="e",pady=10)
cm=Label(f,text="Comment: ").grid(row=2,column=0,sticky="e",pady=10)

b=Button(r,text="Enter",command=Enviar)
b.pack()
r.mainloop()