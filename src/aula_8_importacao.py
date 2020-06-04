from aula_7_televisao import  Televisao
from aula_7_calculadora1 import Calculadora
from aula_8_contador_letras import contador_letras

if __name__ == '__main__':
    televisao  = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

calculadora = Calculadora(5,10)
print(calculadora.soma())

lista = ['cachorro','gato','elefante']
total_letraas = contador_letras(lista)
print('O total de letras por palavras da lista: {}'.format(total_letraas))