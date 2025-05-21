"""

Base de datos PostgreSQL
Objetivo: Consultar e insertar datos en una base de datos PostgreSQL.
Enunciado:
1. Crea una tabla llamada `usuarios` con los siguientes campos:

id SERIAL PRIMARY KEY,
nombre VARCHAR(100),
correo VARCHAR(100),
fecha_registro TIMESTAMP DEFAULT NOW()

2. Inserta al menos 3 usuarios con datos ficticios.
3. Escribe una consulta para obtener todos los usuarios registrados en los últimos 7 días.
4. En Python, usando `psycopg2` o `SQLAlchemy`, crea un script que:
- Inserte un nuevo usuario desde variables del código.
- Lea y muestre por consola todos los usuarios en la base de datos.
"""
from itertools import count

import psycopg2

#1 Hacer conexion con la base de datos
conexion = psycopg2.connect(dbname='postgres',user='postgres',password='',host="localhost",port="5432")

try:
    with conexion:
        with conexion.cursor() as selector:
            #crear tabla
            selector.execute(""" 
            CREATE TABLE IF NOT EXISTS usuarios ( id SERIAL PRIMARY KEY, 
                                                nombre VARCHAR(100), 
                                                correo VARCHAR(100),
                                                fecha_registro TIMESTAMP DEFAULT NOW()
                                                );""")

            #Insertar 3 datos
            selector.executemany("""INSERT INTO usuarios (nombre,correo) VALUES (%s,%s);""",
                             [('Pepito perez', 'pepito_perez55@unmail.com'),
                              ('Luisa Rodriguez','luisa_rod95@unmail.com'),
                              ('Michelle Juarez','mich-juarez@unmail.com')])

            #Seleccionar los usuarios registrados en los ultimos 7 dias
            print('Usuarios registrados en los ultimos 7 dias: \n')
            selector.execute("""SELECT id, nombre, correo, fecha_registro FROM usuarios WHERE fecha_registro >= NOW() - INTERVAL '7 days';""")
            usuarios_ultimos_7dias= selector.fetchall()
            for registrado in usuarios_ultimos_7dias:
                print(f"ID: {registrado[0]}, Nombre: {registrado[1]}, Correo: {registrado[2]}, Fecha: {registrado[3]}")

            #Insertar datos desde una variable
            nombre_nuevo_usuario = "Camilo Andrade"
            correo_nuevo_usuario = "andrade-camilo@unmail.com"
            selector.execute("""INSERT INTO usuarios (nombre,correo) VALUES (%s,%s);""",(nombre_nuevo_usuario,correo_nuevo_usuario))

            # Seleccionar todos los usuarios en la base de datos
            print("Todos los usuarios en la base de datos: \n")
            selector.execute("SELECT id, nombre, correo, fecha_registro FROM usuarios;")
            usuarios = selector.fetchall()
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}, Fecha: {usuario[3]}")
finally:
    #Cerrar la conexion a la base de datos al finalizar sin importar que se haya generado algun error.
    conexion.close()