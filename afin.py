# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#1 A

import math

class Afin():
    def __init__(self):
        self.alpha = "abcdefghijklmnñopqrstuvwxyz"
        flag = True
        
        while flag:
            try:
                print("\nMenú (Cifrado Afín)\n\n1) Encriptar\n2) Desencriptar\n3) Salir")
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
        x1,x2 = 'áéíóúü','aeiouu'
        proc = word.strip().translate(str.maketrans(x1,x2))
        a = int(input("Ingrese a: "))
        desp = int(input("Desplazamiento: "))
        newW = ""
        
        for c in proc.lower():
            if c in self.alpha:
                newW += self.alpha[((a*(self.alpha.index(c)) + desp) % (len(self.alpha)))]
            else:
                newW += c
        
        print("\nPalabra encriptada:", newW)     
        
    def desencriptar(self):
        word = input("Palabra a desencriptar: ")

        try:
            a = int(input("Ingrese a: "))
            desp = int(input("Desplazamiento: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos.")
            return
        
        if math.gcd(a, len(self.alpha)) != 1:
            print("'a' y la longitud del alfabeto(27) deben ser coprimos.")
            return
        
        newW = ""
        
        for c in word:
            if c in self.alpha:
                newW += self.alpha[((pow(a, -1, len(self.alpha)) * (self.alpha.index(c) - desp)) % len(self.alpha))]
            else:
                newW += c
        
        print("\nPalabra desencriptada:", newW.capitalize())
        
afin = Afin()        
