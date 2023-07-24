'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        """ Nombre
            Edad (mayor de edad)
            Género (F-M-NB)
            Tecnología (PYTHON - JS - ASP.NET)
            Puesto (Jr - Ssr - Sr)"""
        for postulantes in range(10):

            nombre = prompt("TP 7", "Ingrese su nombre")
            while (nombre == None or nombre == "") or not nombre.isalpha() or len(nombre) < 2:
                nombre = prompt("TP 7", "Ingrese su nombre correctamente:")


            edad = prompt("TP 7", "Ingrese su edad")
            while edad == None or not edad.isdigit() or int(edad) < 18 or int(edad) > 120:
                edad = prompt("TP 7","Ingrese su edad correctamente")
            edad = int(edad)


            genero = prompt("TP 7", "Ingrese su genero (M / F / NB)")
            genero = genero.upper()
            while (genero == None or not genero.isalpha()) or (genero != "M" and genero != "F" and genero != "NB"):
                genero = prompt("TP 7","Ingrese su genero correctamente (Masculino(M) / Femenino(F) / No Binario(NB))")
            genero = genero.upper()


            tecnologia = prompt("TP 7", "Ingrese la tecnologia (JS / PYTHON / ASP.NET)")
            tecnologia = tecnologia.upper()
            while (tecnologia == None or not tecnologia.isalpha()) or (tecnologia != "JS" and tecnologia != "PYTHON" and tecnologia != "ASP.NET"):
                tecnologia = prompt("TP 7","Ingrese la tecnologia correctamente (JS / PYTHON / ASP.NET)")
            tecnologia = tecnologia.upper()


            puesto = prompt("TP 7", "Ingrese su puesto (Jr / Ssr / Sr)")
            puesto = puesto.upper()
            while (puesto == None or not puesto.isalpha()) or (puesto != "JR" and puesto != "SSR" and puesto != "SR"):
                puesto = prompt("TP 7", "Ingrese su puesto correctamente (Jr / Ssr / Sr)")
            puesto = puesto.upper()


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


"""
contador = 0
        puntoA = 0
        bandera_del_primero = True
        numero = 0
        numero_menor = 0
        totalf = 0
        totalm = 0
        totalnb = 0
        acumuladorf = 0
        acumuladorm = 0
        acumuladornb = 0
        genteasp = 0
        gentejs = 0
        gentepython = 0
        porcentajef = 0
        porcentajem = 0
        porcentajenb = 0

        for contador in range(0,2):
            nombre = prompt(title="nombre", prompt= "ingrese su nombre")
            while nombre == "" and  nombre.isdigit():
                nombre = prompt(title="Error", prompt= "ingrese su nombre devuelta por favor")
            
            genero = prompt(title="genero",prompt="ingrese su genero = F, M o NB")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt(title= "error", prompt="no introdujo F, M o NB")   
            
            tecnologia=prompt(title= "tecnologia", prompt="introduzca la tecnologia con la que trabaja, PYTHON, JS o ASP.NET")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt(title= "error", prompt="no introdujo PYTHON, JS o ASP.NET")
            
            puesto = prompt(title="puesto",prompt="ingrese el puesto al que se postula = Jr,Ssr o Sr")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt(title= "error", prompt="no introdujo Jr,Ssr o Sr ")
            
            while True:
                edad = prompt(title="edad",prompt="ingrese su edad")
                if (edad !=None and edad.isdigit()):
                    edadinteada = int(edad)
                    if edadinteada < 18:
                        edad = prompt(title="ERROR",prompt="ERROR , Debe ser mayor a 18")
                    else:
                        break
                else:
                    edad = prompt(title="ERROR",prompt="ERROR , ingrese una edad correcta")
            
            if edad >25 and edad < 40 and tecnologia == "ASP.NET" or tecnologia == "JS" and puesto == "Ssr" and genero == "NB":
                puntoA = puntoA + 1     

            if puesto == "Jr":
                if bandera_del_primero == True:
                        numero_menor = edad 
                        nombre_menor = nombre
                        bandera_del_primero = False

            if puesto == "Jr":
                if edad < numero_menor:
                    numero_menor = edad
                    nombre_menor = nombre
                    

            match genero:
                case "F":
                    totalf = totalf + edad
                    acumuladorf = acumuladorf +1
                case "M":
                    totalm = totalm + edad
                    acumuladorm = acumuladorm +1
                case "NB":
                    totalnb = totalnb + edad 
                    acumuladornb = acumuladornb + 1

            match puesto:
                case "JS":
                    gentejs = gentejs + 1
                case "ASP.NET":
                    genteasp = genteasp + 1
                case "PYTHON":
                    gentepython = gentepython + 1
            
            if gentejs > genteasp and gentejs > gentepython:
                mayortecnologia = "JS"
            elif genteasp > gentejs and genteasp > gentepython:
                mayortecnologia = "ASP.NET"
            elif gentepython > gentejs and gentepython > genteasp:
                mayortecnologia = "PYTHON"
        
        promediof = totalf / acumuladorf

        promediom = totalm / acumuladorm

        promedionb = totalnb / acumuladornb

        porcentajem = (10 * acumuladorm) / 100

        porcentajef = (10 * acumuladorf) / 100

        porcentajenb = (10 * acumuladornb) / 100

        alert ("hola", "hay "+ str(puntoA) +" de gente y " + str(nombre_menor) + " es el mas joven y " + str(promediof) + " es el promedio de edad de las mujeres y " + str(promediom) +" es el promedio de edad de los hombres y " + str(promedionb) + " es el promedio de edad no binario, la tecnologia mas usada es " + mayortecnologia +" el porcentaje de mujeres es " + porcentajef +"% , el porcentaje de hombres es " + porcentajem +"% y el porcentaje de no binarios es de " + porcentajenb + "%." )
"""