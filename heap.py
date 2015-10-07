from random import randint

def push_heap(lista,val):
	lista.append(val)
	n = len(lista)
	while n!=1:
		if lista[n-1] < lista[n/2-1] :
			val = lista[n-1]
			lista[n-1] = lista[n/2-1]
			lista[n/2-1] = val
		if n%2 == 1 and lista[n-2] < lista[n/2-1] :
			val = lista[n-2]
			lista[n-2] = lista[n/2-1]
			lista[n/2-1] = val
		n = n/2

l = []
for n in range(2,50):
	push_heap(l,randint(1,100))

print l

def pop_heap(lista):
	top = lista[0]
	n = len(lista)
	lista[0] = lista[n-1]
	del lista[n-1]
	n -= 1
	
	i = 1
	while i <= n/2:
		val = lista[i-1]
		if 2*i < n:
			if lista[2*i-1] < lista[2*i]:
				if lista[2*i-1] < lista[i-1]:
					lista[i-1] = lista[2*i-1]
					lista[2*i-1] = val
					i = 2*i
				else:
					return top
			else:
				if lista[2*i] < lista[i-1]:
					lista[i-1] = lista[2*i]
					lista[2*i] = val
					i = 2*i+1
				else:
					return top
		else:
			if lista[2*i-1] < lista[i-1]:
				lista[i-1] = lista[2*i-1]
				lista[2*i-1] = val
				i = 2*i
			else:
				return top
	return top

