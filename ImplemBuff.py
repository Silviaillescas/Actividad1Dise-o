def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer and "eof" not in buffer:
        buffer.append("eof")  # Añadir el carácter centinela si el buffer no se llena completamente
    return buffer

def procesar_buffer(entrada, tamano_buffer):
    inicio = 0
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    lexema = ""
    
    while True:
        avance = 0
        
        while avance < len(buffer):
            if buffer[avance] == " " or buffer[avance] == "eof":
                if lexema:  # Si hay un lexema acumulado, imprimirlo
                    print(f"Lexema procesado: {lexema}")
                    lexema = ""
            else:
                lexema += buffer[avance]
            avance += 1
        
        if "eof" in buffer:
            break  # Salir del bucle al encontrar el centinela
        
        # Avanzar al siguiente segmento del buffer
        inicio += tamano_buffer
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    
    # Imprimir el último lexema si quedó algo en el buffer
    if lexema and lexema != "eof":
        print(f"Lexema procesado: {lexema}")

# Entrada de ejemplo
txt = "Esto es un ejemplo de entrada con eof"
entrada = list(txt)  # Convertir la entrada en una lista de caracteres
tamano_buffer = 10  # Tamaño del búfer definido en el problema

procesar_buffer(entrada, tamano_buffer)
