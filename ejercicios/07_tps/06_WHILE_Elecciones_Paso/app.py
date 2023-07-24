'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidatos = []
        for candidatos in range(100):

            nombre = prompt("TP 6", "Ingrese su nombre")
            while (nombre == None or nombre == "") or not nombre.isalpha() or len(nombre) < 2:
                nombre = prompt("TP 6", "Ingrese su nombre correctamente:")


            edad = prompt("TP 6", "Ingrese su edad")
            while edad == None or not edad.isdigit() or int(edad) < 25 or int(edad) > 100:
                edad = prompt("TP 6","Ingrese su edad correctamente")
            edad = int(edad)


            votos = prompt("TP 6", "Ingrese la cantidad de votos")
            while votos == None or not votos.isdigit() or int(votos) < 1:
                votos = prompt("TP 6", "Ingrese la cantidad de votos correctamente")
            votos = int(votos)


            candidatos.append()

            respuesta = question("TP 6", "Desea continuar?")
            if respuesta == False:
                break

        
"""
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)
"""

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
