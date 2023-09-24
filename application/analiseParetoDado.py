import domain.DadoService as DadoService

from prettytable import PrettyTable
import customtkinter
from tkinter import ttk
from tkinter import *

def analiseParetoFront(user):
    
    def sairFunction():
        app.destroy()

    casos = DadoService.analisePareto(user)
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("1000x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    columns = ("Nome", "Qnt.", "Fr%", "Fr Acu.")

    style = ttk.Style()
    style.configure("Treeview",
                    background="grey",
                    foreground="lightgreen"
                    )

    tv = ttk.Treeview(master=app, column=columns, show="headings")

    tv.column("Nome", anchor=CENTER)
    tv.column("Qnt.", anchor=CENTER)
    tv.column("Fr%", anchor=CENTER)
    tv.column("Fr Acu.", anchor=CENTER)

    tv.heading("Nome", text="Nome", anchor=CENTER)
    tv.heading("Qnt.", text="Qnt.", anchor=CENTER)
    tv.heading("Fr%", text="Fr%", anchor=CENTER)
    tv.heading("Fr Acu.", text="Fr Acu.", anchor=CENTER)

    tv.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    for caso in casos:
        tv.insert("",END, values=caso)

    buttonLoginMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonLoginMenu.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()