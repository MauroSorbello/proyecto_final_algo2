import math
import pickle

def Floyd_Warshall(graph): #O(V^3)
    #Añadir vertices  
    for elemento1 in graph:
        for elemento2 in graph:
            for elemento3 in graph:
                #Comparamos 
                num = min(graph[elemento2][elemento3][0], graph[elemento2][elemento1][0] + graph[elemento1][elemento3][0])
                if num < graph[elemento2][elemento3][0]:
                    #Actualizamos la distancia y el vertice
                    graph[elemento2][elemento3][0] = num 
                    graph[elemento2][elemento3][1] = elemento1

def leer_mapa(archivo):
    file = open(archivo, 'r')
    dic=dict()
    b=False


    file = open(archivo, 'r')
    ###loop para el conjunto de esquinas
    while True:
        l=[]
        char = file.read(1)
        #print("¡¡¡")

        #print(char)
        if char=="}":
            break
        if char=="e":
            while char!=",":
                ###crea una variable con el nombre de la esquina y la guarda en el diccionario como key para una lista vacia
                l.append(char)
                char=file.read(1)

                ##si hay un salto de pagina sigue leyendo
                if char=="\n":
                    char=file.read(1)
                ##si ya no queda nada en el conjunto termina el loop
                if char=="}":
                    b=True 
                    break
                #print("jjj")
            dic["".join(l)]=[]
            
        if b:
            break
        
        b=False 
    
    #Creo el diccionario de F-W (Dentro tiene una lista con la letra de adyacencia y el valor) O(V^2)
    dictFW = dict()
    for elemento1 in dic:
        dictFW["".join(elemento1)] = {}
        for elemento2 in dic:
            if elemento1 != elemento2:
                dictFW[elemento1][elemento2] = [math.inf, elemento2]
            else:
                dictFW[elemento1][elemento2] = [0, elemento2]
    
    ###s {<e1,e2,c>,<e3,e4,c>, <e2,e1,c>
    ##ahora empieza a leer el conjunto de calles 
    while True:

        char = file.read(1)


        ### si encuentra ese carecter significa que el conjunto ya no tiene más elementos y tiene que terminar.
        if char=="}":
            break

        if char=="(" or char=="<":
            char = file.read(1)
            primer_e=[]

            while char != ",":
                primer_e.append(char)
                char = file.read(1)
                
            prim = "".join(primer_e)
            char=file.read(1)
            segunda_e=[]
            while char != ",":
                segunda_e.append(char)
                char = file.read(1)
            segun = "".join(segunda_e)

        
            char=file.read(1)

            peso=0
            while char!=")" and char!=">":
                ##print(char)
                peso=peso*10+int(char)
                char=file.read(1)
            


            ##print(primer_e,prim,"II",segunda_e,segun,"II",peso)
            dic[prim].append([segun,peso])
            #Actualizo la distancia de los vertices adyacentes en el dic de Floyd-Warshall
            dictFW[prim][segun][0] = peso

    file.close()
    #Usamos el algoritmo de Floyd-Warshall
    Floyd_Warshall(dictFW)
    with open("file","wb") as f:
        pickle.dump(dic,f)
    with open("dicFloyd_Warshall","wb") as f:
        pickle.dump(dictFW,f)

    #print(dictFW)
    ###Crearemos tambien los archivos para elementos moviles y fijos
    dic_movil = dict()
    dic_fijo = dict()

    with open("dic_ubi_movil","wb") as f:
        pickle.dump(dic_movil,f)

    with open("dic_ubi_fijo","wb") as f:
        pickle.dump(dic_fijo,f)

    print("map created successfully")
    return dic

def leer_esquinas(line):
    l=[]
    for caracter in line:
        if caracter=="\n":
            break
        l.append(caracter)
    return ("".join(l))


def load_fix_element (nombre,dirección):
    ###Cambiar condicion a nombre != Nombres de lod elementos fijos
    if nombre!=None and (nombre[0]!= "H" or nombre[0]=="A" or nombre[0]!= "T" or nombre[0]=="S" or nombre[0]!= "E" or nombre[0]=="K" or nombre[0]=="I"):
        direc=direccion_lista(dirección)
        #print(direc)
        direc=check_direccion(direc,None)
        if direc==[]:
            print("direccion erronea")
            return
        with open("dic_ubi_fijo","rb") as f:
            dic_fijo = pickle.load(f)
        ###Agregamos al diccionario el objeto fijo
        dic_fijo[nombre] = direc
        #print(direc)
        #print(dic_fijo)
        with open("dic_ubi_fijo","wb") as f:
            pickle.dump(dic_fijo,f)
    else:
        print("nombre erroneo")
        return False
    

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

