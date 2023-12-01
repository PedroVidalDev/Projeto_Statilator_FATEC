import domain.DadoService as DadoService

from prettytable import PrettyTable
import customtkinter
from tkinter import ttk
from tkinter import *

def analiseQntFront(user):
    
    def sairFunction():
        app.destroy()

    casos = DadoService.analiseQnt(user)
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("1000x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    labelMaior = customtkinter.CTkLabel(master=app, text=f"Maior numero = {casos[0]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMaior.place(relx=0.25, rely=0.2, anchor=customtkinter.CENTER)

    labelMenor = customtkinter.CTkLabel(master=app, text=f"Menor numero = {casos[1]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMenor.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    labelAmplitude = customtkinter.CTkLabel(master=app, text=f"Amplitude = {casos[2]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelAmplitude.place(relx=0.75, rely=0.2, anchor=customtkinter.CENTER)

    labelMedia = customtkinter.CTkLabel(master=app, text=f"Media = {casos[3]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMedia.place(relx=0.25, rely=0.25, anchor=customtkinter.CENTER)

    labelMediana = customtkinter.CTkLabel(master=app, text=f"Mediana = {casos[4]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMediana.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

    labelModa = customtkinter.CTkLabel(master=app, text=f"Mediana = {casos[5]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelModa.place(relx=0.75, rely=0.25, anchor=customtkinter.CENTER)

    labelPrimeiroQuartil = customtkinter.CTkLabel(master=app, text=f"1 quartil = {casos[6]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelPrimeiroQuartil.place(relx=0.25, rely=0.30, anchor=customtkinter.CENTER)

    labelTerceiroQuartil = customtkinter.CTkLabel(master=app, text=f"3 quartil = {casos[7]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelTerceiroQuartil.place(relx=0.5, rely=0.30, anchor=customtkinter.CENTER)

    buttonSairMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonSairMenu.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()