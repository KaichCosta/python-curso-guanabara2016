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
print('Escolha 3 valor pra definirmos se pode ser formado um triângulo')
v1=int(input('Valor 1 = '))
v2=int(input('Valor 2 = '))
v3=int(input('Valor 3 = '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')          
