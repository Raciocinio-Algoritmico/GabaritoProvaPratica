# Escreva um programa para ler 3 valores inteiros e escrever o maior 
# deles. Considere que o usuário não informará valores iguais. (1,0) 

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('Digite um valor: '))

# solução profe
maior = valor1

if maior < valor2:
    maior = valor2

if maior < valor3:
    maior = valor3

print(maior)

#solução alunos

# if valor1 > valor2 and valor1 > valor3:
#     print(valor1)
# elif valor2 > valor1 and valor2 > valor3:
#     print(valor2)
# else:
#     print(valor3)