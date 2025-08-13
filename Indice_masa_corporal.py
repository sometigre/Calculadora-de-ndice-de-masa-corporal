# Programa para calcular el indice de masa corporal
# creo que la formula es peso / estatura al cuadrado

# Pedimos los datos a la persona que evaluaremos los siguiente (variables: nombre, apPaterno, apMaterno, edad, peso, estatura)
nombre = input("Escribe su nombre: ")
apPaterno = input("Escribe su apellido paterno: ")
apMaterno = input("Escribe su apellido materno: ")
edad = input("Edad: ")

while not edad.isdigit():
    print("Ingresar solo numeros enteros")
    edad = input("Edad: ")
edad = int(edad)

peso = input("Peso en kilos: ")
while not peso.replace('.', '', 1).isdigit():
    print("Escribe un numero, puedes usar punto para decimales")
    peso = input("Peso en kilos: ")
peso = float(peso)

estatura = input("Estatura en metros (ejemplo: 1.70): ")
while not estatura.replace('.', '', 1).isdigit():
    print("Pon un numero valido")
    estatura = input("Estatura en metros (eejemplo: 1.70): ")
estatura = float(estatura)

imc = peso / (estatura * estatura)

print("===================================")
print("Hola", nombre, apPaterno, apMaterno)
print("Tiene", edad, "años")
print("Su IMC es:", round(imc, 2))

# checar resultado segun la OMS
if imc < 18.5:
    print("Esta bajo de peso")
elif imc >= 18.5 and imc < 25:
    print("Su Peso es normal")
elif imc >= 25 and imc < 30:
    print("Usted esta en Sobrepeso")
else:
    print("Obesidad")
print("===================================")
