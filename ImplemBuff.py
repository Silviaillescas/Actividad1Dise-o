def cargar_buffer(entrada, inicio, tamano_buffer):
    """
    Carga un segmento de la entrada en el buffer.
    Si el buffer no se llena completamente y no contiene "eof", se añade "eof" como centinela.
    """
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer and "eof" not in buffer:
        buffer.append("eof")  
    return buffer

def procesar_lexema(lexema):
    """
    Procesa y muestra el lexema si no está vacío.
    """
    if lexema:
        print(f"Lexema procesado: {lexema}")
        return "" 
    return lexema

def procesar_buffer(entrada, tamano_buffer):
    """
    Procesa la entrada en bloques de tamaño `tamano_buffer` y extrae lexemas.
    """
    inicio = 0
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    lexema = ""
    
    while True:
        avance = 0
        
        while avance < len(buffer):
            caracter = buffer[avance]
            
            if caracter == " " or caracter == "eof":
                lexema = procesar_lexema(lexema)
            else:
                lexema += caracter
                
            avance += 1
        
        if "eof" in buffer:
            break  
        
      
        inicio += tamano_buffer
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    
  
    lexema = procesar_lexema(lexema)


txt = "Esto es un ejemplo de entrada con eof"
entrada = list(txt) 
tamano_buffer = 10  

procesar_buffer(entrada, tamano_buffer)