from tkinter import *
from os import walk
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import ttk
from PIL import Image, ImageTk


files = []
path = r"C:\Users\User\Desktop\ProgramaAutoedit\DataCarros"
for (dirpath, dirnames, filenames) in walk(path):
  files.extend(filenames)
  break
teste = files

TEMPLETE = [
"tjunta",
"tretentor",
"tparafuso"
] #etc

OPTIONS = [
"Junta",
"Retentor",
"parafuso"
] #etc

root = Tk()
root.configure(bg='white')
root.iconbitmap(r"C:\Users\User\Desktop\ProgramaAutoedit\IconesPrograma\icone.ico")
result = tk.StringVar()
# Set Title
root.title('AutoEdit')

# Set Geometry
root.geometry("700x300")

# Update the listbox
def update_listbox(data):
  # Clear the listbox
  list_box.delete(0, END)

  # Add programming_lan to listbox
  for item in data:
    list_box.insert(END, item)

# Update entry box with listbox clicked
def update(e):
  # Delete entry box
  entry.delete(0, END)

  # Add clicked list item to entry box
  entry.insert(0, list_box.get(ANCHOR))

# Check entry box vs listbox
def check(e):
  # get typed text
  typed_text = entry.get()

  if typed_text == '':
    data = teste
  else:
    data = []
    for item in teste:
      if typed_text.lower() in item.lower():
        data.append(item)
  # update our listbox
  update_listbox(data)


####################TEMPLATE##############

template = StringVar(root)
template.set(TEMPLETE[0]) # default value

w = Combobox(root, values=TEMPLETE, textvariable=template)
w.place(x=40, y=80)

#####################Produto##############

produto = StringVar(root)
produto.set(OPTIONS[0]) # default value
w = Combobox(root, values=OPTIONS, textvariable=produto)
w.place(x=40, y=130,)

def save():
    Junta_Comprimento = 600
    Junta_Altura = 300
    global TipoProduto
    TipoProduto = Image.open(r"C:\Users\User\Desktop\ProgramaAutoedit"+ "\\" + template.get() + ".jpg")
    global TipoProduto1copy
    TipoProduto1copy = TipoProduto.copy()
    Produto = Image.open(r"C:\Users\User\Desktop\ProgramaAutoedit" + "\\" + produto.get() + ".jpg")
    Produto = Produto.resize((Junta_Comprimento, Junta_Altura))
    Produto3copy = Produto.copy()
    TipoProduto1copy.paste(Produto3copy, (570, 60))
    return

def getElement(event):
    selection = event.widget.curselection()
    index = selection[0]
    value = event.widget.get(index)
    result.set(value)
    global resultado
    resultado = value
    Carro = Image.open(r"C:\Users\User\Desktop\ProgramaAutoedit\DataCarros" + "\\" + value)
    Tamanho_carro_Comprimento = 1100
    Tamanho_carro_Altura = 850
    Carro = Carro.resize((Tamanho_carro_Comprimento, Tamanho_carro_Altura))
    Carro2copy = Carro.copy()
    TipoProduto1copy.paste(Carro2copy, (50, 470))
    TipoProduto1copy.save(r"C:\Users\User\Desktop\ProgramaAutoedit\Pronto\\" + value)
    label = Label(root,text=value, bg= "white", compound=tk.LEFT)
    label.place(y=100, x=590)
    label.after(2000, label.destroy)

# Create a label
label = Label(root, text="PARANÁ AUTO PEÇAS",font=("Arial", 14), bg='white')
label.pack(pady=20)
# Create an entry box
entry = Entry(root, font=("Helvetica", 20))
entry.pack()

# Create a listbox
list_box = Listbox(root, width=50)
list_box.pack()



img = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\ProgramaAutoedit\IconesPrograma\logo.jpeg"))
panel = Label(root, image = img, bg="white")
panel.place(x=530, y=180)

icon = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\ProgramaAutoedit\IconesPrograma\icone.ico"))
button = ttk.Button(root, text="Aplicar selecionados", command=save, image=icon, compound=tk.LEFT)
button.place(x=40, y=160,)

logosite = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\ProgramaAutoedit\IconesPrograma\logosite.jpg"))
panel = Label(root, image = logosite, bg="white")
panel.place(x=0, y=0)

label = Label(root, text="Ultimo arquivo criado", bg="white")
label.place(y=80, x=550)

SelecioneProduto = Label(root, text="Selecione o Produto", bg="white")
SelecioneProduto.place(x=50, y=105)

SelecioneTemplate = Label(root, text="Selecione o Template", bg="white")
SelecioneTemplate.place(x=50, y=50)

# Add the programming_lan to our list
update_listbox(teste)



# Create a binding on the listbox
list_box.bind("<<ListboxSelect>>", getElement)
# Create a binding on the entry box
entry.bind("<KeyRelease>", check)


# Execute Tkinter
root.mainloop()