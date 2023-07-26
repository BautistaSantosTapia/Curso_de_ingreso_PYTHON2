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

        #a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
        cantidad_postulante_a = 0

        #b. Nombre del postulante Jr con menor edad.
        edad_min_jr = 0
        nombre_min_jr = 0
        bandera = True

        #c. Promedio de edades por género.
        edad_m = 0
        cantidad_m = 0
        edad_f = 0
        cantidad_f = 0
        edad_nb = 0
        cantidad_nb = 0

        #d. Tecnologia con mas postulantes (solo hay una). 
        contador_js = 0
        contador_py = 0
        contador_asp = 0

        #e. Porcentaje de postulantes de cada genero.
        cantidad_postulantes = 0

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
            while (genero == None) or (genero != "M" and genero != "F" and genero != "NB"):
                genero = prompt("TP 7","Ingrese su genero correctamente (Masculino(M) / Femenino(F) / No Binario(NB))")
                genero = genero.upper()

            tecnologia = prompt("TP 7", "Ingrese la tecnologia (JS / PYTHON / ASP.NET)")
            tecnologia = tecnologia.upper()
            while (tecnologia == None) or (tecnologia != "JS" and tecnologia != "PYTHON" and tecnologia != "ASP.NET"):
                tecnologia = prompt("TP 7","Ingrese la tecnologia correctamente (JS / PYTHON / ASP.NET)")
                tecnologia = tecnologia.upper()

            puesto = prompt("TP 7", "Ingrese su puesto (Jr / Ssr / Sr)")
            puesto = puesto.upper()
            while (puesto == None) or (puesto != "JR" and puesto != "SSR" and puesto != "SR"):
                puesto = prompt("TP 7", "Ingrese su puesto correctamente (Jr / Ssr / Sr)")
                puesto = puesto.upper()


            if genero == "NB":
                if tecnologia == "ASP.NET" or tecnologia == "JS":
                    if edad >= 25 and edad <= 40:
                        if puesto == "SSR":
                            cantidad_postulante_a = cantidad_postulante_a + 1

            if puesto == "JR":
                if bandera == True:
                    edad_min_jr = edad
                    nombre_min_jr = nombre
                    bandera == False
                elif edad_min_jr > edad:
                    edad_min_jr = edad
                    nombre_min_jr = nombre

            if genero == "F":
                edad_f = edad_f + edad
                cantidad_f = cantidad_f + 1
            elif genero == "M":
                edad_m = edad_m + edad
                cantidad_m = cantidad_m + 1
            elif genero == "NB":
                edad_nb = edad_nb + edad
                cantidad_nb = cantidad_nb + 1

            if tecnologia == "JS":
                contador_js = contador_js + 1
            elif tecnologia == "PYTHON":
                contador_py = contador_py + 1
            elif tecnologia == "ASP.NET":
                contador_asp = contador_asp + 1



            cantidad_postulantes = cantidad_postulantes + 1


        if cantidad_m > 0:
            promedio_m = edad_m / cantidad_m
            porcentaje_m = cantidad_m / cantidad_postulantes * 100
        else:
            print("No se ingresaron masculinos")

        if cantidad_nb > 0:
            promedio_nb = edad_nb / cantidad_nb
            porcentaje_nb = cantidad_nb / cantidad_postulantes * 100
        else:
            print("No se ingresaron no binarios")

        if cantidad_f > 0:
            promedio_f = edad_f / cantidad_f
            porcentaje_f = cantidad_f / cantidad_postulantes * 100
        else:
            print("No se ingresaron femeninos")


        if contador_asp > contador_js and contador_asp > contador_py:
            mensaje_tecno = f"La tecnologia con mas postulantes es ASP.NET con {contador_asp} postulante/s"
        elif contador_js > contador_py:
            mensaje_tecno = f"La tecnologia con mas postulantes es JS con {contador_js} postulante/s"
        elif contador_py != contador_asp and contador_py != contador_js:
            mensaje_tecno = f"La tecnologia con mas postulantes es PYTHON con {contador_py} postulante/s"
        else:
            mensaje_tecno = f"Hay empate entre las tecnologias con mas postulantes"

        #a
        print(f"La cantidad de postulantes que cumplen las condiciones del punto 'a' son: {cantidad_postulante_a}")

        #b
        print(f"El nombre del postulante mas joven para el puesto Jr es: {nombre_min_jr}")

        #c
        print(f"\n\
              El promedio de edad de los postulantes masculinos es de: {promedio_m}\n\
              El promedio de edad de las postulantes femeninas es de: {promedio_f}\n\
              El promedio de edad de los postulantes no binarios es de: {promedio_nb}")

        #d
        print(mensaje_tecno)

        #e
        print(f"\n\
              El porcentaje de postulaciones masculinas es de: {porcentaje_m}% \n\
              El porcentaje de postulaciones femeninas es de: {porcentaje_f}% \n\
              El porcentaje de postulaciones no binarias es de: {porcentaje_nb}% ")

        #print(cantidad_f)
        #print(cantidad_m)
        #print(cantidad_nb)
       
       

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

# otra forma de hacerlo
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