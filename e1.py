import random

def funcionFitness():
    pass

def mutacion(array):
    # array del tipo = [[01000, 11011], [00100, 11000]]
    List = [0, 1]
    print()
    array2 = []
    for i in array:
        izq = i[0] # 01000
        der = i[1] # 11011
        palabra1 = ''
        for j in izq:
            cambiar = random.choices(List, weights=(99, 1), k=1)
            if (cambiar[0]):
                if (j == '0'):
                    palabra1 += '1'
                else:
                    palabra1 += '0'
            else:
                palabra1 += j
        palabra2 = ''
        for j in der:
            cambiar = random.choices(List, weights=(99, 1), k=1)
            if (cambiar[0]):
                if (j == '0'):
                    palabra2 += '1'
                else:
                    palabra2 += '0'
            else:
                palabra2 += j
        concatenacion = [palabra1, palabra2]
        array2.append(concatenacion)
    return array2

def cruzamiento():
    pass

def poblacionInicial():
    pass

def reemplazo():
    pass

def binario_numero(array):
    array2 = []
    for i in array:
        pos = []
        for j in i:
            number = int(j, 2)
            pos.append(number)
        array2.append(pos)
    return array2

def numero_binario(array):
    array2 = []
    for i in array:
        pos = []
        for j in i:
            binario = format(j, "b")
            largo = len(binario)
            agregar = '0'*(5 - largo)
            final = agregar + binario
            pos.append(final)
        array2.append(pos)
    return array2

inicial = [[2, 5], [24, 0]]
binarios = numero_binario(inicial)
print(binarios)
numeros = binario_numero(binarios)
print(numeros)