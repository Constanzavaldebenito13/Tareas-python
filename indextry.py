#try

try:
    num1 = float(input("Por favor,ingresa un numero:"))
    num2 = float(input("Por favor,ingrese un numero:"))

    if num2==0:
        raise ZeroDivisionError
    
    resultado = num1 / num2
    print(f"El resultado de esta division es: {resultado}")

except ValueError:
    print("¡Error!Ingresa un nuevo numero")

except ZeroDivisionError:
    print("¡Error!No se puede dividir por cero")