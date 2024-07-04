nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums):
    n = len(nums)
    last = nums[n-1]
    for i in range(n-1,0,-1):
        nums[i]=nums[i-1]
    nums[0] = last
    return nums

for i in range(k):
    nums=rotate(nums)

print(nums)