count=0
for i in range(100,1000):
    s=str(i)
    if int(s[0])+int(s[1])+int(s[2])==20:
        count+=1
print(count)