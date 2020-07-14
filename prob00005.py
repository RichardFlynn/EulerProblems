from functools import reduce
m=20
factors=[]
nums=set([1])
for i in range(1,m+1):
    if i not in nums:
        for j in range(1,i):
            if i%(i-j)==0:
                factors.append(i/(i-j))
                for k in nums:
                    if (i/(i-j))*k<=m:
                        nums=nums.union(set([(i/(i-j))*k]))
                break
#             for k in nums:
#                 if i*k<=m:
#                     nums=nums.union(set([i*k]))
#     for j in range(1,i):
#         if i%(i-j)==0:
#             factors.append(i/(i-j))
#             break
    #factors.append(i)
print(factors)
print(reduce(lambda x,y:x*y,factors))
print(nums)