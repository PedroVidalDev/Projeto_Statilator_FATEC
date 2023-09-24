import application.loginMenu as loginMenu
import application.registerMenu as registerMenu
import application.registrarDado as registrarDadoFront
import application.mostrarDado as mostrarDado
import application.deletarDado as deletarDado
import application.analiseParetoDado as analisePareto

def verificarMenu(esc):
    if(esc == 1):
        registerMenu.registerFront()
    elif(esc == 2):
        loginMenu.loginFront()
    else:
        print("Eu ando consumindo esse mal nada mal geto cumpriu seu dever")

def verificarUserMenu(esc, user):
    if(esc == 1):
        registrarDadoFront.registrarDadoFront(user)
    elif(esc == 2):
        mostrarDado.mostrarDadoFront(user)        
    elif(esc == 3):
        analisePareto.analiseParetoFront(user)
    elif(esc == 4):
        deletarDado.deletarDadoFront(user)
    else:
        print("Escolha invalida")
