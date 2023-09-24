import domain.DadoService as DadoService

import customtkinter

def registrarDadoFront(user):

    def registrarFunction():
        auth = DadoService.registrar(user, inputDado.get())
        if auth == True:
            labelResp = customtkinter.CTkLabel(master=app, text="Dado registrado!", text_color="#008000")
            labelResp.place(relx=0.50, rely=0.4, anchor=customtkinter.CENTER)
        else:
            labelResp = customtkinter.CTkLabel(master=app, text="Dado nao registrado...", text_color="#ff0000")
            labelResp.place(relx=0.50, rely=0.4, anchor=customtkinter.CENTER)

    def sairFunction():
        app.destroy()
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("400x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    labelDado = customtkinter.CTkLabel(master=app, text="Dado:")
    labelDado.place(relx=0.20, rely=0.3, anchor=customtkinter.CENTER)
    inputDado = customtkinter.CTkEntry(master=app, width=200)
    inputDado.place(relx=0.65, rely=0.3, anchor=customtkinter.CENTER)

    buttonRegisterMenu = customtkinter.CTkButton(master=app, text="Registrar", command=lambda:registrarFunction())
    buttonRegisterMenu.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)
    
    buttonLoginMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonLoginMenu.place(relx=0.3, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()
    
