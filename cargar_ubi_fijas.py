import pickle

def search(lista, esquina):
    for elemento in lista:
        if elemento[0] == esquina:
            return elemento
    return False


###{(e1,e3,7)}
def check_direccion(direccion,monto):
    ###Utilizo el grafo
    with open('file', 'br') as f:
        map = pickle.load(f)
    try:
        dir1= map.get(direccion[0][0])
        dir2 = map.get(direccion[1][0])
        if dir1 != None:
            if dir2 != None:
                #print("6")
                ###Comprobamos si son adyacentes
                if (search(dir1, direccion[1][0]) == False and search(dir2, direccion[0][0]) == False):
                    print("3")
                    return []
                ###Comprobamos si la distancia es correcta y doble mano
                else:
                    #print("7")
                    if (search(dir1, direccion[1][0]) != False and search(dir2, direccion[0][0]) != False):
                        #print("8")
                        valor = search(dir1, direccion[1][0])
                        if valor[1] == direccion[0][1] + direccion[1][1]:
                            direccion.insert(0,True)
                            if monto!=None:
                                direccion.insert(0,monto)
                                return direccion
                            else:
                                return direccion
                        else:
                            return []
                    elif search(dir1, direccion[1][0]) != False:
                        #print("9")
                        valor = search(dir1, direccion[1][0])
                        #print(valor[1],direccion[0][1],direccion[1][1])
                        if valor[1] == direccion[0][1] + direccion[1][1]:
                            #print("11")
                            obj=direccion.pop()
                            direccion.insert(0,obj)
                            
                            direccion.insert(0,False)
                            if monto!=None:
                                direccion.insert(0,monto)
                                return direccion
                            else:
                                return direccion
                        else:
                            ##las propociones son incorrectas
                            print("4")
                            return []
                    elif search(dir2, direccion[0][0]) != False:
                        #print("10")
                        valor = search(dir2, direccion[0][0])
                        if valor[1] == direccion[0][1] + direccion[1][1]:

                            direccion.insert(0,False)
                            if monto!=None:
                                direccion.insert(0,monto)
                                return direccion
                            else:
                                return direccion
                        else:
                            print("5")
                            return[]
            else:
                print("1")
                return []
        else: 
            print("2")
            return []
    except ValueError:
        check = False
        return check
        

#direccion = (('e1', 25), ('e2', 30))
##print(direccion[0][0])

##{(ex,10),(ey, 5)}
def load_fix_element (nombre,dirección):
    ###Cambiar condicion a nombre != Nombres de lod elementos fijos
    if nombre!=None and (nombre[0]!= "H" or nombre[0]=="A" or nombre[0]!= "T" or nombre[0]=="S" or nombre[0]!= "E" or nombre[0]=="K" or nombre[0]=="I"):
        direc=direccion_lista(dirección)
        #print(direc)
        direc=check_direccion(direc,None)
        with open("dic_ubi_fijo","rb") as f:
            dic_fijo = pickle.load(f)
        ###Agregamos al diccionario el objeto fijo
        dic_fijo[nombre] = direc
        print(dic_fijo)
        with open("dic_ubi_fijo","wb") as f:
            pickle.dump(dic_fijo,f)
    else:
        print("nombre erroneo")
        return False
"""
H: hospital A: almacén T: tienda S: supermercado E: escuela K: kiosco I: iglesia
"""
    

###direccion en string a direccion en lista
def direccion_lista(direccion):
    peso=[0,0]
    direc=True 
    dir1=[]
    dir2=[]
    i=0
    comprobante=False
    for carac in direccion:
        #print(carac,direc)
        if carac=="(" or carac=="<":
            comprobante=True
            direc=True
            #print("-1")

        elif carac==")" or carac==">":
            #print("-2")
            comprobante=False
            if i==1:
                break
            else:
                i+=1
        elif comprobante:
            #print("-3")
            if carac==",":
                direc=False
            else:
                if direc:
                
                    if i==0:
                        dir1.append(carac)
                    else:
                        dir2.append(carac)
            
                else:
                    #print(carac)
                    peso[i]=peso[i]*10+int(carac)
    dir1= ''.join(dir1)
    dir2= ''.join(dir2)
    direccionf=[[dir1,peso[0]],[dir2,peso[1]]]
    return direccionf

(load_fix_element("H10","(e1,4) (e3,3)"))
#(e1,e2,11)
(load_fix_element("H8","(e1,7) (e2,4)"))
(load_fix_element("H2","(e1,7) (e2,4)"))