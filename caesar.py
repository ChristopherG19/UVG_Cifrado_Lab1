# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#1 A

import string

class Caesar():
    def __init__(self):
        self.alpha = "abcdefghijklmnñopqrstuvwxyz"
        flag = True
        
        while flag:
            try:
                print("\nMenú (Cifrado Caesar)\n\n1) Encriptar\n2) Desencriptar\n3) Salir")
                opt = int(input("\nIngrese una opción: "))
                
                if(opt == 1):
                    self.encriptar()
                elif(opt == 2):
                    self.desencriptar()
                elif(opt == 3):
                    flag = False
                    print()
                else:
                    print("La opción ingresada no existe")
                
            except:
                print("Ha ocurrido un error con la opción ingresada")

    def encriptar(self):
        word = input("Palabra a encriptar: ")
        a,b = 'áéíóúü','aeiouu'
        proc = word.strip().translate(str.maketrans(a,b))
        desp = int(input("Desplazamiento: "))
        newW = ""
        
        for c in proc.lower():
            if c in self.alpha:
                newW += self.alpha[(self.alpha.index(c) + desp % (len(self.alpha)))]
            else:
                newW += c
        
        print("\nPalabra encriptada:", newW)
        
    def desencriptar(self):
        word = input("Palabra a desencriptar: ")
        desp = int(input("Desplazamiento: "))
        newW = ""
        
        for c in word.lower():
            if c in self.alpha:
                newW += self.alpha[(self.alpha.index(c) - desp % (len(self.alpha)))]
            else:
                newW += c
        
        print("\nPalabra desencriptada:", newW.capitalize())

caesar = Caesar()
