import random

def funcionFitness(array):
    # Fitness individual de cada solucion
    fitnessIndividual = []
    for i in array:
        x = i[0]
        y = i[1]
        total = x*x * y - x * y * y
        fitnessIndividual.append(total)
    # Suma de todos los fitness
    sumTotal = 0
    for i in fitnessIndividual:
        sumTotal += i

    return [fitnessIndividual, sumTotal]

def mutacion(array):
    List = [0, 1]
    print()
    array2 = []
    for i in array:
        izq = i[0]
        der = i[1]
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

def cruzamiento(array):
    hijos = []
    for i in array:
        x = i[0]
        y = i[1]
        hijo1 = x[0] + x[1] + y[2] + y[3] + y[4]
        hijo2 = y[0] + y[1] + x[2] + x[3] + x[4]
        hijos.append([hijo1, hijo2])
    return hijos

def poblacionInicial():
    array = []
    for i in range(0, 6):
        number1 = random.randint(0, 31)
        number2 = random.randint(0, 31)
        array.append([number1, number2])
    return array

def reemplazo(array1,array2):
    arrayf = []
    #Seleccionar padres
    arrayf.append(array1[0])
    arrayf.append(array1[1])

    #Seleccionar hijos
    for i in range(len(array2)-3):
        arrayf.append(array2[i])
    
    return arrayf

def torneo(array):
    pass

def calcularProb(array):
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

# Creamos la poblacion inicial
poblacionInicial = poblacionInicial()
print("Poblacion inicial: ", poblacionInicial)
binarios = numero_binario(poblacionInicial)
print("Binarios: ", binarios)
cruce = cruzamiento(binarios)
print("Hijos: ", cruce)

# Transformamos la poblacion inicial a numeros binarios
#print(binarios, "\n")