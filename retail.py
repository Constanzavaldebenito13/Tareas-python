
rut_verificado=21440705
codigo_verificado=1
intento_rut=3
intento_codigo=3
monto=0
descuento=0
total_pagar=0

print("Hola,Bienvenido a Falabella")

while intento_rut > 0: 
    rut=int(input("Ingresa rut sin puntos ni guion y sin el codigo verificador"))

    if rut==rut_verificado:
      codigo=int(input("Ingrese el codigo verificador de su rut"))
      break
    else:
     intento_rut=intento_rut-1
     print(f"Ingrese un rut valido,le quedan {intento_rut} intentos")

if intento_rut ==0:
  print("Intentos superados,vuelva mas tarde")

if codigo==codigo_verificado:
      nombre=input("Ingrese su nombre")

monto=int(input("Ingrese su monto: "))
if monto <= 10000 :
  total_pagar = monto
  print("No tiene descuento")
elif monto >= 10001 and monto <= 50000:
  descuento = monto*0.1
  total_pagar=monto-descuento
  print("Tiene un descuento del 10%")
elif monto > 50000:
 descuento=monto*0.2
 total_pagar=monto-descuento
 print("Tiene un descuento del 20%")

print("------BOLETA------")
print(f"Hola,{nombre}")
print(f"Su rut es {rut}-{codigo_verificado}")
print(f"Su monto es de {monto}")
print(f"Su descuento es de un {descuento}")
print(f"El total a pagar es de {total_pagar}")






    