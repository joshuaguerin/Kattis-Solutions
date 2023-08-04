nums = list(map(int, input().split()))
nums.sort()
letters = input()

print(nums[ord(letters[0])-65], end=" ")
print(nums[ord(letters[1])-65], end=" ")
print(nums[ord(letters[2])-65])


