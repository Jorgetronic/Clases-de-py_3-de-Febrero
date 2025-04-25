"""
Calcular el promedio de una lista de números usando args y un operador ternario, agrego mensaje de error aca
"""

def promedioLista(*args):
    print (f"promedioLista: {sum(args)/len(args)}" if len(args) > 0 else "Error! No hay suficientes argumentos")
promedioLista(3, 7.7, 3 , 4)