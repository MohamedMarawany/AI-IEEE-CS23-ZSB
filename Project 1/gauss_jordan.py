def gauss_jordan(a,b):
    n = len(b)
    if len(a[0]) > n :
        return 2
    flag = 3
    for k in range(n) :
        # Replace the row in which the pivot element is with zero
        if round(a[k][k]) == 0 :
            for i in range(k+1,n) :
                if abs(a[i][k]) > a[k][k] :
                    for j in range (k,n) :
                        temp = a[k][j]
                        a[k][j] = a[i][j]
                        a[i][j] = temp 

                    temp = b[k]
                    b[k] = b[i]
                    b[i] = temp
                    break
        # Convert the pivot elements to one to get the unity matrix

        pivot = a[k][k]
        # handle divide by zero and check if infinte solution
        if pivot == 0 :
            #for i in range(n) :  
                 #if a[k][i] == 0 :
            flag = 1
                    

        else :
            for j in range(k,n) :
              a[k][j] /= pivot
            b[k] /= pivot

         # Apply Gauss Jordan Elimination
        for i in range(n) :
            # Skip Elements Already Equal to 0 And Skip Pivot Element
            if i == k or a[i][k] == 0 : continue
            factor = a[i][k]
            for j in range(k,n):
                a[i][j] -= factor * a[k][j]
            b[i] -= factor * b[k]
    # check if one solution
    if a[-1][-1] == 1 :
        flag = 3
    #check if infinte solution
    elif a[-1][-1] == b[-1]: 
        flag = 2

    return flag

# no solution
#a  = [[3,2],[6,4]]
#b = [5,8]
#a = [[1,1,-1],[2,3,-1],[3,4,-2]]
#b = [2,0,1]
#a = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
#b = [1,4,2]
#a = [[1, 2, 3], [4, -1, 2], [2, -5, -4]]
#b = [2,5,13]
# infinite solution
#a = [[1, 1, 2],  [2, -1, 1],   [4, 1, 5]] 
#b = [1, 2, 4]
#a = [[-6,4],[3,-2]]
#b = [2,-1]
#a = [[2,4],[1,2]]
#b = [8,4]
#a = [[1, 1, 2],  [2, -1, 1],   [4, 1, 5]]
#b = [1,2,4]
#one solution
a = [[0, 2, 1],  [1, 1, 2],   [2, 1, 1]]
b = [4, 6, 7]
#a = [[1,3],[3,4]]
#b = [7,11]
#a = [[-1, 2],[3,-4]]
#b = [-6, 14]
#a = [[0,2,0,1,5,9,8,6,1],[2,2,3,2,6,8,2,5,9],[4,-3,0,1,6,1,3,5,4],[6,1,-6,-5,4,1,4,3,7],[6,1,-6,-5,1,6,6,8,2],[6,1,-6,-5,9,4,5,4,1],[6,1,-6,-5,5,3,2,6,8],[6,1,-6,-5,-4,9,4,2,5],[6,1,-6,-5,7,4,9,7,3]]
#b = [0,-2,-7,6,9,2,4,6,8]
#a = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
#b = [1,4,2]

flag =  gauss_jordan(a,b)
#print(a,b)
if flag == 1 :
    print("Ther no solution")
elif flag == 2 :
    print("Inifinte solution")
else :
    print("one solution")
    #print(a,"\n",b)
    print(*b, sep = "\n")

