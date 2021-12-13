# -*- coding: utf-8 -*-

from patrimonio import *

################################################################
#  Funciones de test
################################################################
def test_calcula_paises(registros):
    pass
    
def test_bienes_por_tipo(registros):
    pass
    
def test_dibuja_bienes_por_tipo(registros):
    pass

def test_pais_mas_bienes(registros):
    pass
    
def test_bienes_mas_recientes_por_pais(registros):
    pass
       
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    
    # Ejercicio 1
    # Lectura del fichero csv y se obtiene la lista de tuplas (registros)
    registros = lee_bienes('./data/whs.csv')
    
    # Mostrar el número total de bienes (filas recuperadas)
    print("Número total de bienes:", len(registros)) 
    # Mostrar las 5 primera filas de la lista
    print(registros[:5], '\n')
    
    # Prueba del ejercicio 2
    test_calcula_paises(registros)
    # Prueba del ejercicio 3
    test_bienes_por_tipo(registros)
    # Prueba del ejercicio 4
    test_dibuja_bienes_por_tipo(registros)
    # Prueba del ejercicio 5
    test_pais_mas_bienes(registros)
    # Prueba del ejercicio 6
    test_bienes_mas_recientes_por_pais(registros)
