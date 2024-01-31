# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#1 A

from prettytable import PrettyTable

class Frecuency():
    def __init__(self):
        self.alpha = "abcdefghijklmnñopqrstuvwxyz"
        self.table = PrettyTable()
        flag = True
        
        while flag:
            try:
                print("\nMenú (Cifrado con frecuencias)\n\n1) Encriptar\n2) Desencriptar\n3) Salir")
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
        self.frecuency(newW)
        
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
    
    def frecuency(self, texto):
        frec = {}
        total = 0

        for caracter in texto:
            if caracter.isalpha():
                frec[caracter] = frec.get(caracter, 0) + 1
                total += 1

        distribucion_probabilidades = {letra: (frecuencia / total) if total > 0 else 0.0 for letra, frecuencia in frec.items()}

        for letra in self.alpha:
            if letra not in distribucion_probabilidades:
                distribucion_probabilidades[letra] = 0.0
        
        letras_colum = []
        porcentaje_column = []
        porcentaje_t_column = [12.53, 1.42, 4.68, 5.86, 13.68, 
                               0.69, 1.01, 0.70, 6.25, 0.44,
                               0.02, 4.97, 3.15, 6.71, 0.31,
                               8.68, 2.51, 0.88, 6.87, 7.98,
                               4.63, 3.93, 0.90, 0.01, 0.22,
                               0.90, 0.52]
        
        print("Distribución de probabilidades de letras:")
        for letra in self.alpha:
            probabilidad = distribucion_probabilidades[letra]
            porcentaje = probabilidad*100
            letras_colum.append(letra)
            porcentaje_column.append(porcentaje)
            
        # self.table.add_column("Letra", letras_colum)
        # self.table.add_column("Porcentaje encontrado", sorted(porcentaje_column, reverse=True))
        # self.table.add_column("Porcentaje teórico", sorted(porcentaje_t_column, reverse=True))

        self.table.add_column("Letra", letras_colum)
        self.table.add_column("Porcentaje encontrado", porcentaje_column)
        self.table.add_column("Porcentaje teórico", porcentaje_t_column)

        print(self.table)

        return distribucion_probabilidades

F = Frecuency()
