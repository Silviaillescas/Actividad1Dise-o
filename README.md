# Simulador de Búfer de Entrada
Este proyecto implementa un pequeño simulador de un búfer de entrada en Python, utilizando un carácter centinela ("eof") para indicar el final de los datos.

## ¿Cómo funciona?
Carga del Búfer:

Se lee la entrada en fragmentos de 10 caracteres y se almacena en un búfer.
Si el fragmento no llena el búfer, se añade "eof" como indicador de final.

## Procesamiento del Búfer:

1. Se utilizan dos punteros (inicio y avance) para recorrer los caracteres.
2. Se extraen los lexemas, es decir, secuencias de caracteres separadas por espacios.
3. Cuando el puntero alcanza el final del búfer, se recargan más datos hasta encontrar "eof".

## Salida esperada:

Se imprime cada lexema procesado en el orden en que aparece en la entrada.
"eof" se maneja correctamente para indicar el final de la lectura.

## Ejemplo de ejecución:
#### Entrada 
Esto es un ejemplo de entrada con eof
#### Salida
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof

 Este proyecto permite simular el procesamiento de un búfer de entrada de manera eficiente, evitando leer la entrada completa en memoria.


