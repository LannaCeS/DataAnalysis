#Exercícios do Capítulo 4 - Lanna C. e S.
import numpy as np

#Exercício 1
'''Manipulação de arrays unidimensionais'''

#criação dos arrays
array1 = np.ones(8) #array de 'uns' com 8 elementos
np.random.seed(42) #controle de reprodução de randomização
array2 = np.random.randint(0,10,8) #array de 8 posições com números aleatórios entre 0 e 9

#print(array1)
#print(array2)

#soma de arrays
array3 = array1+array2

#análise do array resultante
#se a soma dos elementos de array3 >= 40
if array3.sum() >= 40:
    #reshape do array para bidimensional, com mais linhas que colunas
    arrayfinal = array3.reshape(4,2)

else:
    #reshape do array para bidimensional, com mais colunas que linhas
    arrayfinal = array3.reshape(2,4)

print("O array resultante é: "+str(arrayfinal))


#Exercício 2
'''Manipulação de arrays unidimensionais com ordenação e concatenação'''

#criação de arrays
array2_1 = np.arange(0,52,2) #números pares entre 0 e 51 (pula de 2 em 2)
#print(array2_1)

array2_2 = np.arange(100,49,-2) # números pares de 100 a 50 (pulo de 2 em 2 regressivo)
#print(array2_2)

#inverter o array2_2 para ficar na ordem crescente para concatenar
array2_flip = np.flip(array2_2)

#output dos arrays concatenados em ordem crescente
print(np.concatenate((array2_1, array2_flip)))


#Exercício 3
'''Mini campo minado'''

#a) array 2x2 de zeros
array3_1 = np.zeros([2,2])
#print(array3_1)

#b) +1 em uma posição aleatória
np.random.seed(42)
array3_1[np.random.randint(0,2,1), np.random.randint(0,2,1)] += 1
#print(array3_1)

#c) input da seleção de uma posição da matriz
print("~~~~ Mini Minefield ~~~~")
print(np.array([['?', '?'], ['?', '?']]))

for i in range (0,3):
    invalid = True #controle de validade da entrada de dados
    stop = False #controle da interrupção do loop for
    while invalid: #controle de validade da entrada do usuário
        print("Choose the "+str(i+1)+"° position that you wish to reveal")
        positionx = int(input("Line: ")) #entrada da linha
        if positionx>=0 and positionx<=2: #verificação do range de entrada da linha
            posistiony = int(input("Row: ")) #entrada da coluna
            if posistiony>=0 and posistiony<=2: #verificação do range de entrada da coluna
                invalid = False #entradas válidas
                if array3_1[positionx, posistiony] == 1:
                    #encontrou a bomba
                    print("Game Over! :( Try Again!")
                    stop = True #interrupção do for, finalização do programa
                elif array3_1[positionx, posistiony] == 2:
                    #a posição já foi revelada anteriormente
                    print("This position was already revealed!")
                    invalid = True #repetição do while para interromper o incremento do for e receber um valor válido
                else:
                    #posição sem mina
                    print("Safe try!")
                    array3_1[positionx, posistiony]+=2 #controle das posições que já foram escolhidas antes (tornam-se 2)
            else:
                print("Choose a value between 0 and 2.") #entrada inválida para a coluna
        else:
            print("Choose a value between 0 and 2.") #entrada inválida para a linha
    if(stop):
        break #interromper o for, pois encontrou a mina

#não encontrando nenhuma mina, i ==2  
if i == 2:
    #Jogo ganho
    print("Congratulations! You beat the game!")


#Exercício 4
'''Análise de matriz'''

#criação da matriz
matrix = np.array([[0,9,8,3], [7,5,6,8], [2,1,5,4]])

shape = matrix.shape
#print(shape)

num_elements = shape[0] * shape[1]

if num_elements %2 == 0: #se o número de elementos for par
    print("Esta matriz poderia se tornar um vetor unidimensional com um número par de elementos.")

else:
    print("Esta matriz poderia se tornar um vetor unidimensional com um número ímpar de elementos.")


#Exercício 5
'''Manipulação de matriz 4x4, com elementos
 random e análise de linhas e colunas'''

#criação da matriz
np.random.seed(10)
matrix_5 = np.random.randint(1,51,[4,4]) #random entre [1,50]

#output
#a) média de cada linha e coluna da matriz
print("As médias de cada linha da matriz, sequencialmente, são: "+ str(matrix_5.mean(axis=1)))
print("As médias de cada coluna da matriz, sequencialmente, são: "+ str(matrix_5.mean(axis=0)))

#b) maior média das linhas e das colunas
print("A maior média das linhas desta matriz é: "+ str(matrix_5.mean(axis=1).max()))
print("A maior média das colunas desta matriz é: "+ str(matrix_5.mean(axis=0).max()))

#c) quantidade de aparições de cada número
unique, counts = np.unique(matrix_5, return_counts = True)
print("Os valores: "+ str(unique)+ " aparecem, respectivamente, "+str(counts)+ " vezes.")

#números que aparecem 2 vezes
print("Números que aparecem 2 vezes na matriz: "+ str(unique[counts == 2]))