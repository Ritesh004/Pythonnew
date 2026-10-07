# i=1
# while i<=10:
#     j=1
#     while j<=5:
#         if i%2==1:
#             print("*",end=" ")
#         else:
#             print(1,end=" ")
#         j+=1
#     print()
#     i+=1

# * * * * *
# 1 1 1 1 1
# * * * * *
# 1 1 1 1 1
# * * * * *
# 1 1 1 1 1
# * * * * *
# 1 1 1 1 1
# * * * * *
# 1 1 1 1 1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2==1:
#             print("*",end=" ")
#         else:
#             print(1,end=" ")
#         j+=1
#     print()
#     i+=1

# *
# 1 1
# * * *
# 1 1 1 1
# * * * * *

# i=1
# while i<=10:
#     j=1
#     while j<=5:
#         if j%2==1:
#             print("*",end=" ")
#         else:
#             print(1,end=" ")
#         j+=1
#     print()
#     i+=1

# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *
# * 1 * 1 *

# i=1
# while i<=5:
#     k=1
#     while k<=5-i:
#         print(" ",end=" ")
#         k+=1
#     j=1
#     while j<=i:
#         if i%2==1:
#             print("*",end=" ")
#         else:
#             print(1,end=" ")
#         j+=1
#     print()
#     i+=1

#         *
#       1 1
#     * * *
#   1 1 1 1
# * * * * *

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2==1:
#             if i==1 or i==5 or j==i or j==1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if i==1 or i==5 or j==i or j==1 :
#                 print(1,end=" ")
#             else:
#                 print(" ",end=" ")
#         j+=1
#     print()
#     i+=1

# *
# 1 1
# *   *
# 1     1
# * * * * *

# i=1
# while i<=5:
#     k=1
#     while k<=5-i:
#         print(" ",end=" ")
#         k+=1
#     j=1
#     while j<=i:
#         if i%2==1:
#             if i==1 or i==5 or j==i or j==1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if i==1 or i==5 or j==i or j==1 :
#                 print(1,end=" ")
#             else:
#                 print(" ",end=" ")
#         j+=1
#     print()
#     i+=1

#         *
#       1 1
#     *   *
#   1     1
# * * * * *

# i=1
# while i<=10:
#     j=1
#     while j<=5:
#         if i%2==1:
#             if i==1 or i==10 or j==1 or j==5:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if i==1 or i==10 or j==1  or j==5:
#                 print(1,end=" ")
#             else:
#                 print(" ",end=" ")
#         j+=1
#     print()
#     i+=1

# * * * * *
# 1       1
# *       *
# 1       1
# *       *
# 1       1
# *       *
# 1       1
# *       *
# 1 1 1 1 1

# i=1
# while i<=5:
#     k=1
#     while k<=5-i:
#         print("",end=" ")
#         k+=1
#     j=1
#     while j<=i:
#         if i%2==1:
#             if i==1 or i==5 or j==i or j==1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if i==1 or i==5 or j==i or j==1 :
#                 print(1,end=" ")
#             else:
#                 print(" ",end=" ")
#         j+=1
#     print()
#     i+=1

#     *
#    1 1
#   *   *
#  1     1
# * * * * *


# i = 1
# while i <= 5:
#     k = 1
#     while k <= i:
#         print("", end=" ")
#         k += 1
#     j = 1
#     while j <= 6 - i:
#         if i % 2 == 1:
#             if j == 1 or j == 6 - i or i == 1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         else:
#             if j == 1 or j == 6 - i or i == 1:
#                 print(1, end=" ")
#             else:
#                 print(" ", end=" ")
#         j += 1
#     print()
#     i += 1

#  * * * * *
#   1     1
#    *   *
#     1 1
#      *


i = 1
while i <= 5:
    k = 1
    while k <= 6 - i:
        print("", end=" ")
        k += 1
    j = 1
    while j <= i:
        if i % 2 == 1:
            if j == 1 or i == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j == 1 or i == 1 or j == i:
                print(1, end=" ")
            else:
                print(" ", end=" ")
        j += 1
    print()
    i += 1
l = 1
while l <= 4:
    n = 1
    while n <= l + 1:
        print("", end=" ")
        n += 1
    m = 1
    while m <= 5 - l:
        if l % 2 == 1:
            if m == 5 - l or m == 1:
                print(1, end=" ")
            else:
                print(" ", end=" ")
        else:
            if m == 5 - l or m == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        m += 1
    print()
    l += 1
