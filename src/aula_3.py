#Condicionais e operadores logicos

a = int(input('Primeiro bimestre: '))
while a > 10:
   a = int(input('Voce digitou errado! \nPrimeiro bimestre:'))

b = int(input('Segundo bimestre:'))
while b > 10:
   b = int(input('Voce digitou errado! \nSegundo bimestre: '))

c = int(input('Terceiro bimestre: '))
while c > 10:
   c = int(input('Voce digitou errado! \nTerceiro bimestre:'))

d = int(input('Quarto bimestre: '))
while d > 10:
   d = int(input('Voce digitou errado! \nQuarto bimestre:'))

media = (a + b + c + d)/4

print('A media foi: {}'.format(media))



# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('A media foi: {}'.format(media))
# else:
#     print('Revise as notas')



# a = int(input('Digite um valor: '))
# b = int(input('Digite outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b == 0:
#     print('Os numeros são pares: ')
# else:
#     print('Nenhum é par: ')



# a = int(input('Digite um valor: '))
# b = int(input('Digite outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 and resto_b == 0:
#     print('Os numeros são pares: ')
# else:
#     print('Nenhum é par: ')




# a = int(input('Digite um valor: '))
# b = int(input('Digite outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0:
#     print('O numero é par:  {}'.format(a))
# else:
#     print('O numero é impar: {}'.format(a))




#condicional if
# a = int(input('Digite o primeiro  numero: '))
# b = int(input('Digite o segundo numero: '))
# c = int(input('Digite o terceiro  numero: '))
# if a > b and a > c:
#     print('O maior numero é:  {} ' .format(a))
#
# elif b > c and b > c:
#     print('O maior numero é: {}' .format(b))
# else:
#     print('O maior numero é: {}'.format(c))



