def escrever_arquivo(texto):
    arquivo = open('/Users/larissasilveira/PycharmProjects/Python_DIO/teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquvo,texto):
    arquivo = open('notas', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo,'/Users/larissasilveira/PycharmProjects/Python_DIO/')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo,'/Users/larissasilveira/PycharmProjects/Python_DIO/')


if __name__ == '__main__':
    move_arquivo('notas')
    #copia_arquivo('notas')
    #lista_media = media_notas('notas')
    #print(lista_media)
    #media_notas('notas')
    #escrever_arquivo('Primeira linha. \n')
    #aluno = '\nFelipe,7,8,5,6\n'
    #atualizar_arquivo('notas.txt',aluno)
    #ler_arquivo('teste.txt')
