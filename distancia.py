soma = 0
dist = 0
nome = 'null'
while nome!='eof':
	nome = input()
	distancia = int(input())
	dist+=distancia
	soma = soma + 1	

media = dist/(soma-1)
print(media)
