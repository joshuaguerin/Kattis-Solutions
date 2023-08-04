import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))

    # attempt each sum
    for n in nums:
        if sum(nums)-n == n:
            print(n)
            break
