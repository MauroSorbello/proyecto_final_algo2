import pickle


prueba = [1, 2, 4]
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

#Vemos el archivo
pickle_file = open('prueba.pickle', 'rb')
ver = pickle.load(pickle_file)
print(ver)



