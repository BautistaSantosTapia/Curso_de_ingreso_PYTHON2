import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en ese lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts -4
    (F)Poste Quebracho Fino de 2.2 mts -6
    (V)Varillas -50

    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        largo = self.txt_largo.get()
        ancho = self.txt_ancho.get()

        largo = int(largo)
        ancho = int(ancho)

        metros_cuadrados = largo * ancho
        metros_lineales = largo * 2 + ancho * 2

        cantidad_de_G = metros_lineales / 250 + 4
        cantidad_de_G = round(cantidad_de_G,0)
        cantidad_de_F = metros_lineales / 12 - cantidad_de_G
        cantidad_de_F = round(cantidad_de_F,0)
        cantidad_de_V = metros_lineales / 2 - cantidad_de_G - cantidad_de_F
        cantidad_de_V = round(cantidad_de_V,0)

        alambre = metros_lineales * 7 
        alambre = int(alambre)

        texto = f"Los metros cuadrados del terreno son: {metros_cuadrados}, Los metros lineales del perimetro son: {metros_lineales}, La cantidad de postes de quebracho Grueso son: {cantidad_de_G}, La cantidad de postes de quebracho Fino son: {cantidad_de_F}, La cantidad de varillas son: {cantidad_de_V} y la cantidad de alambre necesario es de: {alambre} metros."
        alert("TP 3", texto)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
