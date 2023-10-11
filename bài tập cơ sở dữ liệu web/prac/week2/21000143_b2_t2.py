# function to find solution for 2nd degree expression
def solve_2th_degree(a, b, c):
    if a==0 and b==0 and c==0:
        return None
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    if delta == 0:
        return [-b/(2*a)]
    else:
        return sorted([(-b+delta**0.5)/(2*a), (-b-delta**0.5)/(2*a)])
    
# test
print(solve_2th_degree(1, 2, 1))
print(solve_2th_degree(1, 3, 2))
print(solve_2th_degree(1, 2, 3))
print(solve_2th_degree(0, 0, 0))