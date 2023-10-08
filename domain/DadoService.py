import infrastructure.dadoDAO as dadoDAO

import numpy as np

def registrar(user, dado):
    registrar = dadoDAO.registrarDado(user, dado)
    return registrar

def registrarQnt(user, dado):
    registrar = dadoDAO.registrarDadoQnt(user, dado)
    return registrar

def mostrar(user):
    return dadoDAO.read(user)

def analisePareto(user):
    dados = dadoDAO.readPareto(user)
    dados_sem_duplicata = list(set(dados))
    listaMatrizes = []

    frAcumulada = 0

    for i in range(len(dados_sem_duplicata)):
        caso = []
        contador = dados.count(dados_sem_duplicata[i])
        percentual = (contador / len(dados)) * 100

        frAcumulada += percentual

        caso.append(dados_sem_duplicata[i])
        caso.append(contador)
        caso.append(format(percentual, ".2f"))
        caso.append(format(frAcumulada, ".2f"))
        listaMatrizes.append(caso)
        print(listaMatrizes)

    return listaMatrizes

def analiseQnt(user):
    dados = dadoDAO.readQnt(user)
    listaDados = []

    for i in range(len(dados)):
        listaDados.append(dados[i][0])

    listaDados.sort()

    maiorNum = listaDados[-1]
    menorNum = listaDados[1]
    amplitude = maiorNum - menorNum

    media = sum(listaDados) / len(listaDados)

    antigoCont = 0

    for i in range(len(listaDados)):
        cont = listaDados.count(listaDados[i])

        if cont > antigoCont:
            maiorCont = cont
            moda = listaDados[i]
        else:
            maiorCont = antigoCont

        antigoCont = cont

    primeiroQuartil = np.quantile(listaDados, .25)
    mediana = np.quantile(listaDados, .5)
    terceiroQuartil = np.quantile(listaDados, .75)

    print("maior numero: " , maiorNum)
    print("menor numero" , menorNum)
    print("amplitude " , amplitude)
    print("media " , media)
    print("mediana " , mediana)
    print("moda " , moda)
    print("1 quartil " , primeiroQuartil)
    print("3 quartil " , terceiroQuartil)

def deletar(user):
    return dadoDAO.deletar(user)

