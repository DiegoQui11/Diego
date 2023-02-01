"Calculara el promedio de 5 numeros "

#El programa calculra el promedio entre 5 numeors

nums = []
print("¿Cuantos numeros ingresara?")
n = int(input())
i=0
while i < n:
    print("valor numero:  ",i+1)
    val = float(input())
    nums.append(val)
    i+=1
prom = sum(nums) / len(nums)
print("El promedio es: ",prom)
