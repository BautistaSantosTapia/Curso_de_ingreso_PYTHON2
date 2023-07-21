import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = prompt("TP 5", "Ingrese su apellido:")
        while apellido.isdigit() or apellido == None or len(apellido) < 2:
            apellido = prompt("TP 5", "Ingrese su apellido correctamente:")


        edad = prompt("TP 5", "Ingrese su edad:")
        edad = int(edad)
        while edad == None or (edad < 18 or edad > 90):
            edad = prompt("TP 5","Ingrese su edad correctamente")
            edad = int(edad)
        #edad

        estado_civil = prompt("TP 5", "Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a):")
        estado_civil = estado_civil.lower()
        estado_civil = estado_civil.capitalize()
        while (estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a") or estado_civil == None:
            estado_civil = prompt("TP 5", "Ingrese su estado civil correctamenta (Soltero/a, Casado/a, Divorciado/a, Viudo/a):")
            estado_civil = estado_civil.lower()
            estado_civil = estado_civil.capitalize()
        #tipo

        numero_de_legajo = prompt("TP 5", "Ingrese su numero de legajo (4 digitos):")
        numero_de_legajo = numero_de_legajo.lstrip ("0")
        while not numero_de_legajo.isdigit() or numero_de_legajo == None or len(numero_de_legajo) > 4 or len(numero_de_legajo) < 4:
            numero_de_legajo = prompt("TP 5", "Ingrese su numero de legajo correctamente (4 digitos):") 
            numero_de_legajo = numero_de_legajo.lstrip ("0")
            


        self.txt_apellido.delete(0,tkinter.END)
        self.txt_apellido.insert(0,apellido)

        self.txt_edad.delete(0,tkinter.END)
        self.txt_edad.insert(0,edad)

        #self.combobox_tipo.delete(0,tkinter.END)
        self.combobox_tipo.set(estado_civil)

        self.txt_legajo.delete(0,tkinter.END)
        self.txt_legajo.insert(0,numero_de_legajo)
        
        alert("Ejercicio 7", f"Tu apelido es {apellido}, tu edad es {edad} anos, tu estado es {estado_civil} y su numero de legajo es {numero_de_legajo}.")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
