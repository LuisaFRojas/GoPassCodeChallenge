"""
Objetivo: Automatizar tareas básicas de manejo de archivos localmente.
Enunciado:

1. Cree una carpeta llamada `reportes/` si no existe.
2. Dentro de esa carpeta, genere un archivo de texto llamado `reporte_<fecha>.txt`, donde <fecha> esté en
   formato YYYYMMDD.
3. El archivo debe contener:

* La lista de todos los archivos `.txt` que existan en la carpeta actual (donde se ejecuta el script).
* Para cada archivo listado, mostrar su nombre y el número de líneas que contiene.

4. Al final del archivo de reporte, incluir la cantidad total de archivos `.txt` procesados.
   Extra: Si no se encuentra ningún archivo`.txt`, el script debe escribir en el reporte: “No se encontraron
   archivos de texto.”

"""
import datetime
import os

#1 Crear carpeta si la carpeta no existe
carpeta_reporte = 'reportes'
#Uso la library de OS para interactuar con el sistema operativo - Si la carpeta ya existe no arroja error con el uso de 'exist_ok'
os.makedirs(carpeta_reporte,exist_ok=True)

#2 genere un archivo de texto llamado `reporte_<fecha>.txt` con formato YYYYMMDD.
fecha_hoy = (datetime.datetime.now().strftime('%Y%m%d'))
reporte = f'reporte_{fecha_hoy}.txt'
path_reporte = os.path.join(carpeta_reporte, reporte)
#Generar el nombre del reporte con extension txt y crear el path donde se va a guardar el archivo

#3 Generar una lista de todos los archivos `.txt` que existan en la carpeta

lista_archivos = [i for i in os.listdir('reportes') if i.endswith('.txt')]
#Popular la lista basada en la condicion que el archivo sea extension .txt y que el path sea valido

#4 Generar el reporte y escribir el numero total de archivos encontrados
print(lista_archivos)
with open(path_reporte, 'w', encoding='utf-8') as reporte_final:
    # Nos deja sobreescribir el archivo si ya existe
    if lista_archivos:
        reporte_final.write(f'Total de archivos .txt en la carpeta: {len(lista_archivos)}')
    else:
        reporte_final.write('No se encontraron archivos de texto.')
print(f'Encuentra el reporte en:  {path_reporte}')
