def find_fibonacci(n):
    if n==3 or n==2:
        return 1
    return find_fibonacci(n-1)+find_fibonacci(n-2)

print("5th fibonacci number is ",find_fibonacci(5))
print("10th fibonacci number is ",find_fibonacci(10))