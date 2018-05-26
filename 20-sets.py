#sets (conjuntos)  -  Set Theory

def main():
	s = set([1, 2, 3])
	t = set([3, 4, 5])

	print('Sets  s = {}   t = {}\n'.format(s, t))

	print ('s.union: {}'.format(s.union(t)))
	print ('s.intersection: {}'.format(s.intersection(t)))
	print ('s.difference: {}'.format(s.difference(t)))

	a = 1 in s
	print ('\n\n\n1 in s:  {}'.format(a))
	a = 1 in t
	print ('1 in t:  {}'.format(a))
	a = 1 not in s
	print('1 not in s:  {}'.format(a))
	a = 1 not in t
	print ('1 not in t:  {}'.format(a))

if __name__ == '__main__':
	main()