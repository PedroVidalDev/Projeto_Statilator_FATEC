import domain.DadoService as DadoService

import customtkinter
from tkinter import ttk
from tkinter import *

def analiseQntFront(user):
    
    def sairFunction():
        app.destroy()

    analise = DadoService.analiseQnt(user)
    dadosTabela = DadoService.organizarDadosTabelaQnt(user, analise[8], analise[9])
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("1000x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    labelMaior = customtkinter.CTkLabel(master=app, text=f"Maior numero = {analise[0]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMaior.place(relx=0.25, rely=0.2, anchor=customtkinter.CENTER)

    labelMenor = customtkinter.CTkLabel(master=app, text=f"Menor numero = {analise[1]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMenor.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    labelAmplitude = customtkinter.CTkLabel(master=app, text=f"Amplitude = {analise[2]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelAmplitude.place(relx=0.75, rely=0.2, anchor=customtkinter.CENTER)

    labelMedia = customtkinter.CTkLabel(master=app, text=f"Media = {analise[3]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMedia.place(relx=0.25, rely=0.25, anchor=customtkinter.CENTER)

    labelMediana = customtkinter.CTkLabel(master=app, text=f"Mediana = {analise[4]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelMediana.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

    labelModa = customtkinter.CTkLabel(master=app, text=f"Mediana = {analise[5]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelModa.place(relx=0.75, rely=0.25, anchor=customtkinter.CENTER)

    labelPrimeiroQuartil = customtkinter.CTkLabel(master=app, text=f"1 quartil = {analise[6]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelPrimeiroQuartil.place(relx=0.25, rely=0.30, anchor=customtkinter.CENTER)

    labelTerceiroQuartil = customtkinter.CTkLabel(master=app, text=f"3 quartil = {analise[7]}", font=customtkinter.CTkFont(size=15, weight="bold"))
    labelTerceiroQuartil.place(relx=0.5, rely=0.30, anchor=customtkinter.CENTER)

    columns = ("Intervalo", "Qnt.", "Fr", "Fr%", "Fr Acu.")

    style = ttk.Style()
    style.configure("Treeview",
                    background="grey",
                    foreground="lightgreen"
                    )

    tv = ttk.Treeview(master=app, column=columns, show="headings")

    tv.column("Intervalo", anchor=CENTER)
    tv.column("Qnt.", anchor=CENTER)
    tv.column("Fr", anchor=CENTER)
    tv.column("Fr%", anchor=CENTER)
    tv.column("Fr Acu.", anchor=CENTER)

    tv.heading("Intervalo", text="Intervalo", anchor=CENTER)
    tv.heading("Qnt.", text="Qnt.", anchor=CENTER)
    tv.heading("Fr", text="Fr", anchor=CENTER)
    tv.heading("Fr%", text="Fr%", anchor=CENTER)
    tv.heading("Fr Acu.", text="Fr Acu.", anchor=CENTER)

    tv.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    for dado in dadosTabela:
        tv.insert("",END, values=dado)

    buttonSairMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonSairMenu.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()