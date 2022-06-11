import random
import heapq

def funcionFitness(array):
    # Fitness individual de cada solucion
    fitnessIndividual = []
    for i in array:
        x = i[0]
        y = i[1]
        total = x*x * y - x * y * y
        fitnessIndividual.append(total)

    return fitnessIndividual

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
    #print("Array que se cruzara :", array)
    hijos = []
    n = 0
    if(len(array)%2 == 0):
        for i in range(len(array)):
            if(n < len(array)):
                hijo1 = (array[n][0], array[n+1][1])
                hijo2 = (array[n+1][0], array[n][1])
                hijos.append(hijo1)
                hijos.append(hijo2)
                n += 2
    else:
        for i in range(len(array)):
            if(n < len(array) - 1):
                hijo1 = (array[n][0], array[n+1][1])
                hijo2 = (array[n+1][0], array[n][1])
                hijos.append(hijo1)
                hijos.append(hijo2)
                n += 2
        hijos.append(array[-1])
    hijos_m = mutacion(hijos)
    #print("Hijos finales :", hijos_m)
    return hijos_m

def poblacionInicial(N):
    array = []
    for i in range(N):
        number1 = random.randint(0, 31)
        number2 = random.randint(0, 31)
        array.append([number1, number2])
    return array

def reemplazo(array1,array2):
    arrayf = []
    fitness1 = funcionFitness(array1) 
    fitness2 = funcionFitness(array2) 
    padres = heapq.nlargest(2,fitness1)
    hijos = heapq.nlargest(len(array2) - 2, fitness2)

    #Seleccionar padres
    for i in range(len(padres)):
        valor = padres[i]
        ind = fitness1.index(valor)
        arrayf.append(array1[ind])
    
    #Seleccionar hijos
    for i in range(len(hijos)):
        valor = hijos[i]
        ind = fitness2.index(valor)
        arrayf.append(array2[ind])
    
    return arrayf

def torneo(array):
    fitness = funcionFitness(array)
    ganadores = []

    for i in range(len(fitness)):
        valores = []
        for j in range(3):
            num = random.randint(0,len(fitness)-1)
            valores.append(fitness[num])
        ind = fitness.index(max(valores))
        ganadores.append(array[ind])
    
    #print("Ganadores del torneo : ", ganadores)

    return ganadores

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

def nuevaGeneracion(array):
    pre_seleccion = torneo(array)
    binario = numero_binario(pre_seleccion)
    hijos_b = cruzamiento(binario)
    hijos = binario_numero(hijos_b)
    seleccion = reemplazo(pre_seleccion,hijos)

    return seleccion

def maximizar(array):
    maxi = funcionFitness(array)
    ind = maxi.index(max(maxi))

    return [maxi[0], array[ind]]


pobla_inicial = poblacionInicial(6)
for i in range(0, 100):
    print("Iteracion numero: ", i+1)
    print("Poblacion inicial: ", pobla_inicial)
    # Ejecutamos la funcion nuevaGeneracion
    poblacionNueva = nuevaGeneracion(pobla_inicial)
    print("Poblacion nueva: ", poblacionNueva)
    # Se busca el mejor valor obtenido de la nueva generacion de soluciones.
    [maximo, solucion] = maximizar(poblacionNueva)
    print("Maximo de la funcion :", maximo, "| En los valores :",solucion)
    pobla_inicial = poblacionNueva
    print("---------------------------------------------------------------------")