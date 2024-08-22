'''
#Tipos de Concatenação
# Com sinal (+)

num = int(input("Digite: "))


Não possivel concatenar numero inteiro usando esse metodo, a menos que
converta o numero inteiro em uma string


print("Ola, " + str(num) + ". Seja bem-vindo!")
print(type(num))


#CONCATENAÇÃO COM A (,)

print("O numero digitada é: " , num)

#Concatenação com fstring (f)

print(f"O numero digitado é {num} usando a concatenação 'f'")

div = num / 3
# Usando format para formatação numérica
# Limitando a quantidade de casas decimais
print(f'O resultado da divisão é {div:.5f}')
'''

nome = input("Insira seu nome de usuario: ")
email = input("Insira seu e-mail: ")
telefone = input("Insira seu numero de telefone: ")
preco_gas = input("Insira o preço do gas: ")
preco_alcool = input("Insira a o preço do alcool: ")
telefone = input("Insira seu numero de telefone: ")
carro_capacidade = 55 # litros
rota_casa_trabalho = 32 # km
autonomia_gas = 14
autonomia_alc = 12
mes = 20 # segunda-sexta 6 vezes
gas_dia = 2.286
alc_dia = 2.670
km_por_mes = (rota_casa_trabalho * mes) * 2


preço_alcool = 4
# Gasolina tem autonomia de 14km/litro, alcool 12km/litro

gas_km = (autonomia_gas * gas_dia) * 2
alc_km = (autonomia_alc * alc_dia) * 2

gasto_mensal_gas = 1280 / 14
gasto_mensal_alcool = 1280 / 12

gas_mensal = gas_km * mes
alc_mensal = alc_km * mes



print("Nome: " + nome)
print("E-mail: " + email)
print("Telefone : " + telefone)
print("___________________________")
print("Gasto mensal com gasolina: ")
print("Gasto mensal com álcool: ")
print("Média de quilômetros rodados mensalmente:" + km_por_mes + " km")
print("Consumo Gas Mensal: " + gas_dia * 20)
print("Consumo Alcool Mensal: " + alc_dia * 20)