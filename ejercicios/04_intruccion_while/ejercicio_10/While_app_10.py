import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero = 0
        suma_negativos = 0
        cantidad_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_ceros = 0
        diferencia = 0

        while numero != None:
            numero = prompt("Ejercicio 10", "Ingrese un numero:")
            if numero == None:
                break
            numero = int(numero)
            if numero < 0:
                suma_negativos = suma_negativos + numero
                cantidad_negativos = cantidad_negativos + 1
            elif numero > 0:
                suma_positivos = suma_positivos + numero
                cantidad_positivos = cantidad_positivos + 1
            else:
                cantidad_ceros = cantidad_ceros + 1

        if cantidad_positivos > cantidad_negativos:
            diferencia = cantidad_positivos - cantidad_negativos
            texto_diff = f"La diferencia es de +{diferencia} para los positivos"
        elif cantidad_positivos < cantidad_negativos:
            diferencia = cantidad_negativos - cantidad_positivos
            texto_diff = f"La diferencia es de +{diferencia} para los negativos"
        else:
            diferencia = 0
            texto_diff = f"Hay la misma cantidad de positivos que de negativos"


            
        texto = f"La suma de los negativos da {suma_negativos}.\n"
        texto = texto +  f"La suma de los positivos da {suma_positivos}.\n"
        texto = texto +  f"La cantidad de numeros negativos son {cantidad_negativos}.\n"
        texto = texto +  f"La cantidad de numeros positivos son {cantidad_positivos}.\n"
        texto = texto +  f"La cantidad de ceros son {cantidad_ceros}.\n"
        texto = texto + texto_diff

        alert("Ejercicio 10", texto)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
