# -*- coding: utf-8 -*-
#Maquina Enigma by Jose Ramon Martínez

def rotor(letra, numero, reverse=False):

   I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
   II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
   III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

   #    IV = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]
   #   V = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]

   tipo = [I, II, III]

   if reverse == False:
       return tipo[numero - 1][(letra) % 26]
   else:
       return tipo[numero - 1].index((letra) % 26) #con index pasamos la posicion

    #list(range) genera una lista del estilo cambios='0','1','2'...
def enigma(input, numerosnumerosrotores, posicionesclavijas, stickers=list(range(26))):

   #como Q=16, E=4, V=21, J=9, Z=25
   girorotor = [16, 4, 21, 9,25]

   #TRANSFORMACION DE la CADENA INPUT
   lista = list(input)  # Convertimos el input que es texto en una lista de caracteres. En plan, Hola como 'H','o','l','a'

   listacif = []  # Inicializamos la lista de letras cifradas

    #traducimos lo que nos pasa como parametro que ya hemos transformado en una lista y lo transformamos en numeros, 
    #con ord hay que restarle 65 porq A=65, B=66
   for letra in lista

    letras = [ord(letra) - 65 ]
   
   #Vamos a la traduccion de cada letra de input
   for letra in letras:
       #comprobamos que no este cambiado los stickers
       letra = stickers[letra]

       posicionesclavijas[2] = (posicionesclavijas[2] + 1) % 26

       if posicionesclavijas[2] == girorotor[numerosrotores[2] - 1] + 1:  #el del medio
           posicionesclavijas[1] = (posicionesclavijas[1] + 1) % 26

       if posicionesclavijas[1] == girorotor[numerosnumerosrotores[1] - 1]:  #el de la izquierda
           posicionesclavijas[0] = (posicionesclavijas[0] + 1) % 26
           posicionesclavijas[
               1] += 1  #El doble paso


       rotor1 = rotor((letra + posicionesclavijas[2]) % 26, numerosnumerosrotores[
           2])

       rotor2 = rotor((rotor1 - (posicionesclavijas[2] - posicionesclavijas[1])) % 26, numerosrotores[1])

       rotor3 = rotor(rotor2 - (posicionesclavijas[1] - posicionesclavijas[0]) % 26, numerosrotores[0])

       # Ahora vamos con la reflexión.
       R = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

       reflejado = R[rotor3 - posicionesclavijas[0]]

       rotor3 = rotor(reflejado + posicionesclavijas[0], numerosrotores[0], True)

       rotor2 = rotor(rotor3 + (posicionesclavijas[1] - posicionesclavijas[0]) % 26, numerosrotores[1], True)

       rotor1 = (rotor(rotor2 + (posicionesclavijas[2] - posicionesclavijas[1]) % 26, numerosrotores[2], True) - posiciones[2]) % 26


       #el intercambiador letra = cambios[rotor1]

       listacif.append(letra)




   listafin = [chr(letra + 65) for letra in listacif]

   listafin = ''.join(listafin)

   return listafin


#Pasamos lo que queremos traducir, la posicion de los rotores, la posicion de las clavijas y los stickers
print(
   enigma('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
          [1, 2, 3], [0, 0, 25],
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))



