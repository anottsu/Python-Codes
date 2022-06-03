# CRIANDO E UTILIZANDO LISTAS
import os
os.system('cls')

lista1 = [1, 2, 6, 6, 6, 3, 4, 9, 5, 15, 65]
lista2 = list('first Rep')
lista3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
lista4 = list(range(10, -1, -1))
lista5 = [0, 1, 'a', 2.365, 'rep']
'''

#LISTA COM IF E ELSE
num = 3
if num in lista1:
    print(f'encontrei o valor {num}')
else:
    print(f'não encontrei o valor {num}')

letra = 'a'
if letra in lista2:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')


# ORDENANDO UMA LISTA COM O SORT()
lista2.sort()
print(lista2)


#CONTANDO O NUMERO DE OCORRENCIAS EM UMA LISTA COM O COUNT()
print(lista1.count(6))
print(lista2.count('o'))


# USANDO O .APPEND()
lista1.append(42)            # ADD UM UNICO ELEMENTO NO FINAL DA FILA
lista1.append([99, 98, 97])  # ADD UMA SUBLISTA AO FINAL DA FILA
print(lista1, "\n")

if [99, 98, 97] in lista1:
    # ELE ENCONTRA TODA SUBLISTA MAS NAO UM VALOR DELA ISOLADO
    print('Encontrei a sublista')
else:
    print('Não encontrei a lista')

if 103 in lista1:
    # ELE NÃO ENCONTRA O VALOR, PQ A SUBLISTA FOI ADD A LISTA PRINCIPAL
    print('encontrei o valor')
else:
    print('Nada encontrado')


# USANDO O .EXTEND()
# ADD CADA ITEM DA SUBLISTA NA LISTA PRINCIPAL MAS AO FINAL DA FILA
lista1.extend([101, 102, 103])
print(lista1, "\n")

lista1.extend(lista2)          # JUNTA AS DUAS LISTAS EM UMA, A LISTA2 ENTRA EM LISTA1
print(lista1, "\n")
# somaListas = lista1 + lista2 # FAZ A MESMA COISA QUE A LINHA ACIMA
# print(lista1,"\n")


# USANDO O .INSERT()
# ADD O NOVO VALOR NA POSIÇÃO 2 DESLOCANDO OS DEMAIS VALORES A DIREITA
lista1.insert(2, 'novoValor')
print(lista1, "\n")


# USANDO O .REVERSE()
# IMPRIME A LISTA DE TRAS PARA FRENTE
lista2.reverse()
print(lista2, "\n")
# print(lista2[::-1])       # FAZ MESMA COISA QUE O REVERSE SO QUE USANDO O SLICE//


# USANDO O .COPY()
# COPIA UMA LISTA PARA UMA OUTRA LISTA
copiaLista = lista1.copy()
print(copiaLista, "\n")


# USANDO O .LEN()
# CONTA A QUANTIDADE DE ITENS DA LISTA
print(len(lista2))


# USANDO O .POP()
# REMOVE O ULTIMO ELEMENTO DA LISTA E RETORNA NO  TERMINAL O ELEMENTO RETIRADO
print(lista2)
lista2.pop()
print(lista2, "\n")
# DA PARA REMOVER O ELEMENTO PELO INDICE, CASO NÃO HOUVER O INDICE INFORMADO, APARECERÁ O ERRO IndexError
lista2.pop(10)
print(lista2, "\n")


# USANDO O .CLEAR()
# USADO PARA LIMPAR UMA LISTA
print(lista3)
lista3.clear()
print(lista3, "\n")


# REPETIR ELEMENTOS DE UMA LISTA
# QUANDO NAO UTILIZAMOS O LIST AQUI ELE INTENDE COMO "INT" SE USAR O LIST SERÁ STRING
nova = [1007]
print(nova)
nova = nova * 5
print(nova, "\n")


#USANDO .SPLIT()
# CONVERTE UMA STRING PARA UMA LISTA.
# PODEMOS PASSAR O TIPO DE DE SEPARADOR PARA ELE IDENTIFICAR = .SPLIT(',') se estiver () ele entende como espaço
frase = 'oi,eu,sou,o,goku'
print(frase)
frase = frase.split(',')
print(frase, "\n")


# USANDO O .JOIN()
# CONVERTENDO UMA LISTA PARA STRING
frase2 = ['maldito', 'kakaroto', 'ele', 'é', 'um', 'gênio']
print(frase2)
# ABAIXO DIZ O COMANDO: PEGUE A FRASE2 COLOQUE espaços ENTRE OS ELEMENTOS E TRANSFORME EM STRING
frase21 = ' '.join(frase2)
print(frase21, "\n")
# ABAIXO DIZ O COMANDO: PEGUE A FRASE2 COLOQUE ponto e virgula ENTRE OS ELEMENTOS E TRANSFORME EM STRING
frase21 = ';'.join(frase2)
print(frase21, "\n")


#------------ ITERANDO EM UMA LISTA ----------------------------

# USANDO FOR PARA INTEIROS
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print("\n",soma)


# USANDO FOR PARA STRINGS
del soma
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print("\n",soma)


# USANDO WHILE
carrinho = []
produto = ''
sair = 'SAIR'

while produto != sair:
    produto = input("Digite o nome do produto ou digite 'SAIR' para sair: \n ").upper()
    if produto != sair:
        carrinho.append(produto)
        os.system("clear")
    
for produto in carrinho:
    print(produto)


# FAZER ACESSO AOS ELEMENTOS DE FORMA INDEXADA
# PODEMOS INSERIR VALORES EM UMA LISTA DIRETAMENTE
cores = [1, 2, 3]
print("\n", cores)
# OU ASSIM
num1 = 1
num2 = 2
num3 = 3
del cores
cores = [num1, num2, num3]
print("\n", cores)


# FAZER ACESSO AOS ELEMENTOS DE FORMA INDEXADA
# indice     0         1           2
cores = ['verde', 'amarelo', 'vermelho']

# se passarmos -1 ele vota para o vermelho se passarmos -4 vai da erro pq o indice vai ate 3
print(cores[-1])
print(cores[-2])
print(cores[-3])
print("\n\n")
# print(cores[-4]) aqui vai dar erro pq o indice vai ate 3
# devemos pensar em um circulo onde o final de um elemento é o inicio do outro
# 2,1,0,-1,-2,-3


# USANDO O FOR PARA INDICES
cores = ['verde', 'amarelo', 'vermelho']
for cor in cores:
    print("\n", cor, "\n")


# USANDO O WHILE PARA INDICES
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


# GERAR INDICE EM UM FOR PARA UMA GRANDE LISTA
for indice, cor in enumerate(cores):
    print(indice, cor)
    # o resultado será:
    # 0 verde
    # 1 amarelo
    # 2 vermelho


# Encontrar um indice de um elemento numa lista
# como localizar um produto em uma lista de 1000 produtos?
# utilizar o índice para buscar o produto é uma opção
# DEVE SER PASSADO O NOME DO PRODUTO QUE VC DESEJA
# CASO NÃO HAJA O VALOR NA LISTA ELE RETORNA O ValueError

lista2.extend(['kyo', 'kusanagy', 'kyo',
              'rin slayer', 'kyo', 'son goku', 'kyo'])
              
print(lista2.index('kyo'))
# CASO HOUVER MAIS DE UM PRODUTO ELE RETORNA O INDICE DO PRIMEIRO ENCONTRADO SOMENTE

# PODEMOS FAZER UMA BUSCA UTILIZANDO UM RANGE,PASSANDO QUAL INDICE ELE DEVE COMEÇAR
print(lista2.index('kyo',16)) # BUSCA 'KYO' A PARTIR DO INDICE 16

#PODEMOS FAZER UMA BUSCA DENTRO DE UM RANGE, INICIO / FIM
print(lista2.index('kyo',1,18)) #PROCURA 'KYO' ENTRE OS INDICES 1 E 18


# SLINCING TANTO PARA LISTA QUANTO PARA RANGES
# LISTA[INICIO : FIM : PASSO]
# RANGE (INICIO : FIM : PASSO)

# SLINCING EM LISTAS, ABAIXO TEMOS A ESTRUTURA USANDO O PARAMETRO 'INICIO'
print(lista1[1:])  # imprime todos os números seguintes, excluindo o indice 1
print(lista1[::])  # pega todos os elementos
                   # lembrar do circulo de elementos ele começará de tras para frente
print(lista1[-3:])


# USANDO SLICING COM PARAMETRO 'FIM'
# pega o indice 0, 1 mas não o 2 ou seja (é lista indice 2- 1)
print("\n\n", lista1[:2])
print(lista1[1:5])  # pega de um inicio a um fim
# lembrar do circulo de elementos ele começara de tras para frente "O ELO"
print(lista1[1:-6])

# USANDO SLICING COM PARAMETRO 'PASSO'
print("\n\n", lista1[::3])  # passa de 2 em 2, lembrar (3-1)
print(lista1[2::-1])        # "ELO"[6,2,1] o resultado
print(lista2[::-1])         # imprime de tras para frente 


# INVERTER VALORES EM UMA LISTA
nomes = ['1-anottsu', '2-haomaru']
print(nomes)

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

print(nomes.reverse())


#COMO REALIZAR SOMA, ENCONTRAR O VALOR MAX, MIN E TAMANHO DE UMA LISTA PARA INT OU FLOAT

lista6 =[1,2,3,4,5,6]
print("\n",sum(lista6))      #SOMA DO ITENS DA LISTA
print(max(lista6))      #MAIOR VALOR DA LISTA
print(min(lista6))      #MENOR VALOR DA LISTA
print(len(lista6))      #TAMANHO DA LISTA

#CONVERTER UMA LISTA EM TUPLA
print("\n\n",lista6)
print(type(lista6)) #LISTAS SAO IMPRESSAS DENTRO DE CHAVES
tupla = tuple(lista6)
print("\n",tupla)   #TUPLAS SAO IMPRESSAS DENTRO DE PARENTESES
print(type(tupla))


#DESEMPACOTAR UMA LISTA
#PEGA A LISTA E DISTRIBUI CADA VALOR EM UM VARIAVEL
#SE HOUVER MAIS VALORES DO QUE VARIAVEIS OU O INVERSO, HAVERÁ ValueError

print("\n\n", lista6)
num1, num2, num3, num4, num5, num6 = lista6
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)


#COPIANDO UMA LISTA PARA OUTRA (SHALLOW COPY E DEEP COPY)
#DEEP COPY - COPIA UMA LISTA PARA OUTRA PODENDO MODIFICAR UMA E MANTER A OUTRA
print("\nDEEPY COPY \n",lista6)

nova = lista6.copy()  #A DICA ESTÁ AQUI, PORQUE FAZEMOS UMA NOVA COPIA
print(nova)

nova.append(4)

print("\n\n")
print(lista6)
print(nova)
print("-"*30) # faz um divisor


#SHALLOW COPY - COPIA UMA LISTA PARA OUTRA ONDE UMA ALTERAÇÃO INFLUENCIA A OUTRA
print("\n\nSHALLOW COPY \n ",lista6)

nova = lista6 # A DICA ESTÁ AQUI, PORQUE RECEBE O VALOR DE LISTA6 E NÃO UMA COPIA COMO A DEEP
print(nova)

nova.append(4)

print("\n\n")
print(lista6)
print(nova)

'''
