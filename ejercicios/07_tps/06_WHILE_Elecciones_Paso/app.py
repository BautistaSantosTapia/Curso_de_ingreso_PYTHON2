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
        repeticion = 0
        bandera = True

        #a. nombre del candidato con más votos
        votos_max = 0
        nombre_max = None

        #b. nombre y edad del candidato con menos votos
        votos_min = 0
        nombre_min = None
        edad_min = None

        #c. el promedio de edades de los candidatos
        suma_edades = 0
        cantidad_candidatos = 0

        #d. total de votos emitidos.
        suma_votos = 0

        while repeticion == 0:

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


            if bandera == True:
                votos_max = votos
                votos_min = votos
                nombre_min = nombre
                nombre_max = nombre
                edad_min = edad
                bandera = False
            else:
                if votos < votos_min:
                    votos_min = votos
                    nombre_min = nombre
                    edad_min = edad
                if votos > votos_max:
                    votos_max = votos
                    nombre_max = nombre

            suma_edades = suma_edades + edad
            cantidad_candidatos = cantidad_candidatos + 1
            suma_votos = suma_votos + votos

            respuesta = question("TP 6", "Desea continuar?")
            if respuesta == False:
                break


        if cantidad_candidatos > 0:
            promedio_edades = suma_edades / cantidad_candidatos
        else:
            alert("TP 6", "No se registraron candidatos")

        alert("TP 6", f"\n\
            El candidato con mas votos fue {nombre_max} con {votos_max} votos.\n\
            El candidato con menos votos fue {nombre_min} de {edad_min} anos con {votos_min} votos.\n\
            El promedio de edad de los candidatos fue {promedio_edades} anos.\n\
            El total de votos emitidos fue de {suma_votos} votos.")

        print(votos_max)
        print(nombre_max)

        print(votos_min)
        print(nombre_min)
        print(edad_min)

        print(promedio_edades)

        print(suma_votos)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
