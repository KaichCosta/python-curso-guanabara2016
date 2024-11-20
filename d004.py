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
maq = randint (0,10)
print('=='*30)
print('|BEM VINDO AO JOGO DE PAR OU IMPAR|')
print('=='*30)
soma = 0
resp = 'V'
while resp == 'V':
    escolha = (input('Digite ( P ) para PAR E ( I ) para ÍMPAR = ')).upper()
    print(f'VC ESCOLHEU {escolha}')

    if escolha != 'I' != 'P':

        while escolha != 'I' != 'P':
            print('DIGITE UMA ESCOLHA VÁLIDA')
            escolha = (input('Digite ( P ) para PAR E ( I ) para ÍMPAR = ')).upper()
            print(escolha)

    n = int(input('Digite um valor = '))

    valida = maq + n
    if  valida %2 == 0 and escolha == 'P':
        print('GANHOU A || PARTIDA {soma} !!! VAMOS DE NOVO ')
        resp = 'V'
        soma += 1
        
    if valida %2 == 0 and escolha == 'I':
        print('FIM DE JOGO VC PERDEU')
        break

    if valida %2 != 0 and escolha == 'P':
        print('FIM DE JOGO VC PERDEU')
        break

    if valida %2 != 0 and escolha == 'I':
        soma += 1
        print(f'GANHOU A || PARTIDA {soma} !!! VAMOS DE NOVO ')
        resp = 'V'
        
print('=='*30)
if soma >= 1:
    print(f' FIM DE JOGO VC PERDEU !\n MAS GANHOU {soma} VEZES')