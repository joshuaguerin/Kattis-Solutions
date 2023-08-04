# easy, arithmetic

denom = int(input())
nums = list(map(int, input().split()))

pos_nums = [i if i>0 else 0 for i in nums]
neg_nums = [i if i<0 else 0 for i in nums]

total = (sum(pos_nums)) /  (denom + sum(neg_nums))

print(total)

