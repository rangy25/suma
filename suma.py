# programa para calcular la suma de un numero n 

#input
n = int(input( " por favor digite el numero n : "))

#processing and output
suma = 0
i = 1
while (i <= n):
    suma = suma+i
    i = i+1
print(" la suma es " + str(suma) )