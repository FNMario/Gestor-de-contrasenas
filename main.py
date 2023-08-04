import os
from tabulate import tabulate
import questionary
from Conexion import *
import Usuario
import Contrasena

conexion = conectar()
crear_tablas(conexion)


def check_not_empty(answer):
    if len(answer) > 0:
        return True
    else:
        return 'Debe ingresar un valor'


def inicio():
    os.system('clear')
    comprobar = Usuario.comprobar_usuario()
    if len(comprobar) == 0:
        print('Bienvenido, registre su Informacion:')
        nombre = questionary.text('Ingrese su nombre:',
                                  validate=check_not_empty,
                                  qmark='-').ask()
        apellido = questionary.text('Ingrese su apellido:',
                                    validate=check_not_empty, qmark='-').ask()
        contrasena_maestra = questionary.password(
            'Ingrese su contraseña maestra:', qmark='-').ask()
        respuesta = Usuario.registrar(nombre, apellido, contrasena_maestra)
        if respuesta == 'Registro correcto':
            os.system('clear')
            print(f'Bienvenido {nombre}')
            menu()
        else:
            print(respuesta)
    else:
        contrasena_maestra = questionary.password(
            'Ingrese su contraseña maestra:', qmark='-').ask()
        respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
        if len(respuesta) == 0:
            print('Contraseña incorrecta')
        else:
            print('Bienvenido!')
            menu()


def menu():
    while True:
        opciones = ['Añadir contraseña',
                    'Ver todas las contraseñas',
                    'Visualizar una contraseña',
                    'Modificar una contraseña',
                    'Eliminar una contraseña',
                    'Salir']
        opcion = questionary.select("Selecciona una de las siguientes opciones:",
                                    choices=opciones, qmark='-').ask()
        if opcion == 'Añadir contraseña':
            nueva_contrasena()
        elif opcion == 'Ver todas las contraseñas':
            mostrar_contrasenas()
        elif opcion == 'Visualizar una contraseña':
            buscar_contrasena()
        elif opcion == 'Modificar una contraseña':
            modificar_contrasena()
        elif opcion == 'Eliminar una contraseña':
            eliminar_contrasena()
        elif opcion == 'Salir':
            break
        else:
            print('No ingreso una opcion valida')
        questionary.confirm('Volver?').ask()
        os.system('clear')
    print('Hasta pronto!')


def nueva_contrasena():
    nombre = questionary.text('Ingrese el nombre:',
                              validate=check_not_empty, qmark='-').ask()
    url = questionary.text('Ingrese la url:',
                           validate=check_not_empty, qmark='-').ask()
    nombre_usuario = questionary.text('Ingrese el nombre de usuario:',
                                      validate=check_not_empty, qmark='-').ask()
    contrasena = questionary.text('Ingrese la contraseña:',
                                  validate=check_not_empty, qmark='-').ask()
    descripcion = questionary.text('Ingrese la descripcion:', qmark='-').ask()
    respuesta = Contrasena.registrar(
        nombre, url, nombre_usuario, contrasena, descripcion)
    print(respuesta)


def mostrar_contrasenas():
    datos = Contrasena.mostrar()
    nuevos_datos = []
    for dato in datos:
        convertido = list(dato)
        convertido[4] = '********'
        nuevos_datos.append(convertido)
    headers = ['ID', 'NOMBRE', 'URL', 'USUARIO', 'CONTRASEÑA', 'DESCRIPCION']
    tabla = tabulate(nuevos_datos, headers, tablefmt='fancy_grid')
    print('\t\t\tTodas las contraseñas')
    print(tabla)


def buscar_contrasena():
    contrasena_maestra = questionary.password(
        'Ingrese su contraseña maestra:', qmark='-').ask()
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña incorrecta')
    else:
        id = questionary.text('Ingrese el id de la contraseña que desea buscar:',
                              validate=check_not_empty, qmark='-').ask()
        datos = Contrasena.buscar(id)
        headers = ['ID', 'NOMBRE', 'URL',
                   'USUARIO', 'CONTRASEÑA', 'DESCRIPCION']
        tabla = tabulate(datos, headers, tablefmt='fancy_grid')
        print('\t\t\tContraseña')
        print(tabla)


def modificar_contrasena():
    contrasena_maestra = questionary.password('Ingrese su contraseña maestra:',
                                              qmark='-').ask()
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña incorrecta')
    else:
        id = questionary.text('Ingrese el id de la contraseña que desea modificar:',
                              validate=check_not_empty, qmark='-').ask()
        nombre = questionary.text('Ingrese el nuevo nombre:',
                                  validate=check_not_empty, qmark='-').ask()
        url = questionary.text('Ingrese la nueva url:',
                               validate=check_not_empty, qmark='-').ask()
        nombre_usuario = questionary.text('Ingrese el nuevo nombre de usuario:',
                                          validate=check_not_empty, qmark='-').ask()
        contrasena = questionary.text('Ingrese la nueva contraseña:',
                                      validate=check_not_empty, qmark='-').ask()
        descripcion = questionary.text('Ingrese la nueva descripcion:',
                                       qmark='-').ask()
        respuesta = Contrasena.modificar(
            id, nombre, url, nombre_usuario, contrasena, descripcion)
        print(respuesta)


def eliminar_contrasena():
    contrasena_maestra = questionary.password(
        'Ingrese su contraseña maestra: ', qmark='-').ask()
    respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña incorrecta')
    else:
        id = questionary.text('Ingrese el id de la contraseña que desea eliminar: ',
                              validate=check_not_empty, qmark='-').ask()
        respuesta = Contrasena.eliminar(id)
        print(respuesta)


if __name__ == '__main__':
    inicio()
