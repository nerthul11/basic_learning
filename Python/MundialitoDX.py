from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random

r = Tk()
r.title("MundialitoDX")
r.config(width=480, height=240)
f = Frame()
f.pack()

archivo = StringVar()
n = IntVar() # Cantidad de equipos
g = IntVar() # Cantidad de grupos
pick = IntVar() # Elección de fase
equipos = [] # Lista de equipos

def abrir():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="*", filetypes=(("Fichero de texto", "*.txt"),("Hoja de cálculo de Excel","*.xlsx")))
    with open(archivo, "r") as listado:
        for lines in listado:
            equipo = lines.strip()
            if equipo not in equipos:
                equipos.append(equipo)
    n.set(len(equipos))
    larchivo.config(text=archivo)
    lequipos.config(text=f"Equipos anotados: {n.get()}")

def exit():
    salir=messagebox.askokcancel("Salir","¿Deseas salir?")
    if salir:
        r.destroy()

def fasedegrupos():
    if g.get() == 0:
        messagebox.showerror("Error","No se pueden formar grupos de 0 equipos")
    else:
        if n.get()%g.get()!= 0:
            messagebox.showwarning("Advertencia",f"{g.get()} no es divisor de {n.get()}. Poné otro número")
        else:
            gt = int(n.get() / g.get())  # GT = Cuántos equipos por grupo hay
            for grupos in range(g.get()):
                print(f"\nGrupo {grupos + 1}:")
                for i in range(gt):
                    print(equipos[i + gt * grupos])

def iniciar():
    if n.get() == 0:
        messagebox.showwarning("Advertencia","No hay ningún equipo anotado")
    elif pick.get() == 1:
        fasedegrupos()
    elif pick.get() == 2:
        playoff()

def playoff():
    if n.get()<=3:
        messagebox.showwarning("Advertencia","Tiene que haber al menos 4 equipos para esta instancia")
    elif n.get()%2==1:
        messagebox.showwarning("Advertencia","Tiene que ser una cantidad par de equipos")
    else:
        random.shuffle(equipos)
        vs=1
        i=0
        while i<n.get():
            print(f"{vs}- {equipos[i]} vs {equipos[i+1]}")
            vs+=1
            i+=2

random.shuffle(equipos)
m = Menu()
r.config(menu=m)
archivo = Menu(m,tearoff=0)
archivo.add_command(label="Abrir", command=abrir)
archivo.add_command(label="Salir", command=exit)
m.add_cascade(label="Archivo", menu=archivo)
larchivo = Label(f,text="No hay ningún archivo abierto.")
larchivo.grid(row=0, column=0, sticky="w")
lequipos = Label(f,text=f"Equipos anotados: {n.get()}")
lequipos.grid(row=1, column=0, sticky="w")
bgrupos = Radiobutton(f,text="Fase de Grupos",variable=pick, value=1).grid(row=2, column=0, sticky="w")
egrupos = Entry(f,textvariable=g,width=3).grid(row=2, column=1, sticky="w")
lgrupos = Label(f,text="grupos").grid(row=2, column=2, sticky="w")
bplayoffs = Radiobutton(f,text="Playoff",variable=pick, value=2).grid(row=3, column=0, sticky="w")
bsend = Button(r, text="Iniciar", command=iniciar)
bsend.pack()

r.mainloop()