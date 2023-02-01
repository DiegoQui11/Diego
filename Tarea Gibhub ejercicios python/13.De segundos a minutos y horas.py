"El programa calcula los minutos y horas segun la cantidad de segundos"

#Calcular minutos y horas teniendo en cuenta los segundos

segundos=input("Ingrese cantidad de segundos: ") #"3665"
segundos=int(segundos)
horas=segundos//3600 #1
sobrante1=segundos%3600 #65
minutos=sobrante1//60 #1
sobrante2= sobrante1%60 #5
print("Horas")
print(horas)
print("Minutos")
print(minutos)
print("Segundos")
print(sobrante2)
