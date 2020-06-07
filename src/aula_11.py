
lista = [1,10]
try:
     divisao = 10 /1
     numero = lista[1]
     #x = a
except ZeroDivisionError:
     print('Nao é possivel realizar divisao por zero')
except ArithmeticError:
    print('Houve um erro para realizar uma operacao aritmetica')
except IndexError:
    print('Erro ao acessar um indice ivalido da lista')

except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa quando nao ocorre excecao')

finally:
    print('Sempre executa')
