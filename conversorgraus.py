import os

def linha():
    print("=" * 30)

def converter_temperatura():
    print("Conversor de temperatura")
    linha()
    opc = input("Escolha a unidade de temperatura entre Celsius, Fahrenheit e Kelvin: ").strip().lower()

    if opc == "celsius":
        temperaturac = float(input("Insira a temperatura em Celsius: "))
        fahrenheit = (temperaturac * 9/5) + 32
        kelvin = temperaturac + 273.15
        print(f"{temperaturac:.2f}°C = {fahrenheit:.2f}°F")
        print(f"{temperaturac:.2f}°C = {kelvin:.2f}K")

    elif opc == "fahrenheit":
        temperaturaf = float(input("Insira a temperatura em Fahrenheit: "))
        celsius = (temperaturaf - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temperaturaf:.2f}°F = {celsius:.2f}°C")
        print(f"{temperaturaf:.2f}°F = {kelvin:.2f}K")

    elif opc == "kelvin":
        temperaturak = float(input("Insira a temperatura em Kelvin: "))
        celsius = temperaturak - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temperaturak:.2f}K = {celsius:.2f}°C")
        print(f"{temperaturak:.2f}K = {fahrenheit:.2f}°F")

    else:
        print("Opção inválida. Tente novamente.")
    linha()

# Loop principal
while True:
    converter_temperatura()
    continuar = input("Deseja converter outra temperatura? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        input("Saindo...")
        break
