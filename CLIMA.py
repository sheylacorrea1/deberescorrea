def ingresar_temperatura():
    while True:
        try:
            temperatura = float(input("Ingrese la temperatura diaria: "))
            return temperatura
        except ValueError:
            print("Por favor, ingrese un número válido.")

def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temperaturas_semanales = []

    for dia in range(1, 8):
        print(f"\nDía {dia}:")
        temperatura = ingresar_temperatura()
        temperaturas_semanales.append(temperatura)

    promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)

    print("\nTemperaturas semanales ingresadas:", temperaturas_semanales)
    print("Promedio semanal del clima:", promedio_semanal)

if __name__ == "__main__":
    main()
