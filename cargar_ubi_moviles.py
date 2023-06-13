import pickle
import cargar_ubi_fijas

def load_movil_element(nombre,direccion,monto):
    direc = cargar_ubi_fijas.direccion_lista(direccion)
    print(direc)
    if nombre != None and (nombre[0] == 'P' or nombre[0] == "C"):
        direc=cargar_ubi_fijas.check_direccion(direc,monto)
       #Cargamos el archivo
        with open("dic_ubi_movil","rb") as f:
            dic_movil = pickle.load(f)
        ###Agregamos al diccionario el objeto movil
        dic_movil[nombre] = direc
        print(dic_movil)
        with open("dic_ubi_movil","wb") as f:
            pickle.dump(dic_movil,f)
    else:
        print("nombre erroneo")
        return False
    
(load_movil_element("P10","(e1,4) (e3,3)", 780))
#(e1,e2,11)
(load_movil_element("P8","(e1,7) (e2,4)", 780))
(load_movil_element("C8","(e1,7) (e2,4)", 780))


"""
#Creamos el archivo
pickle_file = open('prueba.pickle', 'wb')
pickle.dump(prueba, pickle_file)
pickle_file.close()

#Abrimos el archivo modo lectura
pickle_file = open('prueba.pickle', 'rb')
#Trabajamos con la estructura en otra variable
ver = pickle.load(pickle_file)
ver.append(5)
pickle_file.close()

#Reescribimos el archivo
pickle_file = open('prueba.pickle', 'wb')
pickle.dump(ver, pickle_file)
pickle_file.close()
"""