import domain.UserService as UserService
import application.loginMenu as loginMenu

import customtkinter

def registerFront():

    def registrarFunction():
        auth = UserService.registrar(inputNome.get(), inputEmail.get(), inputSenha.get(), inputConfirm.get())
        if auth == True:
            labelResp = customtkinter.CTkLabel(master=app, text="Usuario criado com sucesso.", text_color="#008000")
            labelResp.place(relx=0.50, rely=0.55, anchor=customtkinter.CENTER)
            app.destroy()
            loginMenu.loginFront()
        else:
            labelResp = customtkinter.CTkLabel(master=app, text="Erro ao criar usuario...", text_color="#ff0000")
            labelResp.place(relx=0.50, rely=0.55, anchor=customtkinter.CENTER)

    def sairFunction():
        app.destroy()
    

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("400x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Cadastro", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    labelNome = customtkinter.CTkLabel(master=app, text="Nome:")
    labelNome.place(relx=0.20, rely=0.2, anchor=customtkinter.CENTER)
    inputNome = customtkinter.CTkEntry(master=app, width=200)
    inputNome.place(relx=0.65, rely=0.2, anchor=customtkinter.CENTER)

    labelEmail = customtkinter.CTkLabel(master=app, text="Email:")
    labelEmail.place(relx=0.20, rely=0.3, anchor=customtkinter.CENTER)
    inputEmail = customtkinter.CTkEntry(master=app, width=200)
    inputEmail.place(relx=0.65, rely=0.3, anchor=customtkinter.CENTER)

    labelSenha = customtkinter.CTkLabel(master=app, text="Senha:")
    labelSenha.place(relx=0.20, rely=0.4, anchor=customtkinter.CENTER)
    inputSenha = customtkinter.CTkEntry(master=app, width=200, show="*")
    inputSenha.place(relx=0.65, rely=0.4, anchor=customtkinter.CENTER)

    labelConfirm = customtkinter.CTkLabel(master=app, text="Confirmar senha:")
    labelConfirm.place(relx=0.20, rely=0.5, anchor=customtkinter.CENTER)
    inputConfirm = customtkinter.CTkEntry(master=app, width=200, show="*")
    inputConfirm.place(relx=0.65, rely=0.5, anchor=customtkinter.CENTER)

    buttonRegisterMenu = customtkinter.CTkButton(master=app, text="Registrar", command=lambda:registrarFunction())
    buttonRegisterMenu.place(relx=0.7, rely=0.6, anchor=customtkinter.CENTER)
    
    buttonLoginMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonLoginMenu.place(relx=0.3, rely=0.60, anchor=customtkinter.CENTER)

    app.mainloop()
