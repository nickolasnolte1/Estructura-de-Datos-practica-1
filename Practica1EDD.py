import cProfile

def sumatoria(numero):
    if(numero == 0):
        return numero
    else:
        return (numero * (numero + 1) / 2)
    
number = int(input("Escriba un número entero positivo: "))

valortotal = sumatoria(number)

print("La sumatoria de los números naturales del 1 al {0} es: {1}".format(number, valortotal))


cProfile.run ('sumatoria(5)') 
