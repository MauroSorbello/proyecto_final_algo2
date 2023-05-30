import pickle

prueba = [1, 2, 4]
pickle_file = open('prueba.pickle', 'wb')
pickle.dump(prueba, pickle_file)
pickle_file.close()


pickle_file = open('prueba.pickle', 'rb')
ver = pickle.load(pickle_file)
ver.append(5)
pickle_file.close()

pickle_file = open('prueba.pickle', 'wb')
pickle.dump(ver, pickle_file)
pickle_file.close()

pickle_file = open('prueba.pickle', 'rb')
ver = pickle.load(pickle_file)
print(ver)



