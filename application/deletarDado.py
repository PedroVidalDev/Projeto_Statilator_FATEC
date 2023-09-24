import domain.DadoService as DadoService

import customtkinter

def deletarDadoFront(user):
    def sairFunction():
        app.destroy()
    
    DadoService.deletar(user)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("400x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    labelDeletar = customtkinter.CTkLabel(master=app, text="Dados delatados com sucesso!", text_color="#FF4500")
    labelDeletar.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
    
    buttonLoginMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonLoginMenu.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()