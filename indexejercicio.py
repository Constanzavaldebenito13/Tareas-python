
print("Hola,Bienvenido a To-do list ewe")

intento=4

while intento >0:
    usser=input("Ingrese su nombre")

    if usser== "Ivan":
        print("Usuario correcto")
        break
    else:
        intento = intento - 1
        print(f"Usuario incorrecto vuelva a intentarlo,tienes {intento} intentos")
if intento == 0:
 print("Cantidad de intentos excedida,vuelva mas tarde")

  
edad=int(input("Ingrese su edad"))
if edad>=18:
    print ("Eres mayor de edad")
    print(f"Bienvenido,{usser} Aqui esta tu lista de pendientes")
    pendientes=["lavarplatos","cocinar","ordenar","pasearperro"]
    print(pendientes[0:4])
    choice=input("Elije la tarea por hacer")
    print(pendientes[1])
else:
    print("Eres menor de edad,no puedes ingresar")