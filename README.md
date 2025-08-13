# Calculadora de Índice de Masa Corporal
Este programa calcula el Índice de Masa Corporal (IMC) de una persona solicitando ciertos datos. Algunas de estas variables son informativas y otras se usan directamente para realizar el cálculo.

La fórmula del IMC es sencilla:

𝐼 𝑀 𝐶 =  Peso (kg) / Estatura (m)2

---

Variables utilizadas
Variables de tipo cadena (str):
1. nombre – Nombre de la persona
2. apPaterno – Apellido paterno
3. apMaterno – Apellido materno

Variables numéricas:
4. edad – Entero (int)
5. peso – Decimal (float)
6. estatura – Decimal (float)

> De estas seis variables, las indispensables para el cálculo son **peso** y **estatura**, ya que permiten determinar la masa corporal de una persona.

---

## Uso de bucles y validacion de cadena
En este programa utilizamos bucles para validar las respuestas del usuario y asegurarnos de que los datos sean correctos antes de continuar, y metodos de validacion de cadenas;


# Bucle usado: "While"
Ejecuta un bloque de código mientras se cumpla una condición. Útil cuando no sabemos cuántas repeticiones serán necesarias.
Función: Repetir la solicitud de datos hasta que el usuario introduzca la información en el formato correcto.

# metodo de cadena (str) isdgit() Validar enteros positivos sin signo.

Ejemplo:
El peso se introduce como un número decimal (float), por ejemplo: 79.6 kg.
La estatura también es un número decimal, por ejemplo: 1.62 m (un metro con 62 cm).

Si el usuario introduce datos inválidos, el bucle se repite hasta que la información cumpla las indicaciones.

## Clasificación del IMC según la OMS
IMC	Clasificación
< 18.5	Bajo peso
18.5 – 24.9	Peso normal
25.0 – 29.9	Sobrepeso
≥ 30.0	Obesidad

### ESTE CÓDIGO ES BÁSICO, le faltan algunas mejoras que con el tiempo se podrían realizar como por ejemplo. evitar que se coloque ceros en la edad, en la estatura evitar por ejemplo si la persona mide un metro con 60 centímetros no dejar que omita el punto decimal para que diga 1.60 y no 160.

## Conclusión – Aprendizaje
En este ejercicio utilicé en Python el paradigma estructurado, organizando el código en scripts con una lógica clara. Aprendí a:

1. Solicitar y almacenar datos en variables.
2. Validar entradas de usuario con bucles while.
3. Realizar cálculos matemáticos simples.
4. Aplicar una fórmula y mostrar resultados con formato adecuado.


