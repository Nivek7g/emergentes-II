print("hola mundo desde python")
#variables numericas
edad = 25 #entero
altura = 1.75 #flotante
bandera = False #booleano
nombre ="Bruno Diaz" #string
print("print tradicional")
print("-----------------------------")
print("mi nombre es:",nombre)
print("mi edad es:",edad)
print("mi altura es:",altura)
print("estoy vivo",bandera,"\n")
#segunda forma de imprimir
print("print moderno")
print("-----------------------------")
print(f"mi nombre es:{nombre}")#cadenas formateadas
print(f"mi edad es: {edad}")
print(f"mi altura es: {altura}")
print(f"esty vivo: {bandera}")
#entrada de datos
print("\nEntrada de datos")
print("------------------")
nombre = input("ingesa tu nombre ")
edad = int(input("ingresa tu edad"))
altura = float(input("ingresa tu altura"))
bandera = input("estas vivo? (true/false: )")

print(f"mi nombre es:{nombre}")#cadenas formateadas
print(f"mi edad es: {edad}")
print(f"mi altura es: {altura}")
print(f"esty vivo: {bandera}")
