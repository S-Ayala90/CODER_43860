import json

def introducir_datos():
    usuarios = {}
    usuarios["nombre"] = input("Nombre: ")
    usuarios["password"] = input("Password: ")
    return usuarios


def guardar_datos():
    ...

def cargar_datos():
    ...

def mostrar_datos():
    ...

def main():
    diccionario_de_datos = introducir_datos()
    print(diccionario_de_datos)

main()