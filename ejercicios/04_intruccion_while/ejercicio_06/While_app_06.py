import tkinter 
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        resultado_suma = 0
        cantidad = 0

        while cantidad < 5:
            numero = int(prompt("Ejercicio 6", "Ingresa un numero:"))
            resultado_suma = resultado_suma + numero 
            cantidad = cantidad + 1

        promedio = resultado_suma / cantidad
        
        self.txt_suma_acumulada.delete(0,tkinter.END)
        self.txt_suma_acumulada.insert(0,resultado_suma)
        
        self.txt_promedio.delete(0,tkinter.END)
        self.txt_promedio.insert(0,promedio)

        alert("Ejercicio 6", f"El promedio es de {promedio} y la suma da {resultado_suma}.")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
