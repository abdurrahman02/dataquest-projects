A = [247, 240, 303, 9, 304, 105, 44, 204, 291, 26, 242, 2, 358, 264, 176, 289, 196, 329, 189, 102, 45, 111, 115, 339,
     74, 200, 34, 201, 215, 173, 107, 141, 71, 125, 6, 241, 275, 88, 91, 58, 171, 346, 219, 238, 246, 10, 118, 163, 287,
     179, 123, 348, 283, 313, 226, 324, 203, 323, 28, 251, 69, 311, 330, 316, 320, 312, 50, 157, 342, 12, 253, 180, 112,
     90, 16, 288, 213, 273, 57, 243, 42, 168, 55, 144, 131, 38, 317, 194, 355, 254, 202, 351, 62, 80, 134, 321, 31, 127,
     232, 67, 22, 124, 271, 231, 162, 172, 52, 228, 87, 174, 307, 36, 148, 302, 198, 24, 338, 276, 327, 150, 110, 188,
     309, 354, 190, 265, 3, 108, 218, 164, 145, 285, 99, 60, 286, 103, 119, 29, 75, 212, 290, 301, 151, 17, 147, 94,
     138, 272, 279, 222, 315, 116, 262, 1, 334, 41, 54, 208, 139, 332, 89, 18, 233, 268, 7, 214, 20, 46, 326, 298, 101,
     47, 236, 216, 359, 161, 350, 5, 49, 122, 345, 269, 73, 76, 221, 280, 322, 149, 318, 135, 234, 82, 120, 335, 98,
     274, 182, 129, 106, 248, 64, 121, 258, 113, 349, 167, 192, 356, 51, 166, 77, 297, 39, 305, 260, 14, 63, 165, 85,
     224, 19, 27, 177, 344, 33, 259, 292, 100, 43, 314, 170, 97, 4, 78, 310, 61, 328, 199, 255, 159, 185, 261, 229, 11,
     295, 353, 186, 325, 79, 142, 223, 211, 152, 266, 48, 347, 21, 169, 65, 140, 83, 156, 340, 56, 220, 130, 117, 143,
     277, 235, 59, 205, 153, 352, 300, 114, 84, 183, 333, 230, 197, 336, 244, 195, 37, 23, 206, 86, 15, 187, 181, 308,
     109, 293, 128, 66, 270, 209, 158, 32, 25, 227, 191, 35, 40, 13, 175, 146, 299, 207, 217, 281, 30, 357, 184, 133,
     245, 284, 343, 53, 210, 306, 136, 132, 239, 155, 73, 193, 278, 257, 126, 331, 294, 250, 252, 263, 92, 267, 282, 72,
     95, 337, 154, 319, 341, 70, 81, 68, 160, 8, 249, 96, 104, 137, 256, 93, 178, 296, 225, 237]


def repeatedNumber(A):
    A = [i for i in A]
    l = len(A)
    for i in range(l):
        if A[abs(A[i]) - 1] < 0:
            print(A[i], i, A[A[i] - 1])
            return abs(A[i])
        A[abs(A[i]) - 1] = (A[abs(A[i]) - 1]) * (-1)
        print(abs(A[i]) - 1, A[abs(A[i]) - 1])
    return -1


# print(repeatedNumber(A))
def dompare(item1, item2):
    if item1 + item1 > item2 + item1:
        return -1
    else:
        return 1


def largestNumber(A):
    b = [str(i) for i in A]
    b = sorted(b, cmp = dompare)
    return "".join(b)


# print(largestNumber([3, 30, 34, 5, 9]))

# def maximumGap(A):
#     lmin = [0]
#     i = 1
#     l = len(A)
#     if l == 1:
#         return -1
#     smalli = 0
#     largei = l - 1
#     rmax = [0]*l
#     while i < l:
#         if A[i] >= A[smalli]:
#             lmin.append(smalli)
#         else:
#             smalli = i
#             lmin.append(i)
#         i += 1
#     i = l - 1
#     largei = l-1
#     while i >= 0:
#         if A[i] <= A[largei]:
#             # print (largei)
#             rmax[i] = largei
#         else:
#             largei = i
#             # print (i)
#             rmax[i] = largei
#         i -=1
#     i = 0
#     j = 0
#     maxv = -1
#     while i < l and j < l:
#         if(A[lmin[i]]) < (A[rmax[j]]):
#             while j < l and (A[lmin[i]]) < (A[rmax[j]]):
#                 maxv = max(maxv, rmax[j] - lmin[i])
#                 j += 1
#         else:
#             i = i + 1
#     return maxv

#
# print(maximumGap([3, 5, 4, 2]))
# print(maximumGap([1, 2, 3, 77, 76, 75, -1]))


