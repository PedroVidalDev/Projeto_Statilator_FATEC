import domain.tratamentoMenu as tratamentoMenu

import customtkinter

def userFront(user):
    def function(esc):
        if(esc == 7):
            app.destroy()
        else:
            tratamentoMenu.verificarUserMenu(esc, user)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("400x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)

    buttonAddDado = customtkinter.CTkButton(master=app, text="Adicionar dado", command=lambda:function(1))
    buttonAddDado.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

    buttonAddDadoQnt = customtkinter.CTkButton(master=app, text="Adiocionar dado qnt.", command=lambda:function(2))
    buttonAddDadoQnt.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
    
    buttonListarDados = customtkinter.CTkButton(master=app, text="Listar dados", command=lambda:function(3))
    buttonListarDados.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

    buttonPareto = customtkinter.CTkButton(master=app, text="Realizar analise de pareto", command=lambda:function(4))
    buttonPareto.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

    buttonPareto = customtkinter.CTkButton(master=app, text="Realizar analise quantitativa", command=lambda:function(5))
    buttonPareto.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

    buttonLimparBanco = customtkinter.CTkButton(master=app, text="Resetar registros", command=lambda:function(6))
    buttonLimparBanco.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    buttonSair = customtkinter.CTkButton(master=app, text="Sair", command=lambda:function(7))
    buttonSair.place(relx=0.5, rely=0.60, anchor=customtkinter.CENTER)

    app.mainloop()
