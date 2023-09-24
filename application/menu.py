import domain.tratamentoMenu as tratamentoMenu

import customtkinter

def menu():

    def function(esc):
        app.destroy()
        tratamentoMenu.verificarMenu(esc)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Statilator Project")
    app.geometry("400x700")
    app.resizable(width=False, height=False)

    labelTitle = customtkinter.CTkLabel(master=app, text="Statilator", font=customtkinter.CTkFont(size=60, weight="bold"))
    labelTitle.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

    buttonRegisterMenu = customtkinter.CTkButton(master=app, text="Registrar", command=lambda:function(1))
    buttonRegisterMenu.place(relx=0.7, rely=0.5, anchor=customtkinter.CENTER)
    
    buttonLoginMenu = customtkinter.CTkButton(master=app, text="Entrar", command=lambda:function(2))
    buttonLoginMenu.place(relx=0.30, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()