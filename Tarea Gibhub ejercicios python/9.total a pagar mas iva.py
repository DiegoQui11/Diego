"total a pagar de productos mas el iva"

#programa calcula la cantidad que se debe pagar por los productos mas el iva 

print("Cantidad de productos: ")
prods = int(input())
i = 0
sub = 0
while i<prods:
    print("Producto ",i+1,  "valor: ")
    val = int(input())
    print("Cantidad")
    cant = int(input())
    subpro = val*cant
    sub=sub+subpro
    i+=1

iva = sub * 0.19
total = sub + iva
print("Se vendieron: ",prods,"Productos")
print("subtotal: ",sub)
print("Iva 19% ",iva)
print("Total: ",total)
