import numpy as np
import math
#Declaramos nuestra lista de caracteres
slave_char  = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
#Declaramos nuestra lista de "codigo"
code        = np.array([33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58])
#Declaramos llave matriz
k_m         = np.array([[2,1,1], [0,1,2], [1,1,2]])

#Creamos el input para el mensaje
message = input('Inserte mensaje a encriptar\n')
#Volvemos en minuscula el mensaje debido a que nuestra lista (slave_char) esta completamente en minuscula
new_message = message.lower()
#Bucle for para guardar los indices en una lista 
array_index  = []
array_charc  = []
list_message = list(new_message)

for i in range(len(new_message)):
    array_index.append(i)
    
#Convertirmos lista a matriz (obtenemos la longitud de la lista)
length  = len(array_index)
row     = math.ceil(length/3)
newA = []
if length < 3*row:
        for i in range(3*row-length):
            array_index.append(43)
            new_matrix = np.asarray(array_index)
else:
            new_matrix = np.asarray(array_index)
    

new_matrix = np.reshape(new_matrix,(row,3))

print (new_matrix)


