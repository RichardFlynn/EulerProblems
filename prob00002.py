current=1
prev=1
# n=0
# while current<4000000:
#     temp=current
#     current=prev+current
#     prev=temp
#     n+=1
# print(n)
total=0
for i in range(31):
    temp=current
    current=prev+current
    prev=temp
    if current%2==0:
        total+=current
print(total)