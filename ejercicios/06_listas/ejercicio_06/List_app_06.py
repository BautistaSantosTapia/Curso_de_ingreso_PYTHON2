import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'PROMEDIO' se analizará el vector lista_datos a efectos de calcular 
el promedio el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        lista = self.lista_datos
        #lista.append(100)
        suma_numeros = 0
        promedio = 0
        for numero in lista:
            suma_numeros = suma_numeros + numero

        cantidad_elementos = len(lista)
        promedio = suma_numeros / cantidad_elementos

        alert("Ejercicio 6", f"La promedio de los numeros es: {promedio}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()