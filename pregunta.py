"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    license_file = open("clusters_report.txt", mode='r')
    license_name = license_file.readlines()
    palabras= license_name[0].lower().split()
    palabras2=license_name[1].lower().split()
    columnas=[palabras[0],palabras[1]+'_'+palabras[2]+'_'+palabras2[0]+'_'+palabras2[1],palabras[3]+'_'+palabras[4]+'_'+palabras2[0]+'_'+palabras2[1],
            palabras[5]+'_'+palabras[6]+'_'+palabras[7]]
    columnas
    def row(inicial,final):
        primero=''
        for i in range(inicial,final):
            primero=primero+license_name[i]
        primero=primero.replace('\n','')
        row_1=primero.split('%')[0].split()
        division=primero.split('%')[1].split()
        claves=''
        for i in division:
            claves+=i+' '
        claves=claves.replace('. ','')
        if claves[len(claves)-1]==' ':
            claves=claves[0:(len(claves)-1)]
        row_1.extend([claves])
        return row_1
    row_1=row(4,9)
    row_2=row(9,14)
    row_3=row(14,19)
    row_4=row(19,24)
    row_5=row(24,29)
    row_6=row(29,34)
    row_7=row(34,39)
    row_8=row(39,44)
    row_9=row(44,49)
    row_10=row(49,54)
    row_11=row(54,57)
    row_12=row(57,62)
    row_13=row(62,67)
    datos=rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13]
    dataframe=pd.DataFrame(datos,columns=columnas)
    # dataframe['porcentaje de palabras clave']=dataframe['porcentaje de palabras clave']+'%'
    dataframe['cluster']=dataframe['cluster'].astype(int)
    dataframe['cantidad_de_palabras_clave']=dataframe['cantidad_de_palabras_clave'].astype(int)
    dataframe['porcentaje_de_palabras_clave']=dataframe['porcentaje_de_palabras_clave'].str.replace(',','.').astype(float)
    return dataframe
