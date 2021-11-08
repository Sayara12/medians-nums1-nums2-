from random import randint

def medians(nums1,nums2):
    both_nums = nums1 + nums2
    nums_len=len(both_nums)
    if n%2==0:
        med = (both_nums[int(nums_len/2-1)] + both_nums[int(nums_len/2)])/2
    else:
        med = both_nums[int((nums_len+1)/2 - 1)]
    return(med)

n = int(input("Длина первого списка:"))
m = int(input("Длина второго списка:"))
nums1 = [randint(0,10) for i in range(n)]
nums2 = [randint(0,10) for i in range(m)]

print("Среднее значение двух списков:",medians(nums1,nums2))
