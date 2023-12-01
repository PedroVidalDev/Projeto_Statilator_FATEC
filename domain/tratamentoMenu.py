import application.loginMenu as loginMenu
import application.registerMenu as registerMenu
import application.registrarDado as registrarDadoFront
import application.registrarDadoQnt as registrarDadoQnt
import application.deletarDado as deletarDado
import application.analiseParetoDado as analisePareto
import application.analiseDadoQnt as analiseDadoQnt
import application.analiseBinomial as analiseBinomial

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
    elif(esc == 3):
        registrarDadoQnt.registrarDadoFront(user)       
    elif(esc == 2):
        analisePareto.analiseParetoFront(user)
    elif(esc == 4):
        analiseDadoQnt.analiseQntFront(user)
    elif(esc == 5):
        analiseBinomial.binomialFront(user)
    elif(esc == 6):
        deletarDado.deletarDadoFront(user)
    else:
        print("Escolha invalida")
