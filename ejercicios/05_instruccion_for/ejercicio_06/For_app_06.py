import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Ejercicio 6", "Ingresa un numero:")
        numero = int(numero)
        print(numero)
        numero = range(1,numero + 1)
        print(numero)

        numeros_pares = []
        numeros_impares = []
        cantidad_pares = 0
        cantidad_impares = 0
        
        for valor in numero:
            if valor % 2 == 0:
                print(f"es par {valor}")
                cantidad_pares = cantidad_pares + 1
                numeros_pares.append(valor)
            else:
                print(f"es inpar {valor}")
                cantidad_impares = cantidad_impares + 1
                numeros_impares.append(valor)

    
        print(f"La cantidad de pares son {cantidad_pares}")
        print(f"La cantidad de impares son {cantidad_impares}")
        print(f"Los numeros pares son {numeros_pares}")
        print(f"Los numeros impares son {numeros_impares}")


        alert("Ejercicio 6", f"La cantidad de pares son {cantidad_pares} y los numeros pares son {numeros_pares}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()