n = int(input("Enter Number Of Elements : ")) 

a = list(map(int,input("Enter The Numbers : ").strip().split()))[:n]

b = a[::-1]

if( a==b ):
    print("List is Symmetric")
else:
    print("List is Not Symmetric")