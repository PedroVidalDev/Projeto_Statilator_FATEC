import infrastructure.userDAO as userDAO

def registrar(name, email, password, confirm):

    if(name == "" or email == "" or password == "" or confirm == ""):
        return False

    elif(password != confirm):
        return False
    
    else: 
        userRegisterAuth = userDAO.criarUser(name, email, password)
        return userRegisterAuth

def entrar(email, password):
    user = userDAO.validarUser(email)
    if(user is None):
        return False
    else:
        if(user[3] == password):
            return user
        else:
            return False