import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Ejercicio 8", "Ingresa un numero:")
        numero = int(numero)
        print(numero)
    
        cantidad_primos = 0
        cantidad_no_primos = 0
        
        for valor in range(2,numero + 1):
            if numero % valor == 0:
                print(f"no es primo {valor}")
                cantidad_no_primos = cantidad_no_primos + 1
            else:
                print(f"es primo {valor}")
                cantidad_primos = cantidad_primos + 1
                
                
        if cantidad_no_primos >= 2:
            print("respuesta final: no es primo")
            texto = "Respuesta final: No es primo"
        else:
            print("respuesta final: es primo")
            texto = "Respuesta final: Es primo"
        

        alert("Ejercicio 8", texto)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()