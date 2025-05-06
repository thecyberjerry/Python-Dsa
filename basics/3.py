# n = 10
#
# count = 0
#
#
# def printNum(x):
#     global count
#     count += n
#
#     def printInReverse(num):
#         global count
#         count -= 1
#         print(count, end=" ")
#         if count == 1:
#             return
#         else:
#             printInReverse(num)
#
#     printInReverse(x)
#
#
# printNum(n)
# ==================
# n = 6
#
#
# def printNaturalNumbers(x):
#     count = 0
#     total = 0
#
#     def loopNums(x):
#         nonlocal count
#         nonlocal total
#         count += 1
#         total += count
#         if count == x:
#             return
#         else:
#             loopNums(x)
#
#     loopNums(x)
#     print(total)
#
#
# printNaturalNumbers(n)
# ==================
import time

# x = 3
#
#
# def getFactorial(x):
#     count = x
#     total = 1
#
#     def multiplyNum(x):
#         nonlocal count
#         nonlocal total
#         if count == 0:
#             return
#         else:
#             total *= count
#             count -= 1
#             multiplyNum(x)
#
#     multiplyNum(x)
#     print(total)
#
#
# getFactorial(x)
# ======================================


# x = 5
#
#
# def getFactorial(x):
#     total = 1
#     def multiplyNum(x):
#         nonlocal total
#         if x == 1:
#             return
#         else:
#             total *= x
#             multiplyNum((x - 1))
#
#     multiplyNum(x)
#     print(total)
#
#
# getFactorial(x)
# ============================================

# arr = [1, 2, 3, 45]


# def iterateArray(arr: list):
#     n = len(arr) - 1
#     a = []
#
#     def reverseArray():
#         nonlocal n
#         a.append(arr[n])
#         n -= 1
#         if n >= 0:
#             return reverseArray()
#         else:
#             return
#
#     reverseArray()
#     print(a)
#
# iterateArray(arr)

# def reverseArray(arr: list):
#     p1, p2 = len(arr) - len(arr), len(arr) - 1
#
#     def initiateReverse():
#         nonlocal p1, p2
#         if p1 >= p2:  # Base case: when p1 crosses p2, the array is reversed
#             return
#         arr[p1], arr[p2] = arr[p2], arr[p1]
#         p1 += 1
#         p2 -= 1
#         return initiateReverse()
#
#     initiateReverse()
#     print(arr)
#
# reverseArray([1, 3, 4, 56, 6])
# ============================================

# n = "amasn"
#
#
# def ifPalindrome(s1: str):
#     c: str = ""
#     counter: int = len(s1) - 1
#
#     def createReversedString():
#         nonlocal c, counter
#         if counter >= 0:
#             counter -= 1
#             c += s1[counter]
#             createReversedString()
#         else:
#             return
#
#     createReversedString()
#     print(c == s1)
#
#
# ifPalindrome(n)

# arr = [1, 2, 3, 43, 1, 1]
#
# hash_arr = {}
# for i in arr:
#     if i in hash_arr:
#         hash_arr[i] += 1
#     else:
#         hash_arr[i] = 1

# arr = "abcdeaee"
# hash_arr = {}
# for i in arr:
#     if i in hash_arr:
#         hash_arr[i] += 1
#     else:
#         hash_arr[i] = 1
#
# print(hash_arr)

# arr = [11, 2, 3, 43, 11, 11, 43, 2, 3, 2, 43, 2, 3, 3, 2, 3, 2, 43]
# hash_arr = {}
# for i in arr:
#     if i in hash_arr:
#         hash_arr[i] += 1
#     else:
#         hash_arr[i] = 1
# print(hash_arr)
#
# print(max(hash_arr, key=hash_arr.get))
# print(min(hash_arr, key=hash_arr.get))
