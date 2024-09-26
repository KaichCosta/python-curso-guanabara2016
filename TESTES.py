print('=*45')
print('BEM VINDO AO BANCO DE FINANCIAMENTO DE CASAS')
print('=*45')

v=int(input('Qual o valor da casa que você quer comprar? = '))
s=int(input('Qual o seu salário? = '))
t=int(input('Quanto anos você quer pagar pelo empréstimo? = '))

meses= t / 12
prest= v / meses
trinta= s * 0.3

if prest <= trinta:
    print('SEU EMPRÉSTIMO PODE SER REALIZADO')
    print('VOCÊ DEVE PAGAR {} POR MÊS AO BANCO'.format(prest))
else: 
    print('SEU EMPRÉSTIMO NÃO PODE SER REALIZADO')
