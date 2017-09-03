palavra = input()
aux = 0 
vogais = ['a', 'e', 'i', 'o', 'u']
tamanho = len(palavra)
tamanhoVogal = len(vogais)

def verifica(letra):
	for j in range(tamanhoVogal):
		if letra == vogais[j]:
			return True
	return False

for i in range(tamanho):
	if verifica(palavra[i]) == False:
		aux = aux + ord(palavra[i]) - ord('a') + 1
print(aux)
	