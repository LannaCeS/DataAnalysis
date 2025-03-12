#Exercícios do Capítulo 3 - Lanna C. e S.

#EXERCÍCIO 1
'''Lista com os 5 primeiros colocados 
de um campeonato de futebol, em ordem'''

#Criação da lista
tabela = ["Barcelona", "Liverpool", "Real Madrid", "Chelsea", "Porto"]

#output
#os 3 primeiros colocados [:3]
print("Os três primeiros colocados são: "+ str(tabela[:3]))

#os últimos 2 colocados [-2:]
print("Os dois últimos colocados são: "+ str(tabela[-2:]))

#lista com times em ordem alfabética
print("Os times, em ordem alfabética, são: "+str(sorted(tabela)))

#posição do Barcelona na tabela (lista original)
print("A posição do Barcelona na tabela é: "+str(tabela.index("Barcelona")+1))


#EXERCÍCIO 2
'''Mostrar informações de duas lojas'''

#Criação dos conjuntos (loja1, loja2)
loja1 = {"Iphone 15", "Iphone 15 pro max", "Iphone 16"} #modelos de smartphone disponíveis
loja2 = {"Galaxy S24", "Galaxy S25", "Iphone 16", "Iphone 15"} #modelos de smartphone disponíveis

#total de opções
print("Indo em ambas as lojas, os modelos disponíveis são: "+ str((loja1 | loja2)))

#modelos disponíveis em ambas as lojas
print("E em ambas as lojas há o(s) modelo(s): "+ str(loja1 & loja2))

#EXERCÍCIO 3
'''Armazenar dados de nome e média de um aluno em um dicionário e gerar a 
situação final do aluno, mostrando ao fim todo o conteúdo do dicionário'''

#input
nome = input("Digite o nome do aluno para registrar a média: ")
media = input("Digite a média do(a) aluno(a) "+nome+": ")

aluno = {'nome':nome, 'media':media}

#análise da nota
if int(aluno['media'])>=50:
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

print("Dados do(a) aluno(a): "+str(aluno))

#EXERCÍCIO 4
'''Análise de peso de três pessoas'''
pessoa1 = {'nome': '', 'peso': ''}
pessoa2 = {'nome': '', 'peso': ''}
pessoa3 = {'nome': '', 'peso': ''}
pessoas = [pessoa1, pessoa2, pessoa3]

#input
#leitura de nome e peso de três pessoas
for i in range (0,3):
    pessoas[i]['nome'] = input("Insira o nome da pessoa: ")
    pessoas[i]['peso']= input("Agora informe seu peso: ")

#output
#pessoa mais pesada
pesos = (float(pessoa1['peso']), float(pessoa2['peso']), float(pessoa3['peso']))
maior = pesos.index(max(pesos))

print("A pessoa mais pesada é: "+str(pessoas[maior]['nome']))

#pessoa mais leve
menor = pesos.index(min(pesos))
print("A pessoa mais leve é: "+str(pessoas[menor]['nome']))



#EXERCÍCIO 5 
'''Análise de um grupo de pessoas'''

#input -> n pessoas
#nome, idade e sexo
pessoas = []
n = 4
for i in range (0,n):
    pessoa = {'nome':'', 'idade':'', 'sexo':''}
    pessoas.append(pessoa)
    pessoas[i]['nome'] = input("Insira o nome da pessoa: ")
    pessoas[i]['idade']= input("Agora informe sua idade: ")
    pessoas[i]['sexo']= input("Agora informe seu sexo (F/M): ")


#output
#média de idade do grupo
#quantas mulheres têm menos de 20 anos
soma_idade = 0
counter = 0
for count in range (0,n):
    soma_idade = soma_idade + int(pessoas[count]['idade'])
    if (int(pessoas[count]['idade'])< 20) and (pessoas[count]['sexo'] == 'F'):
        counter+=1

media = soma_idade/n
print("A média de idade do grupo é de "+str(media)+" anos.")
print("Há "+str(counter)+" mulher(es) menores de 20 anos nesse grupo.")