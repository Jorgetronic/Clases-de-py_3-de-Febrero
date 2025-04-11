""""
Escribe un programa que intente acceder a una clave que no existe en un diccionario.
Si se produce una excepción KeyError, captura la excepción y muestra
"""
dicqueyaexiste = {
    "Nombre":"Jorge",
    "Apellido":"Colombo",
    "DNI":"1234567"
}
try:
    print(dicqueyaexiste["Edad"]) 
except KeyError as e: 
    print(f"Esta clave no existe, error tipo : {type(e)}")


