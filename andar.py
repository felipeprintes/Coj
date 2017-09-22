a1 = int(input())
a2 = int(input())
a3 = int(input())

t1 = 2*a2+ 4*a3
t2 = 2*a1 + 2*a3
t3 = 4*a1 + 2*a2

if t1<=t2 and t1<=t3:
	menor = t1
elif t2<=t3:
	menor = t2
else:
	menor = t3

print(menor)			
