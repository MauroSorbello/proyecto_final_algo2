import pickle

def search(lista, esquina):
    for elemento in lista:
        if elemento[0] == esquina:
            return elemento
    return False

def load_movil_element(nombre,direccion,monto):
    ##Comprobamos la direccion 
    ##Ingreso de personas
    if nombre[0] == 'P':
        pass
    ##Ingreso de autos
    elif nombre[0] == 'C':
        pass
    else:
        return('El elemento ingresado no corresponde con un elemento movil.')

###{(e1,e3,7)}
def check_direccion(direccion):
    ###Utilizo el grafo
    with open('file', 'br') as f:
        map = pickle.load(f)
    try:
        dir1 = map[direccion[0][0]]
        dir2 = map[direccion[1][0]]
        if dir1 != None:
            if dir2 != None:
                ###Comprobamos si son adyacentes
                if (search(dir1, direccion[1][0]) == False and search(dir2, direccion[0][0]) == False):
                    return('Las esquinas proporcionadas no son adyacentes')
                ###Comprobamos si la distancia es correcta y doble mano
                else:
                    if (search(dir1, direccion[1][0]) != False and search(dir2, direccion[0][0]) != False):
                        valor = search(dir1, direccion[1][0])
                        if valor[1] == direccion[0][1] + direccion[1][1]:
                            pass ###Codigo doble mano y dist correcta
                        else:
                            return('La distancia del objeto movil hacia las esquinas es incorrecta')
                    elif search(dir1, direccion[1][0]) != False:
                        valor = search(dir1, direccion[1][0])
                        if valor[1] == direccion[0][1] + direccion[1][1]:
                            pass ###Codigo una mano y dist correcta
                        else:
                            return('La distancia del objeto movil hacia las esquinas es incorrecta')
                    elif search(dir2, direccion[0][0]) == True:
                        valor = search(dir2, direccion[0][0])
                        if valor[1] == direccion[0][1] + direccion[1][1]:
                            pass ###Codigo una mano y dist correcta
                        else:
                            return('La distancia del objeto movil hacia las esquinas es incorrecta')
    except ValueError:
        check = False
        return check
        

direccion = (('e1', 25), ('e2', 30))
print(direccion[0][0])

