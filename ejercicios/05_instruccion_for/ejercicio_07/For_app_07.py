import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("Ejercicio 7", "Ingresa un numero:")
        numero = int(numero)
        print(numero)

        numeros_divisores = []
        numeros_no_divisores = []
        cantidad_divisores = 0
        cantidad_no_divisores = 0
        
        for valor in range(1,numero + 1):
            if numero % valor == 0:
                print(f"es divisor {valor}")
                cantidad_divisores = cantidad_divisores + 1
                numeros_divisores.append(valor)
            else:
                print(f"no es divisor {valor}")
                cantidad_no_divisores = cantidad_no_divisores + 1
                numeros_no_divisores.append(valor)

    
        print(f"La cantidad de divisores son {cantidad_divisores}")
        print(f"La cantidad de no divisores son {cantidad_no_divisores}")
        print(f"Los numeros divisores son {numeros_divisores}")
        print(f"Los numeros no divisores son {numeros_no_divisores}")


        alert("Ejercicio 7", f"La cantidad de divisores son {cantidad_divisores} y los numeros divisores son {numeros_divisores}")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()