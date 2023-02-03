a = input("Enter List Of String : ").split(',')

print(a)

dict1 = {}

for i in a:
	x,y = i.split(':')
	dict1[x] = y

print(dict1)
