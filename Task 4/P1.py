def min_nums(a):
    return min(a)

def max_nums(a):
    return max(a)

def range_nums(a):
    x = max_nums(a) - min_nums(a)
    return x

def Q1_nums(a):
    a.sort()
    first_half = a[:len(a)//2]
    return(Q2_nums(first_half))

       
def Q2_nums(a): #MEDIAN
    a.sort()
    x = len(a)
    if x % 2 == 0:
        med1 = a[x//2]
        med2 = a[(x//2) - 1]
        med = ( med1 + med2 ) //2
    else:
        med = a[x//2]
    
    return med

def Q3_nums(a):
    a.sort()
    second_half = a[len(a)//2:]
    return(Q2_nums(second_half))
    
def IQR_nums(a):
    return Q3_nums(a) - Q1_nums(a)

def Variance_nums(a):

    mean_nums = sum(a) / len(a)
    res = sum((i - mean_nums) ** 2 for i in a) / len(a)

    return res

def STD_nums(a):
    return Variance_nums(a) ** 0.5


if __name__ == "__main__":
    n = int(input("Enter number of elements : "))
    a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
    #a.sort()

    print("Output:")
    print("min :", min_nums(a))
    print("Q1 :", Q1_nums(a))
    print("Q2 :", Q2_nums(a))
    print("Q3 :", Q3_nums(a))
    print("max :", max_nums(a))
    print("range :", range_nums(a))
    print("IQR :", IQR_nums(a))
    print("Variance :", "%.3f"%Variance_nums(a))
    print("Standard deviation :", "%.3f"%STD_nums(a))