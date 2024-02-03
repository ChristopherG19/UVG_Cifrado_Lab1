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
                print("\nMenú (Cifrado Caesar - Fuerza Bruta)\n\n1) Encriptar\n2) Desencriptar\n3) Salir")
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
        
    def brute_force(self):
        self.table = PrettyTable()
        word = input("Palabra a desencriptar: ")

        list_e, list_t = self.frecuency(word.lower())
        
        first_e = list(list_e.items())[0]
        first_t = list(list_t.items())[0]
        
        init_index = abs(((self.alpha.index(first_e[0])) - (self.alpha.index(first_t[0]))))
        
        with open("Caesar.txt", "w", encoding="utf-8") as file:
            for x in range(len(self.alpha)):
                res = self.desencriptar(word, init_index)
                line = f"Intento ({x+1}) | Desplazamiento: {init_index % len(self.alpha)}\nResultado: {res}\n"
                init_index += 1
                file.write(line)
        
    def desencriptar(self, word, desp):
        newW = ""
        
        for c in word.lower():
            if c in self.alpha:
                newW += self.alpha[(self.alpha.index(c) - desp % (len(self.alpha)))]
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
