# n1=int(input('Digite um numero'))
# n2=int(input('Digite outro numero'))
# print(n1+n2)

# name=input('Quem é você? ')
# print('Olá, seja bem vindo', name)

# a=input('Digite algo: ')
# print('Tipo: ', type(a))
# print('Só espaços? ', a.isspace())
# print('Numero? ', a.isnumeric())
# print('Alfabetico? ', a.isalpha())
# print('Alfanumerico? ', a.isalnum())
# print('MAIUSCULAS? ', a.isupper())
# print('minusculas? ', a.islower())
# print('Captalizada? ', a.istitle())

# n=int(input('Digite um número: '))
# print('Analisando o valor ', n,', seu antecessor é ', n-1,' e seu sucessor é ', n+1)

# n=int(input('Digite um número: '))
# d=n*2
# print('O dobro de {} vale {}'.format(n, d))
# t=n*3
# print('O triplo de {} vale {}'.format(n, t))
# sq=n**(1/2)
# print('A raiz quadrada de {} vale {}'.format(n, sq))

# n1=int(input('Digite um número: '))
# n2=int(input('Digite outro número: '))
# m=(n1+n2)/2
# print('A média aritimética entre {} e {} é {}'.format(n1,n2,m))

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# c1=float(input('Cateto 1: '))
# c2=float(input('Cateto 2: '))
# h=((c1**2)+(c2**2))**(1/2)
# print('A hipotenusa é ', h)

# nome=str(input('Digite seu nome completo: ')).strip()
# print('Seu nome em maiúsculas é: ',nome.upper())
# print('Seu nome tem ao todo {}'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# print(len(nome.split()[0]))

# nome=str(input('Digite seu nome completo: ')).strip()
# primeiro=nome.split(' ')[0]
# ultimo=nome.split(' ')[len(nome.split(' ')) - 1]
# print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(primeiro, ultimo))

# n=int(input('Digite um número: '))
# if n % 2 == 0:
#     print('o numero {} é par'.format(n))
# else:
#     print('o numero {} é ímpar'.format(n))

import random
print('Suas Opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
itens=('Pedra', 'Papel', 'Tesoura')
n=int(input('Qual a sua Jogada? '))
oponente=random.randint(0, 2)
if n > 2 or n < 0:
    print('Jogada invalida!')
else:
    print(oponente)
    if n == oponente:
        print('Você: {}'.format(itens[n]))
        print('Computador: {}'.format(itens[oponente]))
        print('Empate!')
    else: 
        if n - oponente == 1:
            print('Você: {}'.format(itens[n]))
            print('Computador: {}'.format(itens[oponente]))
            print('Você ganhou!')
        else:
            print('Você: {}'.format(itens[n]))
            print('Computador: {}'.format(itens[oponente]))
            print('Você perdeu!')