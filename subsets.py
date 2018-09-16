'''
Objective:

If user enters 'n'(=4, say), then the following is printed on screen-
{}
{1}, {2}, {3}, {4}
{12}, {13}, {14}, {23}, {24}, {34}
{123}, {124}, {134}, {234}
{1234}

'''

def factorial(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	fct = 1
	for i in range(1, n+1):
		fct = fct * i
	return fct


def C(n,r):
	if r>n or r<0 or n<0:
		return None
	return int(factorial(n) / (factorial(r) * factorial(n-r)))


def subset(n, set_size):
	if set_size == 0:
	 	print('{}')
	 	subset(n, set_size+1)
	if set_size == 1:
		Set = set()
		for i in range(1, n+1):
			Set.add(i)
		print(Set)
		subset(n, set_size+1)

	if set_size == n:
		parent = set()
		for i in range(1,n+1):
			parent.add(i)
		print(parent)
		return

	for i in range(1, C(n,set_size)+1):
		ss = set()
		for j in range(1, set_size+1):
			if j != i:
				ss.add(str(i) + ',' + str(j))
	print(ss)
	subset(n, set_size+1)


def main():
	n = int(input('Enter element count: '))
	subset(n, 0)

main()