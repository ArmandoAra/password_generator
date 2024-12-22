from tkinter import *
from tkinter import filedialog
import os.path
from logic import pass_gen
from tkinter import messagebox as MessageBox
from datetime import datetime
import pathlib

#Color de campos de texto
color_entry = "#cce2e4"

ventana = Tk()
ventana.title("Pasword Generator")
ventana.geometry("500x800")
ventana.resizable(0, 0)


titulo = Label(ventana, text="Password Generator")
titulo.config(
    fg="white",
    bg="black",
    font=("Arial", 25),
    padx=50,
    pady=20
)
titulo.pack()

num = StringVar() #Stringvar es una funcion para guardar los datos
num_symb = StringVar()  #Stringvar es una funcion para guardar los datos
num_leters = StringVar()  #Stringvar es una funcion para guardar los datos
resultado = StringVar()
service = StringVar()
file_selected = StringVar()

def generate():
    if len(num.get()) == 0 and len(num_symb.get()) == 0 and len(num_leters.get()) == 0:
        MessageBox.showerror("ERROR", "At least one amount must be filled")
        return
    try:
        pass_generated = pass_gen(int(num.get()), int(num_leters.get()), int(num_symb.get()))
        resultado.set(pass_generated) # asignar al la variable el dato recogido
    except:
        MessageBox.showerror("ERROR", "All amounts must be Numbers")
        
#funcion para copiar el texto generado en la memoria
def copy(): 
    if len(resultado.get()) > 0:     
        ventana.clipboard_append(resultado.get())
        MessageBox.showinfo("Copied", "Password Copied to Clipboard")

#funcion para guardar el texto generado en un archivo
    
def save():
    file_name = file_selected.get().split("/")[-1]
    file_path = file_selected.get()
    #Obtener la ruta del archivo .exe
    curent_path = str(pathlib.Path().absolute())
    #reemplazar ls barras por las del sistema operativo
    curent_path = curent_path.replace("\\", "/")
    time = datetime.now(
    ).strftime("%Y-%m-%d-%H-%M-%S")
    if len(resultado.get()) > 0:
        if os.path.isfile(file_path):
            file = open(file_path, "a")
            file.write(f"Servicio: {service.get()} - Pass: {resultado.get()} - Fecha {time[:10]} \n")
            file.close()
            MessageBox.showinfo("Saved", "Password Saved")
        else:
            #Crear carpeta si no existe
            if not os.path.exists(f"{curent_path}/saved"):
                os.makedirs(f"{curent_path}/saved")
            file = open(f"{curent_path}/saved/newPasswods{time}.txt", "w")
            file.write(f"Servicio: {service.get()} - Pass: {resultado.get()} - Fecha {time[:10]} \n")
            file.close()
            MessageBox.showinfo("Saved", f"Password Saved in new file {curent_path}/saved/newPasswods{time}.txt")
    

def select_route():
    file= filedialog.askopenfilename(
        initialdir = "/",
        title = "Select file",
        filetypes = (("text files", "*.txt"),("csv files", "*.csv")))
    
    file_selected.set(file)
    
    
    


#Labels de cantidad de numeros, simbolos y letras
entrys_style = {"side":"top", "fill":"both","padx":5, "pady":5}
Label(ventana, text="Amount of Numbers ").pack(entrys_style)
Entry(ventana, textvariable=num, justify="center", bg=color_entry, font=("Arial", 15) ).pack(entrys_style, ipady=12)

Label(ventana, text="Amount of Leters ").pack(entrys_style)
Entry(ventana, textvariable=num_leters, justify="center", bg=color_entry, font=("Arial", 15)).pack(entrys_style, ipady=12)

Label(ventana, text="Amount of Symbols ").pack(entrys_style)
Entry(ventana, textvariable=num_symb, justify="center", bg=color_entry, font=("Arial", 15)).pack(entrys_style, ipady=12)

Label(ventana, text="Service(Optional) ").pack(entrys_style)
Entry(ventana, textvariable=service, justify="center", bg=color_entry, font=("Arial", 15)).pack(entrys_style, ipady=12)

texto_recogido = Label(ventana, text="Password Genetated: ")
texto_recogido.pack(entrys_style)
texto_recogido = Label(ventana, textvariable=resultado, bg="black", fg="white", font=("Arial", 20))
texto_recogido.pack(fill=X,anchor = NW, pady=2)

def on_enter_generate(e):
    generate_button.config(bg='#82d682')

def on_enter_copy(e):
    copy_button.config(bg='#82d682')

def on_enter_save(e):
    save_button.config(bg='#82d682')

def on_enter_select(e):
    select_route_button.config(bg='#82d682')

# Función para restaurar el color de fondo del botón cuando el cursor se mueve fuera del botón
def on_leave_generate(e):
    generate_button.config(bg='SystemButtonFace')

def on_leave_copy(e):
    copy_button.config(bg='SystemButtonFace')

def on_leave_save(e):
    save_button.config(bg='SystemButtonFace')

def on_leave_select(e):
    select_route_button.config(bg='SystemButtonFace')


generate_button = Button(ventana, text="Generate ", command=generate)
generate_button.pack(entrys_style, ipady=12)

copy_button = Button(ventana, text="Copy ", command=copy)
copy_button.pack(entrys_style)

save_button = Button(ventana, text="Save ", command=save)
save_button.pack(entrys_style)

select_route_button = Button(ventana, text="File", command=select_route)
select_route_button.pack(entrys_style)

Label(ventana, text="File selected to save your passwords: ").pack(entrys_style)

# Asociar los eventos con el botón
generate_button.bind("<Enter>", on_enter_generate)
generate_button.bind("<Leave>", on_leave_generate)
generate_button.config(cursor="hand2")

copy_button.bind("<Enter>", on_enter_copy)
copy_button.bind("<Leave>", on_leave_copy)
copy_button.config(cursor="hand2")

save_button.bind("<Enter>", on_enter_save)
save_button.bind("<Leave>", on_leave_save)
save_button.config(cursor="hand2")

select_route_button.bind("<Enter>", on_enter_select)
select_route_button.bind("<Leave>", on_leave_select)
select_route_button.config(cursor="hand2")

file = Label(ventana, textvariable=file_selected, bg="#82d682")
file.pack(entrys_style)

Label(ventana, text="Create by ArmandoArano", justify="right").pack(anchor=S)


ventana.mainloop()