def load_fix_element (nombre,dirección):
    ###Cambiar condicion a nombre != Nombres de lod elementos fijos
    if nombre!=None and (nombre[0]!= "H" or nombre[0]=="A" or nombre[0]!= "T" or nombre[0]=="S" or nombre[0]!= "E" or nombre[0]=="K" or nombre[0]=="I"):
        direc=direccion_lista(dirección)
        #print(direc)
        direc=check_direccion(direc,None)
        if direc==[]:
            print("direccion erronea")
            return
        with open("dic_ubi_fijo","rb") as f:
            dic_fijo = pickle.load(f)
        ###Agregamos al diccionario el objeto fijo
        dic_fijo[nombre] = direc
        #print(direc)
        #print(dic_fijo)
        with open("dic_ubi_fijo","wb") as f:
            pickle.dump(dic_fijo,f)
    else:
        print("nombre erroneo")
        return False
    
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
                    #print("3")
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
                            #print("4")
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
                            #print("5")
                            return[]
            else:
                #print("1")
                return []
        else: 
            #print("2")
            return []
    except ValueError:
        check = False
        return check
    

def search(lista, esquina):

    for elemento in lista:
        if elemento[0] == esquina:
            return elemento
    return False

def load_movil_element(nombre,direccion,monto):
    direc = direccion_lista(direccion)
    #print(direc)
    if nombre != None and (nombre[0] == 'P' or nombre[0] == "C"):
        direc=check_direccion(direc,monto)
        if direc==[]:
            print("direccion incorrecta")
            return

       #Cargamos el archivo
        with open("dic_ubi_movil","rb") as f:
            dic_movil = pickle.load(f)
        ###Agregamos al diccionario el objeto movil
        dic_movil[nombre] = direc
        #print(dic_movil)
        with open("dic_ubi_movil","wb") as f:
            pickle.dump(dic_movil,f)
    else:
        print("nombre erroneo")
        return False
    


def create_trip(persona,destino):

    ##mapa 
    with open('file','br') as f:
        map=pickle.load(f)

    ##diccionario de las ubicaciones fijas
    with open('dic_ubi_movil','br') as g:
        dicmovil=pickle.load(g)

    ##matriz Floyd Warshall del mapa
    with open('dicFloyd_Warshall','br') as h:
        matriz=pickle.load(h)

    ##diccionario de las ubicaciones fijas
    with open('dic_ubi_fijo','br') as j:
        dicfijo=pickle.load(j)

    ##print(dicfijo)
    ##devuelve una lista de los tres autos mas cercanos
    per=dicmovil.get(persona,False)
    if not per:
        print("no se encuentra la persona")
        return

    L_cars=los_autos_más_cercanos(persona,dicmovil,matriz)

    
    ###significa que el destino es una ubicacion
    if destino[0]=="(" or destino[0]=="{" or destino[0]=="<":
            des= direccion_lista(destino)
            #print (des)
            eq2=search(map[des[0][0]],des[1][0])
            eq1=search(map[des[1][0]],des[0][0])
            if eq1==False:
                if eq2==False:
                    print("direccion erronea")
                    return
                else:
                    if des[0][1]+des[1][1]!=eq2[1]:
                        print("direccion erronea")
                        return
                    else:
                        des=[False,des[1],des[0]]
            elif eq2==False:
                if des[0][1]+des[1][1]!=eq1[1]:
                        print("direccion erronea")
                        return
                else:
                    des=[False,des[0],des[1]]
            else:
                des=[True,des[0],des[1]]
    else:
        des=dicmovil.get(destino,False)
        if not des:
            print("la ubcicacion fija no se encuentra")
            return
    
    camino=[math.inf,None,None]
    #print("-----",per)
    #print("---",des)

    ##la persona esta en una calle doble mano
    if per[1]:
        if matriz[per[2][0]][des[2][0]][0]+per[2][1]+des[2][1]<camino[0]:
            camino[0]=matriz[per[2][0]][des[2][0]][0]+per[2][1]+des[2][1]
            camino[1]=per[2][0]
            camino[2]=des[2][0]
        if matriz[per[3][0]][des[2][0]][0]+per[3][1]+des[2][1]<camino[0]:
            camino[0]=matriz[per[3][0]][des[2][0]][0]+per[3][1]+des[2][1]
            camino[1]=per[3][0]
            camino[2]=des[2][0]
        if des[0]:
            if matriz[per[2][0]][des[1][0]][0]+per[2][1]+des[1][1]<camino[0]:
                camino[0]=matriz[per[2][0]][des[1][0]][0]+per[2][1]+des[1][1]
                camino[1]=per[2][0]
                camino[2]=des[1][0]
            if matriz[per[3][0]][des[1][0]][0]+per[3][1]+des[1][1]<camino[0]:
                camino[0]=matriz[per[3][0]][des[1][0]][0]+per[3][1]+des[1][1]
                camino[1]=per[3][0]
                camino[2]=des[1][0]
    
    ##la calle de la persona es de una mano
    else:
        if matriz[per[2][0]][des[2][0]][0]+per[2][1]+des[2][1]<camino[0]:
            camino[0]=matriz[per[2][0]][des[2][0]][0]+per[2][1]+des[2][1]
            camino[1]=per[2][0]
            camino[2]=des[2][0]
        if des[0]:
            if matriz[per[2][0]][des[1][0]][0]+per[2][1]+des[1][1]<camino[0]:
                camino[0]=matriz[per[2][0]][des[1][0]][0]+per[2][1]+des[1][1]
                camino[1]=per[2][0]
                camino[2]=des[1][0]

    if camino[1]==None:
        print("no hay camino posible")
        return
    current=camino[1]
    cam=[]
    while current!=camino[2]:
        cam.append(current)
        current=matriz[current][camino[2]][1]
        #print("666",matriz[current][camino[2]][1])
    cam.append(camino[2])
    print("Los autos disponibles son los siguientes:")
    for i in range(0, len(L_cars)):
        if L_cars[i][0] != None:
            print(f"{i+1}) Auto: {L_cars[i][0]}")
            print(f"   Monto: {L_cars[i][2]}")
    print(f"El viaje para llegar a su destino es: {cam}")
    accept = input("Desea aceptar el viaje S/N: ")
    check2 = False
    while check2 != True:
        if accept.upper() == "S" or accept.upper() == "N":
            check2 = True
        else:
            print("La letra ingresada es incorrecta, por favor seleccione S/N")
            accept = input("Desea aceptar el viaje S/N: ")
    if accept.upper() == "S":
        auto = input("Por favor seleccione el numero del auto con el que desea viajar: ")
        try: 
            auto = int(auto)
        except: ValueError
        check = False

        while check != True:
            if auto == 1 or auto == 2 or auto == 3:
                if L_cars[auto - 1][0] != None:
                    check = True
                else:
                    check = False
            if check == False:
                print("El numero ingresado es incorrecto")
                auto = input("Por favor seleccione el auto con el que desea viajar 1/2/3: ")
            try:
                auto = int(auto)
            except: ValueError

        name_auto = L_cars[auto - 1][0]
        print(L_cars[auto - 1][2])
        dicmovil[name_auto][1] =  des[0]
        dicmovil[name_auto][2] =  des[1]
        dicmovil[name_auto][3] =  des[2]
        dicmovil[persona][0] = dicmovil[persona][0] - L_cars[auto - 1][2]
        dicmovil[persona][1] =  des[0]
        dicmovil[persona][2] =  des[1]
        dicmovil[persona][3] =  des[2]
        with open('dic_ubi_movil','wb') as g:
            pickle.dump(dicmovil,g)


