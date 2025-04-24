"""
*****
*****
*****
*****
*****
"""

# for _ in range(5):
#     for _ in range(5):
#         print("*", end="")
#     print("\n", end="")

# ============Using Recursion
# counter = 0
# bound = 5
#
#
# def print_star():
#     global counter
#     counter += 1
#     if counter < bound:
#         print("*" * bound, end="\n")
#         return print_star()
#     else:
#         return
#
#
# print_star()
# ====================
"""
*
**
***
****
*****
"""
# counter: int = 1
# for _ in range(5):
#     print("*" * counter)
#     counter += 1
# ====================
"""
1
12
123
1234
12345

"""
# counter = 1
# for _ in range(5):
#     for i in range(counter * 0 + 1, counter + 1):
#         print(i, end="")
#     counter += 1
#     print("\n", end="")
# ====================


"""
1
22
333
4444
55555
"""
# counter = 1
# for _ in range(5):
#     print(f"{counter}" * counter)
#     counter += 1

# ====================

"""
*****
****
***
**
*
"""
# i = 5
# while i > 0:
#     print("*" * i)
#     i -= 1

# ====================

"""
12345
1234
123
12
1
"""
# count = 5
# for _ in range(count):
#     for j in range(1, count + 1):
#         print(j, end="")
#     count -= 1
#     print("\n", end="")
# ====================

"""
     *     
    ***    
   *****   
  *******  

"""

# cols = 4
# rows = 1
# for i in range(cols):
#     print(" " * cols, "*" * rows, " " * cols)
#     cols -= 1
#     rows += 2

# ====================

"""
  *********  
   *******   
    *****    
     ***     
      *      
"""

# max_offset = 9
# rows = 1
#
# for i in range(5):
#     print(" " * rows, "*" * max_offset, " " * rows)
#     rows += 1
#     max_offset -= 2
# ====================

"""
[5,1,5]
[4,3,4]
[3,5,3]
[2,7,2]
[1,9,1] <===bound
[2,7,2]
[3,5,3]
[4,3,4]
[5,1,5]
"""
"""
      *      
     ***     
    *****    
   *******   
  *********  
   *******   
    *****    
     ***     
      *      

"""
# bound = 9
# start = 1
# space_offset = 5
# reverse = False
# for i in range(bound):
#     print(" " * space_offset, "*" * start, " " * space_offset)
#     if start == bound:
#         reverse = True
#     if reverse:
#         space_offset += 1
#         start -= 2
#     else:
#         start += 2
#         space_offset -= 1

# ====================

"""
*
**
***
****
*****
******
*****
****
***
**
*
"""
# counter = 1
# bound = 5
# reverse = False
# while True:
#     print("*" * counter, end="\n")
#     if counter <= bound and not reverse:
#         counter += 1
#     else:
#         counter -= 1
#         reverse = True
#     if counter < 1 and reverse is True:
#         break

# ====================

"""
1
01
101
0101
10101
"""
# counter: int = 1
# bound: int = 5
# for i in range(bound + 1):
#     if i % 2 != 0:
#         counter = 1
#     for j in range(i):
#         print(counter, end="")
#         if counter == 1:
#             counter = 0
#         else:
#             counter = 1
#     print("", end="\n")
# ====================

"""
1      1
12    21
123  321
12344321
"""
# column = 4
# space_offset = 6
# rows = 8
# counter = 1
# for i in range(column):
#     for j in range(1, counter + 1):
#         print(j, end="")
#     print(" " * space_offset, end="")
#     for k in range(counter, 0, -1):
#         print(k, end="")
#     counter += 1
#     space_offset -= 2
#     print(end="\n")
# ====================


"""

1
2	3
4	5	6
7	8	9	10
11	12	13	14	15

"""
# offset = 1
# bound = 5
#
# for i in range(1, bound + 1):
#     for j in range(i):
#         print(offset, end="\t")
#         offset += 1
#     print()
# 65-90 A-Z


# ====================

"""
A
AB
ABC
ABCD
ABCDE
"""
# alphabet = 65
# for i in range(5+1):
#     for j in range(i):
#         print(chr(alphabet), end="")
#         alphabet += 1
#     alphabet = 65
#     print()
#
# alphabet = 65
# count = 5
# for i in range(6):
#     for j in range(count):
#         print(chr(alphabet), end="")
#         alphabet += 1
#     print()
#     alphabet = 65
#     count -= 1


# while count > 0:
#     for _ in range(count):
#         print(chr(alphabet), end="")
#         alphabet += 1
#     print()
#     count -= 1
#     alphabet  = 65
# ====================

"""
A
BB
CCC
DDDD
EEEEE

"""
# alphabet = 65
# for i in range(1, 6):
#     for _ in range(i):
#         print(chr(alphabet), end="")
#     print()
#     alphabet += 1
# ====================


"""
[3,1,3]
[2,3,2]
[1,5,1]
[0,7,0]
"""
# counter = 1
# space_offset = 5
# reverse = False
# alphabet = 65
# for i in range(4):
#     print(" " * space_offset, end="")
#     for j in range(1, counter + 1):
#         print(chr(alphabet), end="")
#         if int((counter + 1) / 2) == j:
#             reverse = True
#         if reverse:
#             alphabet -= 1
#         else:
#             alphabet += 1
#     print(" " * space_offset, end="")
#
#     alphabet = 65
#     counter += 2
#     reverse = False
#     space_offset -= 1
#     print()
# ====================

"""
E
DE
CDE
BCDE
ABCDE
"""
# alphabet = 69
# alphabet_offset = 69
# for i in range(5):
#     for j in range(alphabet, alphabet_offset+1):
#         print(chr(j), end="")
#     alphabet -= 1
#     print()
# ====================
"""
[5,0,5]
[4,2,4]
[3,4,3]
[2,6,2]
[1,8,1]
[1,8,1]
[2,6,2]
[3,4,3]
[4,2,4]
[5,0,5]
"""

"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""
# star_offset = 5
# space_offset = 0
# reverse = False
#
#
# def print_star():
#     for _ in range(star_offset):
#         print("*", end="")
#
#
# for i in range(10):
#     print_star()
#     print(" " * space_offset, end="")
#     print_star()
#     print()
#     if reverse:
#         star_offset += 1
#         space_offset -= 2
#     else:
#         star_offset -= 1
#         space_offset += 2
#     if star_offset == 0:
#         star_offset = 1
#         space_offset = 8
#         reverse = True

# ====================
""" 
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""
# star_offset = 1
# space_offset = 8
# reverse = False
#
#
# def print_star():
#     for _ in range(star_offset):
#         print("*", end="")
#
#
# for i in range(10):
#     print_star()
#     print(" " * space_offset, end="")
#     print_star()
#     print()
#     if star_offset == 5:
#         reverse = True
#     if reverse:
#         space_offset += 2
#         star_offset -= 1
#     else:
#         space_offset -= 2
#         star_offset += 1
# ====================


"""
****

*  *

*  *

****
"""


# cols = 7
# rows = 4
#
#
# def print_star():
#     for j in range(rows):
#         print("*", end='')
#
#
# def print_odd_stars(star=""):
#     for j in range(rows):
#         if j == 0 or j == rows - 1:
#             print(star, end="")
#         else:
#             print(" ", end="")
#
#
# for i in range(1, cols + 1):
#     if i == 1:
#         print_star()
#     elif i == cols:
#         print_star()
#     if i % 2 != 0 and i < cols and i != 1:
#         print_odd_stars("*")
#     print()
# ====================
