import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		-A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		-B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		-C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		-D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		-E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        lamparitas = self.combobox_cantidad.get()
        empresa = self.combobox_marca.get()

        lamparitas = int(lamparitas)
        precio = 800
        resultado = None

        if lamparitas >= 6:
            resultado = lamparitas * precio
            descuento = resultado * 50 / 100
            resultado_final = resultado - descuento
        else:
            if lamparitas == 5 and empresa == "ArgentinaLuz":
                resultado = lamparitas * precio
                descuento = resultado * 40 / 100
                resultado_final = resultado - descuento
            else:
                if lamparitas == 5 and empresa != "ArgentinaLuz":
                    resultado = lamparitas * precio
                    descuento = resultado * 30 / 100
                    resultado_final = resultado - descuento
                else:
                    if lamparitas == 4 and (empresa == "ArgentinaLuz" or empresa == "FelipeLamparas"):
                        resultado = lamparitas * precio
                        descuento = resultado * 25 / 100
                        resultado_final = resultado - descuento
                    else:
                        if lamparitas == 4 and empresa != "ArgentinaLuz" and empresa != "FelipeLamparas":
                            resultado = lamparitas * precio
                            descuento = resultado * 20 / 100
                            resultado_final = resultado - descuento
                        else:
                            if lamparitas == 3 and empresa == "ArgentinaLuz":
                                resultado = lamparitas * precio
                                descuento = resultado * 15 / 100
                                resultado_final = resultado - descuento
                            else:
                                if lamparitas == 3 and empresa == "FelipeLamparas":
                                    resultado = lamparitas * precio
                                    descuento = resultado * 10 / 100
                                    resultado_final = resultado - descuento
                                else:
                                    if lamparitas == 3 and empresa != "ArgentinaLuz" and empresa != "FelipeLamparas":
                                        resultado = lamparitas * precio
                                        descuento = resultado * 5 / 100
                                        resultado_final = resultado - descuento
                                    else:
                                        if lamparitas < 3:
                                            resultado_final = lamparitas * precio

        print(resultado_final)
        if resultado_final > 4000:
            descuento = resultado_final * 5 / 100
            resultado_final = resultado_final - descuento

        print(resultado_final)

        texto = f"El importe final es de: {resultado_final}"
        alert("TP 4", texto)
        #linea 69 84 and o or ?????????????? resultado.__str__() + " " + descuento.__str__() + " " + 

"""     importe = self.txt_importe.get()
        descuento = self.txt_descuento.get()
        resultado = int(importe) * int(descuento) / 100
        resultado_con_descuento = int(importe) - int(resultado) 
        alert("Ejercicio 10", "El importe tras el descuento es: " + resultado_con_descuento.__str__())
"""
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()