def los_autos_más_cercanos(persona,dica,matriz):
    ##print(dica[persona])
    esq1=dica[persona][2][0]
    #print(dica[persona])
    esq2=dica[persona][3][0]
    #print(esq1)
    #print(dica)

    pesoautos=dict()
    for auto in dica:
        ###para asegurarse que sea un auto y no una persona
        if auto[0]=="C":
            
            pesoautos[auto]=math.inf
            ###la calle del auto es doble mano
            if dica[auto][1]:
                if matriz[dica[auto][2][0]][esq1][0]<pesoautos[auto]:
                    pesoautos[auto][0]=matriz[dica[auto][2][0]][esq1][0]+dica[auto][2][1]+dica[persona][2][1]
                    
                if matriz[dica[auto][3][0]][esq1][0]<pesoautos[auto]:
                    pesoautos[auto]=matriz[dica[auto][3][0]][esq1][0]+dica[auto][3][1]+dica[persona][2][1]
                if dica[persona][0]:
                    if matriz[dica[auto][2][0]][esq2][0]<pesoautos[auto]:
                        pesoautos[auto]=matriz[dica[auto][2][0]][esq2][0]+dica[auto][2][1]+dica[persona][3][1]
            
                    if matriz[dica[auto][3][0]][esq2][0]<pesoautos[auto]:
                        pesoautos[auto]=matriz[dica[auto][3][0]][esq2][0]+dica[auto][3][1]+dica[persona][3][1]
                
            else:
                if matriz[dica[auto][2][0]][esq1][0]<pesoautos[auto]:
                    pesoautos[auto]=(matriz[dica[auto][2][0]][esq1][0]+dica[auto][2][1]+dica[persona][2][1])
                if dica[persona][0]:
                    if matriz[dica[auto][2][0]][esq2][0]<pesoautos[auto]:
                        pesoautos[auto]=(matriz[dica[auto][2][0]][esq2][0]+dica[auto][2][1]+dica[persona][3][1])
    L=[[None,math.inf,math.inf],[None,math.inf,math.inf],[None,math.inf,math.inf]]
    for autos in pesoautos:
        costo = (pesoautos[autos]+dica[autos][0])/4
        if (costo)<dica[persona][0]:
            if L[0][1]>pesoautos[autos]:
                L.pop()
                L.insert(0,[autos,pesoautos[autos],costo])
            elif L[1][1]>pesoautos[autos]:
                L.pop()
                L.insert(1,[autos,pesoautos[autos],costo])
            elif L[2][1]>pesoautos[autos]:
                L[2]=[autos,pesoautos[autos],costo]

    return L



(load_movil_element("P10","(e1,4) (e3,3)", 780))
#(e1,e2,11)
(load_movil_element("C8","(e1,7) (e2,4)", 400))
(load_movil_element("C7","(e1,7) (e2,4)", 100))

create_trip("P10","<e6,4> <e7,62>")

