# DESAFIO 1

celsius = input("Qual a temperatura em Celsius? (C°) ")
celsius = int(celsius)

kelvin = celsius + 273.15

farenheit = (celsius/5 * 9 + 32)

print(f'Celsius: {celsius:.2f} °C')
print(f'Kelvin: {kelvin:.2f} °K')
print(f'Farenheit: {farenheit:.2f} °F')

# DESAFIO 2

real = input('Insira a quantia em real: ')
real = int(real)
dolar = real*5.48
print(f'Em dolares, seu valor é ${dolar:.2f}')


# DESAFIO 3
metro = input('Valor metro da distância: ')
metro = int(metro)
cm = metro * 100
mm = metro * 1000
km = metro / 1000
print(f'Distância em centimetro seria {cm} cm, em milimetros seria {mm} mm, e em kilometros seria {km} km')