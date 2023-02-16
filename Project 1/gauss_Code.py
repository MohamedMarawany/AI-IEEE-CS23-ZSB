# function to reduce matrix to reduced
# row echelon form.
def gauss_jordon(a, n):
	i = 0
	j = 0
	k = 0
	c = 0
	flag = 0

	# Performing elementary operations
	for i in range(n):
		# To avoid ZeroDivisionError in Main Diagonal
		if (a[i][i] == 0): 
				
			c = 1
			while ((i + c) < n and a[i + c][i] == 0):
				c += 1
			if ((i + c) == n): 

				flag = 1
				break

			j = i 
			for k in range(1 + n):  # Exchange To Rows To avoid Zero elemnts in main diagonal

				temp = a[j][k]
				a[j][k] = a[j+c][k]
				a[j+c][k] = temp

		for j in range(n):

			# Excluding all i == j
			if (i != j):
				# Converting Matrix to reduced row
				# divide Row to Main diagonal Elements to be 1 
				factor = a[j][i] / a[i][i]

				k = 0
				for k in range(n + 1): # get columns with Zeroes elements Except Main Diagonal
					a[j][k] -= a[i][k] * factor

	return flag

# Function to print the desired result
# if unique solutions exists, otherwise
# prints no solution or infinite solutions
# depending upon the input given.
def PrintResult(a, n, flag):
	
	if (flag == 2):
		print("Infinite number of solutions")
	elif (flag == 3):
		print("No solution")

	# Printing the solution by dividing constants by
	# their respective diagonal elements
	else:
		print("There is one solution: ")
		for i in range(n):
			print(a[i][n] / a[i][i])

# To check whether infinite solutions
# exists or no solution exists 
# To Handle Zero Devision Error (Very Important) for no solution 
def Check_solution(a, n, flag):

	# flag == 2 for infinite solution
	# flag == 3 for No solution
	flag = 3 
	#print("No solution")
	for i in range(n):
		sum = 0
		for j in range(n):
			sum += a[i][j]
		if (sum == a[i][j]):
			flag = 2

	return flag

# Driver code
# input matrix
#a = [[1, 1, 2, 1],  [2, -1, 1, 2],   [4, 1, 5, 4]] # flag 1 => Infinite
a = [[0, 2, 1, 4],  [1, 1, 2, 6],   [2, 1, 1, 7]] #flag 0 => one solution
#a = [[1, 1, 1, 1], [1, 2, 1, 4], [1, 1, 1, 2]] # flag 2 => no solution
# Order of Matrix(n)
n = 3 #Number of equations 
flag = 0


# Performing Matrix transformation
flag = gauss_jordon(a, n)

#print(flag)


if (flag == 1):  # To Handle ZeroDivisionError
	flag = Check_solution(a, n, flag)

"""
# Function to print the matrix
def PrintMatrix(a, n):
    for i in range(n):
        print(*a[i])

#Printing Final Matrix
print("Final Augmented Matrix is : ")
PrintMatrix(a, n)
print()
"""

#print(flag)
# Printing Solutions(if exist)
PrintResult(a, n, flag)


