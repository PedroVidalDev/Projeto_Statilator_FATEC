import infrastructure.dadoDAO as dadoDAO

def registrar(user, dado):
    registrar = dadoDAO.registrarDado(user, dado)
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

def deletar(user):
    return dadoDAO.deletar(user)

