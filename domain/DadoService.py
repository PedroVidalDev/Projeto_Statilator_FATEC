import infrastructure.dadoDAO as dadoDAO

import numpy as np
from scipy.stats import binom 
import matplotlib.pyplot as plt

def registrar(user, dado):
    registrar = dadoDAO.registrarDado(user, dado)
    return registrar

def registrarQnt(user, dado):
    registrar = dadoDAO.registrarDadoQnt(user, dado)
    return registrar

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

    qntClasses = 1 + 3.33 * np.log10(len(listaDados))
    tamanhoClasse = round(amplitude / qntClasses)

    return [maiorNum, menorNum, amplitude, media, mediana, moda, primeiroQuartil, terceiroQuartil, qntClasses, tamanhoClasse]

def organizarDadosTabelaQnt(user, qntClasse, tamanhoClasse):
    dados = dadoDAO.readQnt(user)
    listaDados = []

    for i in range(len(dados)):
        listaDados.append(dados[i][0])

    listaDados.sort()

    # OBTENDO OS INTERVALOS DA TABELA PARA ANALISE #
    intervalos = [listaDados[0]]
    intervaloAtual = intervalos[0]
    
    while intervaloAtual <= listaDados[len(listaDados) - 1]:
        intervaloAtual = intervaloAtual + tamanhoClasse
        intervalos.append(intervaloAtual)

    # OBTENDO QNT DE OCORRENCIA EM CADA INTERVALO #
    qntDeOcorrencia = []
    contador = 0

    for i in range(len(intervalos) - 1):

        for j in range(len(listaDados)):
            if(listaDados[j] >= intervalos[i] and listaDados[j] < intervalos[i+1]):
                contador = contador + 1

        qntDeOcorrencia.append(contador)
        contador = 0

    # OBTENDO A FREQUENCIA DE CADA INTERVALO TENDO COMO BASE O TOTAL DE OCORRENCIAS #
    totalOcorrencia = len(listaDados)
    listaFr = []

    for i in range(len(qntDeOcorrencia)):
        freq = qntDeOcorrencia[i] / totalOcorrencia
        listaFr.append(freq)

    # OBTENDO A FREQUENCIA EM PORCENTAGEM #
    listaFrPorc = []

    for i in range(len(listaFr)):
        listaFrPorc.append(listaFr[i] * 100)

    # OBTENDO A FRENQUENCIA ACUMULADA #
    listaFrAcumulada = [0]
    contadorFr = 0

    for i in range(len(listaFrPorc)):
        contadorFr = contadorFr + listaFrPorc[i]
        listaFrAcumulada.append(contadorFr)

    print(listaFrAcumulada)

    # FORMATANDO FORMA QUE OS INTERVALOS SERAO MOSTRADOS NA TABELA #
    intervalosTexto = []

    for i in range(len(intervalos) - 1):
        texto = f"{intervalos[i]}| --{intervalos[i+1]}"
        intervalosTexto.append(texto)

    # COLOCANDO TUDO DENTRO DE APENAS UMA LISTA #
    dadosTabela = []
    for i in range(len(intervalosTexto)):
        dadosTabela.append([
            intervalosTexto[i],
            qntDeOcorrencia[i],
            listaFr[i],
            listaFrPorc[i],
            listaFrAcumulada[i]
        ])
    dadosTabela.append([
        "Total",
        sum(qntDeOcorrencia),
        sum(listaFr),
        sum(listaFrPorc),
        listaFrAcumulada[len(listaFrAcumulada) - 1],
    ])

    return dadosTabela

def realizarBinomial(n, p):
    x = range(0,n+1) # valores de x =0,1,2,3 ...
    p_x = binom.pmf(x,n,p) #distribuição dos resultados
    print (x)
    print (p_x)
    for i,val in enumerate(p_x):
        print (f'p(x)={i} \t\t {val:.2%}')
    #Grafico
    fig, ax = plt.subplots(figsize=(8, 3.5), dpi=150)

    plt.xlabel('x')
    plt.ylabel('p(x)')
    
    ax.set_facecolor("gray")
    
    for a,b in zip(x, p_x):
        plt.text(a-0.5, b-0.0, str(round(b*100,2))+"%", color='white')
    plt.title('Distribuição Binomial')
    plt.bar(x,p_x,width=0.5,color='blue')
    ####
    plt.show()

def deletar(user):
    return dadoDAO.deletar(user)

