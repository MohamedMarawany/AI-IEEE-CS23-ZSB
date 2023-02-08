from asyncio import events


n = int(input("Enter Number Of Elements :"))

a = list(map(int,input("Enter List Elements :").strip().split()))[:n]
#print("\nList Is :", a)

even_count = len(list(filter(lambda x: (x%2 == 0), a)))

print(even_count)