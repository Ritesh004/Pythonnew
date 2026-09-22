# n=int(input('Enter the number.: '))
# max=0
# smax=0
# i=n
# while i>0:
#     dig=i%10
#     if dig>max:
#         smax=max
#         max=dig
#     elif dig>smax and dig !=max:
#         smax=dig
#     i=i//10
# print('Max value.:',max)
# print('Second max valu.:',smax)

n=int(input('Enter the number.: '))
min=9
smin=8
i=n
while i>0:
    dig=i%10
    if dig<min:
        smin=min
        min=dig
    elif dig<smin and dig !=min:
        smin=dig
    i=i//10
print('Min value.:',min)
print('Second min value.:',smin)

