import customtkinter

import domain.DadoService as service

def binomialFront(user):
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("400x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    labelAmostra = customtkinter.CTkLabel(master=app, text="Amostra:")
    labelAmostra.place(relx=0.20, rely=0.3, anchor=customtkinter.CENTER)

    inputAmostra = customtkinter.CTkEntry(master=app, width=200)
    inputAmostra.place(relx=0.65, rely=0.3, anchor=customtkinter.CENTER)

    labelChance = customtkinter.CTkLabel(master=app, text="Chance:")
    labelChance.place(relx=0.20, rely=0.35, anchor=customtkinter.CENTER)

    inputChance = customtkinter.CTkEntry(master=app, width=200)
    inputChance.place(relx=0.65, rely=0.35, anchor=customtkinter.CENTER)

    buttonSend = customtkinter.CTkButton(master=app, text="Enviar", command=lambda:service.realizarBinomial(int(inputAmostra.get()), float(inputChance.get())))
    buttonSend.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()