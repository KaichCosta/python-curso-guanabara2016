print('====DESAFIO=4====')
valor=input('escolha algum caractere ou número= ')
print('{} é um número? '.format(valor))
print(valor.isnumeric())
print('É um caractere de alfabeto?',valor.isalpha())
print('É um número? ',valor.isnumeric())
print('É composto apenas por espaços?',valor.isspace())
print('É um número decimal? ',valor.isdecimal()) 
print('É um caractere composto apenas por letras minúsculas?',valor.islower())
print('É um caractere composto apenas por letras maiúsculas? ',valor.isupper())      



#==================================

from random import randint
maquina = randint(0,5)
try: 

#==================================      
    tentativa = int(input('Tente adivinhar o número que estou pensando de 1 a 5 = '))
    print('Tente adivinhar o número que estou pensando de 1 a 5 = ')
    if tentativa==maquina:
        print('Parabéns, você acertou o número')
    else:
        print('Errou! Eu pensei em {}Tente novamente'.format(maquina))
    print('---FIM---') 
except:ValueError 
print('Digite um número inteiro por favor') 

print('Escolha 3 números')
n1=int(input('Número 1 = '))
n2=int(input('Número 2 = '))
n3=int(input('Número 3 = '))
maior= 0
menor= 0
if n2 > n1:
    n2 = maior
else:
    n1 = maior
if n3 > n2: 
    n3 > maior
    n1 = menor
else:
    n1 > n3
    n3 = menor
print('O maior é {} e o menor é {}'.format(maior, menor))
