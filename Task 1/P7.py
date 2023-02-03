n = int(input("Enter Number Of Elements : "))

a = list(map(int,input("Enter The Numbers : ").strip().split()))[:n]
k = int(input("Enter Rotate Number : "))
print("Orgin List IS :", a)

# Rotating Right

a = a[-k:] + a[:-k]
print("After Rotating Right :", a)

#####################

# Rotating Left

a = a[k:] + a[:k]
print("After Rotating Left :", a)



