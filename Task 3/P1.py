def mean_val(a):
    sum_a = sum(a)
    avg = sum_a/len(a)

    return avg

def median_val(a):
    a.sort()
    x = len(a)
    if x % 2 == 0:
        med1 = a[x//2]
        med2 = a[(x//2) - 1]
        med = ( med1 + med2 ) //2
    else:
        med = a[x//2]
    
    return med


def mode_val(a):
    #a.sort()
    return max(a, key=a.count)


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter number of elements : "))
            a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
            print("Mean: %0.3f"%(mean_val(a)))
            print("Median:",(median_val(a)))
            print("Mode:",(mode_val(a))) 
            break
        except ValueError:
            print("Enter Numbers only!!") # if Enter a Letter in the List
        except (ZeroDivisionError,RuntimeError,TypeError):
            print("Array Can not be Empty !!") # Enter Number of Elements = 0 and Elments = 0 To check it

    
 