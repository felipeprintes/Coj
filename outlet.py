n = int(input())
soma = 0
aux = 0
j=0
for i in range(n):
	s = input()
	k = list(map(int,s.split()))
	while j<k[0]:
		j+=1
		soma+=k[j]

print(soma)		
