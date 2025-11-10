# Microservicio Factorial – Parcial 2 Arquitectura de Software

## Juan Simón Ospina Martínez
## Universidad EAFIT – 2025-2

### Descripción

Este microservicio recibe un número por la URL y devuelve una respuesta en formato JSON con:

El número recibido

Su factorial

Una etiqueta que indica si el número recibido es par o impar

Fue desarrollado con Python y Flask, aplicando principios de arquitectura basada en microservicios.

### Ejecución del microservicio
1️. Requisitos

Tener Python 3.8 o superior instalado.

Instalar las dependencias con:

pip install -r requirements.txt

2️. Ejecutar el servidor

En la terminal, dentro de la carpeta del proyecto:

python app.py


Si todo va bien, aparecerá algo como:

 * Running on http://127.0.0.1:8000

3️. Probar el servicio

Abre en tu navegador o usa curl:

http://127.0.0.1:8000/factorial/5


Respuesta esperada:

{
  "numero_recibido": 5,
  "factorial": 120,
  "etiqueta": "par"
}

Ó:

{
  "etiqueta": "impar",
  "factorial": 120,
  "numero_recibido": 5
}

## Comunicación con otro servicio (análisis)

Si este microservicio necesitara comunicarse con otro que guarda el historial de cálculos, lo modificaría para que después de generar el resultado, envíe una petición HTTP POST al otro servicio con los datos (numero, factorial, etiqueta).
Ese segundo microservicio se encargaría de almacenar la información en una base de datos externa, manteniendo la independencia entre ambos.
Esto sigue el principio de bajo acoplamiento y permite escalar cada servicio por separado, logrando una arquitectura más ágil y flexible.