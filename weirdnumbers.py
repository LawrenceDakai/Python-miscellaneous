range2to5 = range(2,5)
range6to20 = range(6,20)
range21to100 = range(21,100)

N = 20;

if N % 2 == 0:
	if N in range2to5:
		print 'Not Weird'
	elif N in range6to20:
		print 'Weird'
	elif N == 20:
		print 'Weird'
	else:
		N in range21to100
		print 'Not Weird'
else:
	print 'Weird'
