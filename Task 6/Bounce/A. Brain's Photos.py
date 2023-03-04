n, m = map(int, input().split())

pw = True
for i in range(n):
    cores = input().split()
    for cor in cores:
        if cor in ( 'C', 'M', 'Y' ):
            pw = False
 
if pw:
    print("#Black&White")
else:
    print("#Color")

