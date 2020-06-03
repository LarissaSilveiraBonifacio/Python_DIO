conjunto1 = {1,2,3,4,5}
conjunto2 = {5,6,7,8}

#uniao dos dois conjuntos
conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

#numero que se repete nos dois
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

#apresenta somente os numeros do conjunto1
conjunto_diferenca1 =  conjunto1.difference(conjunto2)
print('Diferenca entre 1 e 2: {}'.format(conjunto_diferenca1))

#apresenta somente os numeros do conjunto2
conjunto_diferenca2 =  conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

#Tudo o que nao tem nos dois,so tem em um ou em outro
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}'.format(conjunto_diff_simetrica))

#Se o conjunto e um subconjuto do outro conjunto
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5,}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('O conjunto A é um subconjunto de B? {}'.format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('O conjunto B é um subconjunto de A? {}'.format(conjunto_subset))

#Se o conjunto é um super conjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um super conjunto de A? {}'.format(conjunto_subset))

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é um super conjunto de B? {}'.format(conjunto_subset))

#Lista para conjunto
lista = ['cachorro','cachorro','gato','elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
#de volta para lista
lista_animais = list(conjunto_animais)
print(lista_animais)


conjunto = {1,2,3,4,}
print(type(conjunto))
conjunto.add(5) #adicionar elemento
conjunto.discard(5) #remover elemento