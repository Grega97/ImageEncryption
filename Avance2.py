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
cd = []
for l in new_message:
    for i in range(len(slave_char)):
        if l == slave_char[i]:
            cd.append(code[i])
            
#Convertirmos lista a matriz (obtenemos la longitud de la lista)
length  = len(cd)
row     = math.ceil(length/3)  

if length < 3*row:
        for i in range(3*row-length):
            cd.append(43)
            new_matrix = np.asarray(cd)
else:
            new_matrix = np.asarray(cd)
            
new_matrix = np.reshape(new_matrix,(row,3))
#Transponemos la matriz
matrix_Tr = new_matrix.T

#multiplicamos la key matrix por la matriz resultante
mult = k_m @ matrix_Tr
#transponemos nuevamente la matriz
new_tr = mult.T
#Obtenemos el modulo de cada uno de los elementos, en este aso 58 es nuestro modulo ya que es el ultimo elemento de nuestro code
modulo = np.mod(new_tr,58)
#convertimos a lista el modulo
new_list = modulo.flatten().tolist()
#recorremos la nueva lista y asignamos las letras correspondientes a las letras
encryption =[]
for l in new_list:
    for i in range(len(code)):
        if l == code[i]:
            encryption.append(slave_char[i]) 

print (encryption)

