import math
import cmath
print('====DESAFIO=16====')
num=int(input('escreva um numero pra extrair a raiz = '))
raiz=math.sqrt(num)
print('caso a raiz não for exata, será mostrado o valor arredondado')
print('a raiz de [{}] é igual a [{}]'.format(num, math.floor(raiz)))

print('====DESAFIO=17====')
catop=int(input('Informe o cateto oposto = '))
catad=int(input('Informe o cateto adjacente = '))
op=catop**2
ad=catad**2
hipquad=op+ad
hip=hipquad**(1/2)
print('a soma dos catetos ao quadrado é igual a hipotenusa ao quadrado que faria com que n/ {} oposto mais {} adjacente gere uma hipotenusa de {:.2f}'.format(catop, catad, hip))


print('====DESAFIO=18====')
n=int(input('Qual número deverá ser mostrado o sen, cos, tan? = '))
cos=cmath.cos(n)
sen=cmath.sin(n)
tan=cmath.tan(n)
print('O número escolhido foi[{:.2f}] que possui o Seno=[{:.2f}] \n Cosseno[{:.2f}] \n Tangente[{:.2f}]'.format(n, sen, cos, tan))






