# check password
def check_password():    
    inp=input("please type your password: ")
    if len(inp)<8:
        print("password is too short")
        return False
    count_digit=0
    is_lower=False
    special_char=False
    for i in inp:
        if i.isdigit():
            count_digit+=1
        if i.islower():
            is_lower=True
        if i in "!@#$%^&*()_":
            special_char=True
    if count_digit<2:
        print("password must contain at least 2 digits")
        return False
    if not is_lower:
        print("password must contain at least 1 lowercase letter")
        return False
    if not special_char:
        print("password must contain at least 1 special character")
        return False
    return True


# loop until user enters a valid password
while not check_password():
    pass        
        