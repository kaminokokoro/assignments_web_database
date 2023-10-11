def check_math1(subject):
    if subject[0:3] == "MAT":
        return True
    return False

def check_mat2(subject):
    if "MAT" in subject:
        return True
    return False

def check_math3(subject):
    if subject.find("MAT") != -1:
        return True
    return False    

print("way1:")
print("check MAT101",check_math1("MAT101"))
print("check GEO5012",check_math1("GEO5012"))
print("way2:")
print("check MAT101",check_mat2("MAT101"))
print("check GEO5012",check_mat2("GEO5012"))
print("way3:")
print("check MAT101",check_math3("MAT101"))
print("check GEO5012",check_math3("GEO5012"))