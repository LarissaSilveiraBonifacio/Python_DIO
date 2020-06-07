class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        self.message = message

while True:
    try:
        x = int(input('Entre com um numero de Zero a Dez: '))
        print(x)
        if x > 10:
            raise InputError('Nao pode ser maior que 10')
        elif x < 0 :
            raise InputError('Nao pode ser menor que Zero')
        break
    except ValueError:
        print('Valor invalido.Deve se digitar apenas numeros')
    except InputError as ex:
        print(ex)