# sequence processing

n = input()
nums = list(map(int, input().split()))
nums.sort()

current_range = []

def unpack(arr):
    if len(arr) == 1:
        print(arr[0], end=' ')
    elif len(arr) == 2:
        print(arr[0], arr[1], end=' ')
    else:
        print(arr[0], '-', arr[-1], sep='', end=' ')

for num in nums:
    if current_range == []:
        current_range.append(num)
    elif current_range[-1]+1 == num:
        current_range.append(num)
    else:
        # finished packing range
        unpack(current_range)
        current_range = [num]

# unpack last range
unpack(current_range)

print()


        
    
