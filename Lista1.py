#Exercícios do Capítulo 2 - Lanna C. e S.

#Exercício 1
'''Manipulação de strings utilizando um nome como base'''

#solicitação do nome
name = input("Insira seu nome completo: ")
name = str(name) #casting

#output
#nome com as letras todas maiúsculas
print(name.upper())
#nome com as letras todas minúsculas
print(name.lower())
#contagem do número de letras no nome
print("Seu nome tem "+str(len(name)-name.count(" "))+ " letras") #desconsiderar espaços
#alteração do último nome para 'do Inatel'
spilt = name.split(" ") #separar a string do nome com base no caracter espaço
print(spilt)
print("Seu novo nome é: "+str(name.replace(spilt[-1], "do Inatel"))) #substtituir a última posição do array para "do Inatel"

#Exercício 2
'''Mostrar a tabuada de um número dado pelo usuário
 em um intervalo também indicado pelo mesmo'''

#solicitar o número para mostrar a tabuada
num = input("Insira o número o qual deseja saber a tabuada: ")

#solicitar o intervalo da tabuada
print("Agora vamos definir o intervalo de cálculo.")
minim = input("Indique o menor número com o qual "+num+" será multiplicado: ")
maxim = input("Indique o maior número com o qual "+num+" será multiplicado: ")

minim = int(minim)#casting
maxim = int(maxim)#casting

#realizando a tabuada com o uso de um loop indo do valor mínimo indicado pelo usuário ao máximo
for i in range(minim, maxim+1):
    print(str(num)+" X "+str(i)+" = "+ str(i*int(num)))


#Exercício 3
'''Verificação do sexo do usuário, exercício para teste de estruturas 
condicionais e laços de repetição'''

invalid = True #variável de controle

#laço de repetição caso a entrada seja inválida (diferente de 'M' ou 'F')
while(invalid):
    gender = str(input("Informe seu gênero (M/F): "))
    if(gender == "M"):
        print("Você é homem!")
        invalid = False #resposta válida
    elif(gender == "F"):
        print("Você é mulher!")
        invalid = False #resposta válida
    else:
        print("Insira uma resposta válida.")

#Exercício 4
'''Cálculo do preço de uma passagem com base na quilometragem seguindo 
as condições: se KM<= 200, preço = 0.5*KM; se não, preço = 0.45*KM'''

#input
#distância percorrida (KM)
dist = float(input("Qual a distância da sua viagem em kilômetros? "))

#lógica condicional e output
if(dist<= 200):
    print(f'O preço de sua passagem é de R${(0.50*dist):.2f}')
else:
    print(f'O preço de sua passagem é de R${(0.45*dist):.2f}')

#Exercício 5
'''Mostar informações para números entre 1000 e 9999, 
os quais possuem milhar, centena, dezena e unidade'''

#ler número entre 1000 e 9999
incorrect = True
#loop condicional para garantir que o número será entre 1000 e 9999
while incorrect:
    #input
    num_1000 = int(input("Insira um número entre 1000 e 9999: "))
    if(num_1000 < 1000 or num_1000 > 9999): #conferência da validade do número
        print("Insira um valor válido.")
    else:
        incorrect = False #número válido
        num_1000 = str(num_1000) #transformar o número para string e pegar as posições correspondentes
        #output
        #número da unidade
        print("O número na posição da unidade é: "+num_1000[3])
        #número da dezena
        print("O número na posição da dezena é: "+num_1000[2])
        #número da centena
        print("O número na posição da centena é: "+num_1000[1])
        #número do milhar
        print("O número na posição do milhar é: "+num_1000[0])

#Exercício 6
'''Cálculos de raiz quadrada, função teto, função chão 
e a parte inteira de um número decimal inserido pelo usuário'''

import math #biblioteca necessária para fazer os cálculos

#loop para não finalizar enquanto o usuário não inserir um dado válido
while errors:
    #try-except para impedir que a inserção de uma string no lugar de um float trave o fluxo do código
    try: 
        #input de um decimal
        num_decimal = float(input("Insira um número decimal: "))
        #output
        #raiz quadrada
        print("A raiz quadrada de "+str(num_decimal)+" é: "+str(math.sqrt(num_decimal)))

        #função teto
        print("A função teto de "+str(num_decimal)+ " é: "+str(math.ceil(num_decimal)))

        #função chão
        print("A função chão de "+str(num_decimal)+ " é: "+str(math.floor(num_decimal)))

        #sua parte inteira
        print("A parte inteira de "+str(num_decimal)+ " é: "+str(math.trunc(num_decimal)))
        errors = False #valor válido, pode finalizar o código

    except(ValueError): #previne crash por inserção de um valor do tipo errado (str ao invés de float)
        print("A entrada deve ser um número.")
