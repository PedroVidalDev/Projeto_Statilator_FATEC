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

    buttonSairMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonSairMenu.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()