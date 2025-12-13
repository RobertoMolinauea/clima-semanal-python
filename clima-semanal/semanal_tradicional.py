# Promedio semanal de temperaturas - Programación Tradicional
# Autor: Roberto Molina

def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de cada día (7 días):")
    for i in range(1, 8):
        temp = float(input(f"Temperatura del día {i}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(lista):
    return sum(lista) / len(lista)


def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)

    print("\n----- RESULTADO -----")
    print("Temperaturas ingresadas:", temps)
    print("Promedio semanal:", round(promedio, 2), "°C")


main()
