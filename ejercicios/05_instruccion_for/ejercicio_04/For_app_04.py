import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        """cantidad = prompt("Ejercicio 4", "Ingrese un valor:")
        cantidad = int(cantidad)
        print(cantidad)
        cantidad = cantidad + 1
        print(cantidad)
        print(range(cantidad))
        #el enunciado esta mal por lo tanto el ejercicio esta bien
        mensaje = "Hola UTN FRA"
        for repeticion in range(cantidad):
            if repeticion == 9:
                alert("Ejercicio 4", "Se ingreso el valor '9'")
                break
            elif repeticion == cantidad - 1:
                alert("Ejercicio 4", "No se ingreso el valor '9'")
                break
            else:
                continue"""
        
        for _ in iter(int, 1): #range(99)
            cantidad = prompt("Ejercicio 4", "Ingrese un valor:")
            if cantidad == "9":
                break

        """if (4 in test_list):
            print("Element Exists")"""
        
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()