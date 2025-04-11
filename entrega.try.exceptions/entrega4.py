"""
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.
"""
# intento abrir el archivo
try:
    text_File = open ('C:/users/cumpleanos.txt','r+')
except FileNotFoundError as e: 
    print(f"Este archivo no existe, error tipo : {type(e)}")
    f = open ("Text_File", "x")
finally:
    print ("hemos creado un archivo text_File para Ud.")
    print ("Ufa, buenas noches")
