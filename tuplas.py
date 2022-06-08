# TUPLAS
# POR QUE UTILIZARMOS TUPLAS
# SÃO MAIS RÁPIDAS E DEIXAM O CODIGO MAIS SEGURO
# ISSO PORQUE TRABALHAR COMO OS ELEMENTOS IMUTÁVEIS TRAZEM MAIS SEGURANÇA

# SÃO REPRESENTADAS POR PARENTESES, MAS PODEM APARECER SEM OS ()
# SEU DIFERENCIAL É A VIRGULA " , "
# SÃO IMUTÁVEIS
# PORTANTO É IMPOSSIVEL USAR METODOS DE ADIÇÃO E REMOÇÃO



tupla = (1, 2, 3)  # usando parenteses
print(tupla)
print(type(tupla))
del tupla  # limpa a variavel
print("_"*30)  # cria uma linha tracejada

tupla = 1, 2, 3  # sem parenteses
print(tupla)
print(type(tupla))
del tupla
print("_"*30)

# TUPLA COM 1 ELEMENTO
# SE NÃO UTILIZARMOS A VIRGULA DEPOIS DO VALOR ELE ENTEDERÁ COMO INT-- PULO DO GATO ESTÁ AQUI
# SE PASSARMOS SEM A VIRGULA RECONHECERÁ COMO INT.
tupla = (1,)  # tupla com um elemento.
tupla1 = 2,  # utilzando sem ()

print(tupla, "\n", tupla1)
print(type(tupla))
print(type(tupla1))
del tupla
del tupla1
print("_"*30)

# UTILIZANDO O RANGE EM UMA TUPLA
tupla = tuple(range(1, 20, 2))  # de 1 a 20 de 2 em 2
print(tupla)
print(type(tupla))
del tupla
print("_"*30)

# DESEMPACOTAMENTO DE TUPLA
# É NECESSÁRIO QUE AS VARIAVEIS TENHAM A MESMA QTD DE VALORES DA TUPLA , 3 VARS = 3 VALORES
tupla = 'pacote A,', 'pacote B,', 'pacote C,'
pct1, pct2, pct3 = tupla

print(pct1, pct2, pct3)
print(type(tupla))
del tupla
del pct1, pct2, pct3
print("_"*30)

# SOMA DE TODOS OS ELEMENTOS*, VALOR MAX*, VALOR MIN* E TAMANHO
# *SOMENTE INTEIRO OU REAIS, JÁ O TAMANHO ACEITA OUTRO TIPO DE VARIAVEL

tupla = (1, 2, 3,)
print("soma: ", sum(tupla))  # soma todos os valores
print("maior valor: ", max(tupla))  # valor maximo da tupla
print("menor valor:", min(tupla))  # valor minimo da tupla
print("tamanho total:", len(tupla))  # mostra o tamanho da tupla
del tupla
print("_"*30)

# CONCATENAR TUPLAS E SOBRESCREVER UMA TUPLA
tupla = (1, 2, 3,)
tupla1 = (4, 5, 6,)
print("tupla1:", tupla, "\n", "tupla2:", tupla1, "\n")
print("concatenação das tuplas:", tupla + tupla1)  # a concatenação ocorre aqui
tupla = tupla + tupla1  # Aqui sobrescrevemos a tupla
print("tupla sobrescrita:", tupla)
del tupla, tupla1
print("_"*30)

# VERIFICAR SE HÁ UM VALOR CONTIDO NA TUPLA
tupla = 1, 2, 3,
print("contem o valor 10 na tupla?:", 10 in tupla)
print("contem o valor 3 na tupla?:", 3 in tupla)
del tupla
print("_"*30)


#ITERANDO SOBRE UMA TUPLA
print("ITERANDO SOBRE UMA TUPLA")
tupla = (1,2,3,)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print("indice:",indice,"valor:",valor)

del tupla
print("_"*30)

#CONTANDO ELEMENTOS DENTRO DE UMA TUPLA

tupla = ('O doce mais doce que outro doce é o de batata doce').lower() # passamos o lower para contar a primeira letra da frase
print(tupla.count('o'))

frase = tupla
print(frase)
print(frase.count('a'))

del tupla, frase
print("_"*30)


#POR QUE PRECISAMOS DA TUPLA E NÃO DA LISTA?
#PARA QUANDO OS DADOS NÃO PODEREM SEREM MODIFICADOS, CONFORME ABAIXO

tupla = ('JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ',)
# REPARE QUE AQUI DEVE SER UMA TUPLA, POIS NÃO SE PODE COLOCAR NENHUM OUTRO MÊS.

print(tupla[4],": resultado por pesquisa de indice\n") # BUSCANDO UM RESULTADO NA TUPLA PELO INDICE
print(tupla.index('MAI'),": Encontrar o indice especifico dentro de uma tupla com muitos dados \n")
i=0
while i < len(tupla): # USANDO A CONDICIONAL WHILE PARA MOSTRAR OS MESES
    print(tupla[i])
    i = i+1

#SLICING NA TUPLA
#TAMBÉM É PERMITIDO ASSIM COMO NAS LISTAS

print(tupla[0:])

del tupla
print("_"*30)

# COPIANDO UMA TUPLA PARA OUTRA
tupla = 1,2,3,
tupla1 = tupla
tupla2 = 4,5,6,
tupla = tupla1 + tupla2
print(tupla1, tupla)

del tupla
print("_"*30)


