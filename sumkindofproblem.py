p = int(input())

for i in range(p):
    k, n = map(int, input().split())
    print(k, n*(n+1)//2, 1 + (n-1)*n + (n-1), 2 * (n * (n + 1) // 2))

# Explanation:
# (I would conjecture that speed is going to be an issue for direct summation)
# Use basic discrete mathematics to locate closed forms
#
# first n:
#       n(n+1) / 2
#
# first n odd:
# consider: sum(first 5 odd)
#         = sum(1, 3, 5, 9)
#         = sum(1, 2+1, 4+1, 8+1)
# general:  sum(1, 2+1, 4+1, ..., 2(n-1)+1)
# move 1's outside sum():
#         = 1 + sum(2, 4, ..., 2(n-1)) + (n-1)
#         = 1 + 2 * sum(1, 2, ..., (n-1)) + (n-1)
#         = 1 + 2 * (n-1)n/2 + (n-1)
#         = 1 + (n-1)n + (n-1)
#
# first n even:
# consider: sum(first 5 even)
#         = sum(2, 4, 6, 8, 10)
#         = 2 * sum(1, 2,, 3, 4, 5)
#         = 2 * n(n+1)/2
