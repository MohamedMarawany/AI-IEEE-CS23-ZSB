n = int(input("Enter Number Of Elements : "))
 
a = list(map(int,input("\nEnter The Numbers : ").strip().split()))[:n]
  
print("\nList is ", a)

b = list(set(a))
b.sort()
print("Sorted List : ", b)

seclarge = b[-2]
secsmall = b[1]

print(seclarge)
print(secsmall)
