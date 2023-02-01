#calcular la nomina de un empleado 

"Calcular el pago de un empleado y el descuento a eps y pension"

nombre = input("Digite el nombre y apellido del empleado: ")
salario = float(input("Digite el salario mensual: "))
diaslaborados=int(input("Digite los dias laborados: "))
totalextras=int(input("Digite la cantidad de horas extras: "))

Valorextras=salario//30//8

totalsalario=salario//30+diaslaborados

totaldevengado=salario+totalextras 

salud=salario*15//100

pension=salario*10//100

sindicato=salario*2//100

totaldeducido=salud*pension*sindicato

print("------------------------------")
print("Nombre: ",nombre)
print("Salario: ",salario)
print("Dias laborados: ",diaslaborados)
print("------------------------------")
print("Salud",salud)
print("Pension",pension)
print("Sindicato",sindicato)
print("------------------------------")
print("Total Salario: ",totalsalario)
print("Horas Extra: ",totalextras)
print("Valor Horas extras: ",Valorextras)
print("------------------------------")
print("Total Devengado: ",totaldevengado)
print("------------------------------")
print("Total Deducido: ",totaldeducido)
print("------------------------------")
print("Neto a Pagar: ")
netoapagar=totaldevengado-totaldeducido
print(" -->",netoapagar)
print("------------------------------")