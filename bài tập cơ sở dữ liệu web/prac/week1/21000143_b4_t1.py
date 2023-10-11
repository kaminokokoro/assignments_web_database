def int_to_str(n):
    s="00"+str(n)
    return s[-3:-1]+s[-1]

print(int_to_str(1))
print(int_to_str(12))
print(int_to_str(123))