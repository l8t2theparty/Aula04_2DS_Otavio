'''
nome = "Otávio"
peso = 42
altura = 1.63
instrutor = False
idade = 16

# FIXME: Visualizando os tipos de dados
print(type(nome))
print(type(idade))
print(type(peso))
print(type(altura))
print(type(instrutor))

sobrenome = input("Registre o seu sobrenome: ")

print(nome, sobrenome)
print("Classe:", type(sobrenome))

# FIXME Conversão

idade = input("Digite sua idade: ")
idade = int(idade)
print(idade, "| Classe:" , type(idade))

ano = int(input('Qual ano estamos? '))
print(ano, "| Classe:" , type(ano))

#if ano > 2024:
#    pass
#print("Fora do if.")

def somar(numero1, numero2):
    print("Numero 1:" , numero1)
    print("Numero 2:" , numero2)
    addition = numero1 + numero2

    return somar

res = somar(1, 2)
print(res)
'''

# Conversões e inputs vão aqui:
nome = input('Insira o nome: ')
nome = str(nome)

CPF = input('Insira o CPF: ')
CPF = int(CPF)

ano_nasc = input('Insira o ano de nascimento: ')
ano_nasc = int(ano_nasc)

# Vamos imprimir os dados:

print("Olá, meu nome é", nome + ", meu CPF é", CPF, "e nasci no ano", ano_nasc)
print("Classes:")
print("Nome:" , type(nome) , "CPF:" , type(CPF) , "Ano de Nascimento:" , type(ano_nasc))