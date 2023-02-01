"Programa que permite calcular la hipotenusa con el teorema de pitagoras"

#Calcular la hipotenuisa

num1=float(input("Ingrese cateto a: ")) #"15.7"
num2=float(input("Ingrese cateto b: "))#"17.6"
hipote=((num1**2)+(num2**2))**(1/2)
print("La medida de la Hipotenusa es: {:.3}".format(hipote))
