
print('====DESAFIO=15====ALUGUEL DE CARROS')
print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
km=int(input('Quantos km seu carro alugado percorreu? = '))
d=int(input('E qual a quantidade de dias pelos quais ele foi alugado'))
tot=60*d+km*0.15
print('Você deverá pagar {:.2f}R$ '.format(tot))