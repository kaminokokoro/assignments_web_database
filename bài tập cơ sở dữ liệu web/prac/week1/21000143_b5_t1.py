def find_factorial_resursion(n):
    if n==1:
        return 1
    return n*find_factorial_resursion(n-1)
def find_factorial_loop(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

def find_number_of_digit(n):
    return len(str(n))


print("10!= ",find_factorial_resursion(10))
print("1000!= ",find_factorial_loop(1000))
print("1000! has ",find_number_of_digit(find_factorial_loop(1000))," digits")
