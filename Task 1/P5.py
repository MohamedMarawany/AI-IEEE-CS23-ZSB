a = input("Enter List Of String : ").split()

print(a)

lst1 = []
lst2 = []

for i in a:

    if (len(i)%2 == 0):
        firstpart, secondpart = i[:(len(i)//2)], i[len(i)//2:]
    else :
        firstpart, secondpart = i[:((len(i)+1)//2)], i[(len(i)+1)//2:]

    lst1.append(firstpart)
    lst2.append(secondpart)

print(lst1,lst2,sep="\n")

