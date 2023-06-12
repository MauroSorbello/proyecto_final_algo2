import pickle

def leer_mapa(archivo):
    file=open(archivo,'r')
    lines=file.readlines()
    
    dic=dict()
    for line in lines:
        for caracter in line:
            if caracter=="}":
                break



    file.close()
    return dic



def leer__mapa(archivo):
    file = open(archivo, 'r')
    dic=dict()
    b=False

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

    file.close()

    with open("file","wb") as f:
        pickle.dump(dic,f)

    print("map created successfully")
    return dic

def leer_esquinas(line):
    l=[]
    for caracter in line:
        if caracter=="\n":
            break
        l.append(caracter)
    return ("".join(l))

