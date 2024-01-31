# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#1 A

class Vigenere():
    def __init__(self):
        self.alpha = "abcdefghijklmnopqrstuvwxyz"
        flag = True
        
        while flag:
            try:
                print("\nMenú (Cifrado Vigenere)\n\n1) Encriptar\n2) Desencriptar\n3) Salir")
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
        key = input("Ingrese clave: ")
        newW = ""
        key2 = (key * (len(proc) // len(key))) + key[:len(proc) % len(key)]
        
        for c, c2 in zip(proc.lower(), key2.lower()):
            if c in self.alpha:
                newW += self.alpha[((self.alpha.index(c) + self.alpha.index(c2)) % (len(self.alpha)))]
            else:
                newW += c

        print("\nPalabra encriptada:", newW)
        
    def desencriptar(self):
        word = input("Palabra a desencriptar: ")
        key = input("Ingrese clave: ")
        key2 = (key * (len(word) // len(key))) + key[:len(word) % len(key)]
        newW = ""
        
        for c, c2 in zip(word.lower(), key2.lower()):
            if c in self.alpha:
                newW += self.alpha[((self.alpha.index(c) - self.alpha.index(c2)) % (len(self.alpha)))]
            else:
                newW += c
        
        print("\nPalabra desencriptada:", newW.capitalize())
     
vigenere = Vigenere()
