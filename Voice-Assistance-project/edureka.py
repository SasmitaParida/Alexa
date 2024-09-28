def func(a,k):
	print(a)
	print("the value of k is",k)
	for x in a:
		if x==k:
			return 'yes'
		else:
			return 'no'

func([10,20,30,40],70)