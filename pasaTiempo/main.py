import io


ruta_archivo_entrada = 'archivo_entrada.txt'
ruta_archivo_salida = 'archivo_salida'

def obtener_contenido(ruta_archivo):
    result = None
    with open(ruta_archivo, 'r') as archivo:
        result = archivo.readlines()
    return result

def limpiar_informacion(contenido):
    contenido = list(map(lambda linea: linea.replace('\n',''), contenido))
    quitar_lineas_vacias = list(filter(lambda linea: linea != '', contenido))
    return quitar_lineas_vacias

def generar_formato(contenido):
    resultado = list()
    for indice in range(len(contenido)):
        if (indice + 1) % 3 == 0:
            resultado.append('{0}\t{1}\t{2}\n'.format(contenido[indice - 2], contenido[indice - 1], contenido[indice]))

    return resultado

def generar_archivo(contenido):
    with open('{0}.txt'.format(ruta_archivo_salida), 'w') as archivo:
        archivo.writelines(contenido)
        archivo.close()

def transformar_archivo():
    contenido = obtener_contenido(ruta_archivo_entrada)
    contenido = limpiar_informacion(contenido)
    contenido_formateado = generar_formato(contenido)
    generar_archivo(contenido_formateado)
    # print(contenido_formateado)
    pass

if __name__ == "__main__":
    transformar_archivo()