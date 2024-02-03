# Universidad del Valle de Guatemala
# Cifrado de la información
# Laboratorio#1 A

from prettytable import PrettyTable
from itertools import product

class Frecuency():
    def __init__(self):
        self.alpha = "abcdefghijklmnñopqrstuvwxyz"
        self.table = PrettyTable()
        flag = True
        
        while flag:
            try:
                print("\nMenú (Cifrado Vigenere - Fuerza Bruta)\n\n1) Encriptar\n2) Desencriptar\n3) Salir")
                opt = int(input("\nIngrese una opción: "))
                
                if(opt == 1):
                    self.encriptar()
                elif(opt == 2):
                    self.brute_force()
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
        
    def brute_force(self):
        self.table = PrettyTable()
        word = input("Palabra a desencriptar: ")
        x1,x2 = 'áéíóúü','aeiouu'
        proc = word.strip().translate(str.maketrans(x1,x2))
        word_m = proc.lower()
        l_1 = list(word_m)
        l_2 = list(word_m)
        
        kasiski_res = self.check_equal(l_1, l_2)
        
        if(type(kasiski_res) == int):
            # Genera todas las combinaciones de 4 letras con el alfabeto
            combinaciones = [''.join(p) for p in product(self.alpha, repeat=kasiski_res)]

            # Imprime las combinaciones
            with open("Vigenere.txt", "w", encoding="utf-8") as file:
                for key in combinaciones:
                    key2 = (key * (len(proc) // len(key))) + key[:len(proc) % len(key)]
                    res = self.desencriptar(word, key2)
                    if res != "N/A":
                        line = f"Key: {key} | Resultado: {res}\n"
                        file.write(line)
        
    def check_equal(self, l1, l2):
        tot = 0 
        for pos in range(len(l1)):
            equal = 0
            
            l2.pop()
            l2.insert(0, "")
            
            for pos2 in range(len(l1)):    
                if(l1[pos2] == l2[pos2]):
                    equal += 1
            
            if(equal >= tot):
                tot = equal
                
            elif(equal < tot):
                return pos
                        
        return "Error"
        
    def desencriptar(self, word, key2):
        newW = ""
        
        for c, c2 in zip(word.lower(), key2.lower()):
            if c in self.alpha:
                newW += self.alpha[((self.alpha.index(c) - self.alpha.index(c2)) % (len(self.alpha)))]
            else:
                newW += c
        
        return  newW.capitalize()
    
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
        
        porcentaje_column = {}
        porcentaje_t_column = {'a':12.53, 'b':1.42, 'c':4.68, 'd':5.86, 'e':13.68, 
                            'f':0.69, 'g':1.01, 'h':0.70, 'i':6.25, 'j':0.44,
                            'k':0.02, 'l':4.97, 'm':3.15, 'n':6.71, 'ñ':0.31,
                            'o':8.68, 'p':2.51, 'q':0.88, 'r':6.87, 's':7.98,
                            't':4.63, 'u':3.93, 'v':0.90, 'w':0.01, 'x':0.22,
                            'y':0.90, 'z':0.52}
        
        print("Distribución de probabilidades de letras:")
        for letra in self.alpha:
            probabilidad = distribucion_probabilidades[letra]
            porcentaje = probabilidad * 100
            porcentaje_column[letra] = porcentaje

        porcentaje_column = dict(sorted(porcentaje_column.items(), key=lambda item: item[1], reverse=True))
        porcentaje_t_column = dict(sorted(porcentaje_t_column.items(), key=lambda item: item[1], reverse=True))

        letras_ordenadas_A = list(porcentaje_column.keys())
        porcentajes_ordenados = list(porcentaje_column.values())
        self.table.add_column("Letra encontrada", letras_ordenadas_A)
        self.table.add_column("% encontrado", ["{:.2f}%".format(p) for p in porcentajes_ordenados])

        letras_ordenadas_B = list(porcentaje_t_column.keys())
        porcentajes_t_ordenados = list(porcentaje_t_column.values())
        self.table.add_column("Letra (teórica)", letras_ordenadas_B)
        self.table.add_column("% teórico", ["{:.2f}%".format(p) for p in porcentajes_t_ordenados])

        print(self.table)
        
        return porcentaje_column, porcentaje_t_column

F = Frecuency()
