import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        primer_importe = self.txt_importe_1.get()
        segundo_importe = self.txt_importe_2.get()
        tercer_importe = self.txt_importe_3.get()

        primer_importe = int(primer_importe)
        segundo_importe = int(segundo_importe)
        tercer_importe = int(tercer_importe)

        resultado_suma = primer_importe + segundo_importe + tercer_importe

        texto = f"El resultado de la suma es {resultado_suma}"

        alert("TP 1", texto)

    def btn_promedio_on_click(self):
        primer_importe = self.txt_importe_1.get()
        segundo_importe = self.txt_importe_2.get()
        tercer_importe = self.txt_importe_3.get()

        primer_importe = int(primer_importe)
        segundo_importe = int(segundo_importe)
        tercer_importe = int(tercer_importe)

        resultado_promedio = (primer_importe + segundo_importe + tercer_importe) / 3
        
        texto = f"El resultado del promedio es {resultado_promedio}"

        alert("TP 1", texto)


    def btn_total_iva_on_click(self):
        primer_importe3 = self.txt_importe_1.get()
        segundo_importe3 = self.txt_importe_2.get()
        tercer_importe3 = self.txt_importe_3.get()

        primer_importe3 = int(primer_importe3)
        segundo_importe3 = int(segundo_importe3)
        tercer_importe3 = int(tercer_importe3)

        resultado_suma = primer_importe3 + segundo_importe3 + tercer_importe3

        precio_iva = resultado_suma * 21 / 100

        precio_final = precio_iva + resultado_suma

        texto = f"El resultado con el IVA es {precio_final}"

        alert("TP 1", texto)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()