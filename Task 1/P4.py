n = int(input("Enter Number Of Elements : "))

a = list(map(int,input("Enter The Numbers : ").strip().split()))[:n]

m = int(input("Enter Target Number : "))

for i in a:
    for j in a[a.index(i):]:
       if i + j == m:
           print(i,j)
           print(a.index(i),a.index(j))




