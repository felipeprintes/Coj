m = int(input())
s = input()
p = list(map(int,s.split()))
soma = 0
aux = 0
qtd = 0
j = 1
for i in range(m):
	if p[i] == 100:
		continue
	soma += p[i]
	if soma == 100:
		qtd+=1
		soma = 0
	else:
		i+=1	


print(qtd)