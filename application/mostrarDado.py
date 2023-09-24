import domain.DadoService as DadoService

import customtkinter

def mostrarDadoFront(user):  

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

    ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app)
    ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

    dados = DadoService.mostrar(user)

    y = 0.3

    for i in range(len(dados)):
        labelDado = customtkinter.CTkLabel(master=app, text=f"ID: {dados[i][0]} \nNome: {dados[i][1]} \nData da ocorrencia: {dados[i][2]}")
        labelDado.place(relx=0.5, rely=y, anchor=customtkinter.CENTER)
        y = y + 0.1
    
    buttonLoginMenu = customtkinter.CTkButton(master=app, text="Sair", command=lambda:sairFunction())
    buttonLoginMenu.place(relx=0.5, rely=y+0.1, anchor=customtkinter.CENTER)

    app.mainloop()