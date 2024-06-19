import random

def lanzar_dados(num_dados = 5):
    # Lanza un conjunto de 5 dados y damos valores ramdon de 1 a 6 a cada dado
    return [random.randint(1, 6) for _ in range(num_dados)]

def es_yahtzee(dados):
    # si los dados todos son iguales forman un Yahtzee

    #UTILIZAMOS EL PARAMETRO set PARA DEFINIR SI EN LA LISTA SOLO HAY UN VALOR
    return len(set(dados)) == 1 


def es_fullHouse(dados):

    # Verificamos si se obtiene un Full House (una terna y un par)    
    # Contamos la cantidad de veces que aparece cada valor
    conteo = {valor: dados.count(valor) for valor in set(dados)}
    
    #print("Valores Dados para Fullhouse: ", conteo)
        
    # Verifica si hay exactamente una terna y un par
    valores_conteo = list(conteo.values())

    return 3 in valores_conteo and 2 in valores_conteo



""" ================================ SIMULACIONES ================================ """

# =========================================== SIMULACION YATHZEE =========================================== 

def simulacion_yahtzee(num_simulaciones = 1000000):
    # Simula el lanzamiento de dados un millon de veces y estima la probabilidad que obtengamos un Yathzee (Las mismas caras o valor en todos los dados).

    yahtzees = 0
    for _ in range(num_simulaciones):
        dados = lanzar_dados()

        if _ < 1:
            print("Lanzando Dados")
            
        # IMPRIMIR UNICAMNETE LAS PRIMERAS 10 SIMULACIONES DE LANZAMINETO DE DADOS
        if _ < 10:
            print("Valores obtenidos de dados para el yathzee: ", dados)

        if es_yahtzee(dados):
            yahtzees += 1

    print("Total Yahtzees en la simulación :" , yahtzees )

    probabilidad_yahtzee = yahtzees / num_simulaciones
    return probabilidad_yahtzee 



# =========================================== SIMULACION FULLHOUSE =========================================== 
#  
def simulacion_fullHouse(can_simulaciones = 1000000 ):
    # Simula el lanzamiento de dados un millon de veces y estima la probabilidad de que obtengamos un full house (una terna y un par)


    fullHouses = 0
    for _ in range(can_simulaciones):
        dados = lanzar_dados()

        if _ < 1:
            print("Lanzando Dados")
        # IMPRIMIR UNICAMNETE LAS PRIMERAS 10 SIMULACIONES DE LANZAMINETO DE DADOS
        if _ < 10:
            print("Valores obtenidos de dados para el full house: ", dados)

        #SI FULL HOUSE EXISTE, SUMAR 1
        if es_fullHouse(dados):
            fullHouses += 1
    
    print("Total Fullhouse obtenidos en la simulación:" , fullHouses)
    
    #ESTIMAR LA PROBABILIDAD DEL FULL HOUSE
    probabilidad_fullHouse = fullHouses / can_simulaciones
    return probabilidad_fullHouse

""" ================================ IMPRESIONES ================================ """


# Ejecutar la simulación

# Simualción Jugador 1
print("Turno Jugador Jugador 1")
probabilidad_yahtzeeJ1 = simulacion_yahtzee()
print(f"\nLa probabilidad estimada de obtener un Yahtzee J1 es: {probabilidad_yahtzeeJ1:.6f}\n")

# Simualción Jugador 1
print("Turno Jugador Jugador 2")
probabilidad_yahtzeeJ2 = simulacion_yahtzee()
print(f"\nLa probabilidad estimada de obtener un Yahtzee J2 es de: {probabilidad_yahtzeeJ2:.6f}\n")

# Ejecutar la simulación Jugador 1
print("Turno Jugador Jugador 1")
probabilidad_FullHouseJ1 = simulacion_fullHouse()
print(f"\nLa probabilidad estimada de obtener un Full house J1 es de: {probabilidad_FullHouseJ1:.6f}\n")

# Ejecutar la simulación Jugador 2 
print("Turno Jugador Jugador 2")
probabilidad_FullHouseJ1 = simulacion_fullHouse()
print(f"\nLa probabilidad estimada de obtener un Full house J2 es de: {probabilidad_FullHouseJ1:.6f}\n")


