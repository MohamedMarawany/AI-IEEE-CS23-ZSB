try:
   n = int(input("Enter Number Of Elements :"))
   a = list(map(int,input("Enter List Elements :").strip().split()))[:n]
   #print("\nList Is :", a)
except:
    print("Enter Integer Number !")
    exit()
if len(a)<1:
    print("length must be > 1")
    exit()

a.sort()
#print(a)
largest_Sum=a[-1]
max_Sub=[a[-1]]

minimum_Sum=a[0]
min_Sub=[a[0]]

for i in range(len(a)):
    if(a[i] + largest_Sum > largest_Sum and i != len(a)-1):
        largest_Sum = a[i] + largest_Sum
        max_Sub.append(a[i])
    
    elif(a[i] + minimum_Sum < minimum_Sum and i !=0):
        minimum_Sum = a[i] + minimum_Sum
        min_Sub.append(a[i])
        
if(len(max_Sub) == 1 ):
    max_Sub.append(a[-2])
    largest_Sum = a[-2] + largest_Sum
if(len(min_Sub) == 1 ):
    min_Sub.append(a[1])
    minimum_Sum = a[1] + minimum_Sum

print(max_Sub,"({})".format(largest_Sum))
print(min_Sub,"({})".format(minimum_Sum))
        
