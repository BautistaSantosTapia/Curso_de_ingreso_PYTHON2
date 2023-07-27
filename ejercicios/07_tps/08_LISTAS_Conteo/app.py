import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        lista_positivos = []
        lista_negativos = []
        lista_ceros = []
        suma_negativos = 0
        suma_positivos = 0
        minimo_negativo = None
        maximo_positivo = None
        bandera = True
        numero_valido = False

        while True:
                
            numero = prompt("TP 8", "Ingrese un numero")
            if numero:
                contador_menos = 0
                for letra in numero:
                    if not letra.isdecimal() and letra != "-":
                        numero_valido = False
                        break
                    elif letra == "-":
                        contador_menos = contador_menos + 1
                        if contador_menos > 1:
                            numero_valido = False
                            break
                    else:
                        numero_valido = True

                if numero_valido == True:

                    numero = int(numero)

                    if bandera == True:
                        minimo_negativo = numero
                        maximo_positivo = numero
                        bandera = False
                    elif numero > maximo_positivo:
                        maximo_positivo = numero
                    elif numero < minimo_negativo:
                        minimo_negativo = numero
                    
                    
                    if numero > 0:
                        lista_positivos.append(numero)
                    elif numero < 0:
                        lista_negativos.append(numero)
                    else:
                        lista_ceros.append(numero)

            if numero_valido == True:
                texto = "El numero es valido"
            else:
                texto = "El numero no es valido"

            alert("TP 8", texto)
            print(lista_positivos)
            print(lista_negativos)
            print(lista_ceros)

            respuesta = question("TP 8", "Desea continuar?")
            if respuesta == False:
                break

        for numero in lista_negativos:
            suma_negativos = suma_negativos + numero


        for numero in lista_positivos:
            suma_positivos = suma_positivos + numero

        #a
        print(suma_negativos)
        #b
        print(suma_positivos)
        #c
        cantidad_positivos = len(lista_positivos)
        print(cantidad_positivos)
        #d
        cantidad_negativos = len(lista_negativos)
        print(cantidad_negativos)
        #e
        cantidad_ceros = len(lista_ceros)
        print(cantidad_ceros)
        #f
        print(minimo_negativo)
        #g
        print(maximo_positivo)
        #h
        if cantidad_negativos > 0:
            promedio_negativos = suma_negativos / cantidad_negativos
            print(promedio_negativos)
        else:
            print("No hay negativos")



    def btn_mostrar_estadisticas_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
