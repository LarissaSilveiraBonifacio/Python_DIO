#funcao retorna valor .. metodo nao retorna valor

# def soma(a,b):
#     return a + b
# print ('A soma é: {}' .format(soma(1,2)))
#
# def subtracao (a,b):
#     return a - b
# print ('A soma é: {}' .format(soma(10,2)))
#
# def multiplicacao (a,b):
#     return a * b
# print ('A soma é: {}' .format(soma(10,2)))
#
# def divisao (a,b):
#     return a / b
# print ('A soma é: {}' .format(soma(10,2)))

#Classe
class Calculadora:
    def __init__(self,num1,num2): #sempre vai passar por esse init
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b


    def subtracao (self):
        return self.a - self.b


    def multiplicacao (self):
        return self.a * self.b


    def divisao (self):
        return self.a / self.b

calculadora = Calculadora(10,2)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())

