# Promedio semanal de temperaturas - Programación Orientada a Objetos
# Autor: Roberto Molina

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_datos(self):
        print("Ingrese las temperaturas de cada día (7 días):")
        for i in range(1, 8):
            temp = float(input(f"Temperatura del día {i}: "))
            self.temperaturas.append(temp)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    semana = ClimaSemanal()
    semana.ingresar_datos()
    promedio = semana.promedio()

    print("\n----- RESULTADO -----")
    print("Temperaturas ingresadas:", semana.temperaturas)
    print("Promedio semanal:", round(promedio, 2), "°C")


main()