# def setZeroes(A):
#     Blen = [0]*len(A[0])
#     Alen = [0]*len(A)
#     print(len(Alen), len(Blen))
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             if A[i][j] == 0:
#                 Alen[i] = 1
#                 Blen[j] = 1
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             if Alen[i] == 1 or Blen[j] == 1:
#                 print(i, j)
#                 A[i][j] = 0
#     return A
#
# print(setZeroes([[1, 2, 3], [5, 6, 7], [0, 2, 1], [5, 0, 6] ]))
# class Solution:
#     def diagonal(self, A):
#         q = []
#         m = len(A)
#         n = len(A[0])
#         l = m*n
#         line = 0
#         for i in range(m):
#             x, y = i, 0
#             p = []
#             while x >= 0:
#                 p.append(A[x][y])
#                 x = x-1
#                 y = line - x
#             q.append(p)
#             line += 1
#         i = m-1
#         for j in range(1, n):
#             x, y = m-1, j
#             p = []
#             while y < n:
#                 p.append(A[x][y])
#                 y = y + 1
#                 x = line - y
#             q.append(p)
#             line += 1
#         return [i[::-1] for i in q]
# diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# def findAllIntegers(num):
#     p = []
#     l = len(num)
#     for i in range(l-1):
#         p.append(num[i])
#         for j in range(i+1,l):
#             p.append((num[i:j+1]))
#     return p
#
# def product_contig(num):
#     return reduce(lambda x, y: x*y, [int(i) for i in num])
#
# def colorful( A):
#     inte = findAllIntegers(str(A))
#     x = {}
#     for i in inte:
#         res = self.product_contig(i)
#         if x.get(res, -1) == -1:
#             return 0
#     return 1
# dp = {}
#
# class Solution:
#     # @param A : integer
#     # @return an integer
#     # def twoSum(self, A, B):
#     #     x = {}
#     #     l = len(A)
#     #     for i in range(l):
#     #         if x.get(B - A[i], (-1, -1)) != (-1, -1):
#     #             return [x[B-A[i]][1]+1, i+1]
#     #         if x.get(A[i], (-1, -1)) == (-1, -1):
#     #             x[A[i]] = (A[i], i)
#     #         print(x)
#     #     return []
#     # def doi(self, a, b):
#     #     return min(a[1], b[1]) >= max(a[0], b[0])
#     #
#     # def merg(self, a, b):
#     #     a[0] = min(a[0], b[0])
#     #     a[1] = max(a[1], b[1])
#     #     return a
#     # # @param intervals, a list of Intervals
#     # # @return a list of Interval
#     # def merge(self, intervals):
#     #     intervals.sort(key = lambda x: x[0])
#     #     print(intervals)
#     #     l = len(intervals)
#     #     p = []
#     #     p.append(intervals[0])
#     #     i = 1
#     #     while i < l:
#     #         ib = p.pop()
#     #         if self.doi(ib, intervals[i]):
#     #             ib = self.merg(ib, intervals[i])
#     #             p.append(ib)
#     #         else:
#     #             p.append(ib)
#     #             p.append(intervals[i])
#     #         i = i+1
#     #     return p
#     def primesum(self, A):
#         sieve = {}
#         s2 = [0]*(A+1)
#         j = 2
#         s3 = []
#         while j*j <= (A):
#             if s2[j] == 0:
#                 q = 2
#                 while j*q <= A:
#                     s2[j*q] = 1
#                     q = q + 1
#             j += 1
#         s3 = []
#         for i in range(2,A+1):
#             if s2[i] == 0:
#                 sieve[i] = 1
#                 s3.append(i)
#         # s3 = sorted(sieve.keys())
#         for i in s3:
#             if sieve.get(A-i, -1) != -1:
#                 return [i, A-i]

# Solution.colorful()
# s = Solution()
# print(s.twoSum([ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ], -3))
# print (s.merge([ [1, 10], [2, 9], [3, 8], [4, 7], [5, 6], [6, 6] ]))
# print(s.primesum(16777214))
# print (dp, "hey")

class Solution:
    # @param A : integer
    # @return a boolean
    def bsearch(self, low, high, n):
        mid = (low + high)//2
        print(mid, low, high)
        if low > high:
            return -1
        if mid*mid < n:
            if low == high:
                return low
            return self.bsearch(mid+1, high, n)
        elif mid*mid > n:
            if low == mid:
                return mid-1
            return self.bsearch(low, mid-1, n)
        elif mid*mid == n:
            return mid

    def sqrt(self, n):
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.bsearch(1, n//2 + 2, n)



import math
s = Solution()
print(s.sqrt(5))
# print(s.sqrt(24))
# print(s.majorityElement([1,2,2,1]))
# print(s.majorityElement([1,2,2,3,2,2,1,3,3,3,3,1]))
# print (s.isPower(1024000000))
# print (math.log(1024000000, 2))