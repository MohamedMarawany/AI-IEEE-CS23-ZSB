n = int(input("Enter Number Of Elements :"))

a = list(map(int,input("Enter List Elements :").strip().split()))[:n]
#print("\nList Is :", a)

a.sort()
#print("\nSoeter List :", a)

target_num = int(input("Enter Target Number :"))

def first_last_apper(target_num):
    b = []
    for i in range(len(a)):
        if a[i] == target_num:
            #print(i)
            b.append(i)

    #print(b)
    print(min(b), max(b))

first_last_apper(target_num)






