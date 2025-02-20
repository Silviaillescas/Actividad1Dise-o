# 🚀 Simulador de Búfer de Entrada

Este proyecto implementa un simulador de búfer de entrada en Python, utilizando un carácter centinela (`"eof"`) para indicar el final de los datos. El simulador procesa la entrada en fragmentos (buffers) y extrae lexemas (secuencias de caracteres separadas por espacios) de manera eficiente.

---

# Link del video:
```
https://youtu.be/EehAV1vUIm4?si=xBXDKFkLpXKuSALf
```

## 🛠️ ¿Cómo funciona?

### 1. **Carga del Búfer**
- La entrada se divide en fragmentos de **10 caracteres** (tamaño del búfer).
- Si el fragmento no llena completamente el búfer, se añade el carácter centinela `"eof"` para indicar el final de los datos.

### 2. **Procesamiento del Búfer**
- Se utilizan dos punteros:
  - **Inicio**: Indica la posición inicial del búfer actual.
  - **Avance**: Recorre los caracteres dentro del búfer.
- Se extraen lexemas (secuencias de caracteres sin espacios).
- Cuando se alcanza el final del búfer, se carga un nuevo fragmento de datos hasta encontrar `"eof"`.

---

## 🧩 Ejemplo de Ejecución

### Entrada
```
Esto es un ejemplo de entrada con eof
```

### Salida Esperada
```
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof
```

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:
```
Actividad1Dise-o/
├── ImplemBuff.py   # Código principal del simulador de búfer
├── README.md      # Documentación del proyecto
```

---

## 🚀 ¿Cómo ejecutarlo?

1. Clona el repositorio o descarga el archivo `simulador.py`.
2. Ejecuta el siguiente comando en tu terminal:
   ```bash
   python ImplemBuff.py
   ```


### **Salida Esperada**
- Cada lexema procesado se imprime en el orden en que aparece en la entrada.
- El carácter `"eof"` se maneja correctamente para indicar el final de la lectura.

```
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof
```
