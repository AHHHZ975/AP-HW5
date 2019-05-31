A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), ('1', '2', '3', '4', '5')))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = sorted(A0[i] for i in A0)
A4 = [[i, i*i] for i in A1]

A0 = A0.items()
A5 = []
A5.extend(A0)
A5.extend(A1)
A5.extend(A2)
A5.extend(A3)
A5.extend(A4)
for item in A5:
	print(item)
