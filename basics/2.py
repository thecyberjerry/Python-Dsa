# import math
#
# n = 101010
#
# digits = math.log(n,10) + 1
# digits = math.floor(digits)
# print(digits)
import math

# Output = 6
#
# n = 101010
# arr = []
# while n > 0:
#     arr.append(n % 10)
#     n = math.floor(n / 10)
# for _ in arr:
#     print(_, end=" ")
# Output = 6

# ========================================

# n = 100100
#
# arr = []
# while n > 0:
#     arr.append(n % 10)
#     n = math.floor(n / 10)
#
# flag = False
# for i in arr:
#     if i == 0 and arr[i + 1] == 0:
#         pass
#     else:
#         print(i, end="")

# n = 123450000 <----------
# r = 0
# while n > 0:
#     ld = n % 10
#     r = (r * 10) + ld
#     n = n // 10
#
# print(r)
# ========================================
# n = 321
#
#
# def createReverse(num):
#     revNum = 0
#     while num > 0:
#         ld = num % 10
#         revNum = (revNum * 10) + ld
#         num = num // 10
#     return revNum
#
#
# print(createReverse(n))
# ========================================

# n = 10
# def findArmstrong(n):
#     power = (math.floor(math.log(n,10) + 1))
#     result = 0
#     while n > 0:
#         ld = n % 10
#         result += ld ** power
#         n = n // 10
#     return result
#
# print(findArmstrong(n))
# ========================================

# n = 36
# arr = set()
# for i in range(1, n + 1):
#     if (n % i) == 0:
#         if i == math.sqrt(n):
#             break
#         else:
#             arr.add(i)
#             arr.add(math.floor(n / i))
# print(arr)
# ========================================

# n = 15
# counter = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += 1
#     if counter >2:
#         print("Not Prime Number")
#         break

# n1 = 20
# n2 = 10
#
#
# def findPrimeFactors(x):
#     arr = set()
#     for i in range(1, x + 1):
#         if (x % i) == 0:
#             arr.add(i)
#     arr.add(x)
#     return arr
#
#
# n1 = findPrimeFactors(n1)
# n2 = findPrimeFactors(n2)
# print(n1.intersection(n2))
