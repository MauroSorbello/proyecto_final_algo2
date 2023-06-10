import pickle
import math


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

def leer__mapa(archivo):
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

        if char=="(":
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
            while char!=")":
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

    print("map created successfully")
    return dic

def leer_esquinas(line):
    l=[]
    for caracter in line:
        if caracter=="\n":
            break
        l.append(caracter)
    return ("".join(l))

grafo1 = leer__mapa("Grafo_de_prueba.txt")

