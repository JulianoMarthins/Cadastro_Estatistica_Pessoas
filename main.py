# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    name = 'JulianoMarthins'
    print(f'Programador por: "{name}"')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
        Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
    dicionário, e todos os dicionários em uma lista. No final, mostre:

    a) Quantas pessoas foram cadastradas
    b) A média de idade
    c) Uma lista com as mulheres
    d) Uma lista de pessoas com idade acima da média

"""

lista = []# lista que armazenará todos as pessoas cadastradas em dicionários
mulheres = []# Lista para as mulheres cadastradas
acimaMedia = []# Lista para as pessoas acima da média de idade das pessoas cadastradas
contador = soma_idade = 0# contador de pessoas cadastradas e soma das idades

print('-=' * 17)
print('\nCadastre pessoas informando nome, idade e sexo: \n')

while True:
    nome = str(input('Nome: ')).capitalize()

    sexo = str(' ')
    while sexo not in 'FM':# Inserção do sexo e tratamento de possivel erro de digitação
        sexo = str(input('Sexo: [F/M] ')).upper()
        if sexo not in 'FM':
            print('Erro! Por favor, digite apenas M ou F: ')

    idade = ' '
    while int is not idade:# Inserção da idade e tratamento de possivel erro de digitação
        idade = input('Idade: ')
        try:
            idade = int(idade)
            break
        except:
            print('Erro! Por favor, digite apenas números: ')

    cond = str(' ')
    while cond not in 'SN':# Inserção da condição de continuidade e tratamento de possivel erro de digitação
        cond = input('Deseja continuar: [S/N] ').upper()
        if cond not in 'SN':
            print('Erro! Por favor, responsta apenas S ou N: ')

    pessoas = {# Dicionário recebendo os atributos contidos nas variaveis nome, idade e sexo
        'nome' : nome,
        'sexo' : sexo,
        'idade' : idade
    }

    if pessoas['sexo'] == 'F':# Adição das mulheres cadastradas na lista só para mulheres.
        mulheres.append(pessoas['nome'])

    contador += 1# contador de pessoas cadastradas
    soma_idade += idade# soma geral das idades cadastradas

    lista.append(pessoas)
    if cond == 'N':
        break

print()
print('=-' * 17)
print(f'Número de pessoas cadastradas: {contador}')
print(f'Idade média: {soma_idade / contador:.2f}\n')

print('=-' * 17)
print('Nome das mulheres cadastradas: \n')
for x in mulheres:
    print(x)
print()

print('=-' * 17)
print(f'Lista de pessoas que estão acima da média de idade: \n')
for x in lista:
    if x['idade'] > (soma_idade / contador):
        print(f"Nome = {x['nome']}; Sexo = {x['sexo']}; Idade = {x['idade']}")

print('=-' * 17)
print('\nFim de programa')
