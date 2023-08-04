# string processing, counting 

vowels = ['a','e','i','o','u','y']

# Note: I'm guessing don't use replacement.
# E.g., floeeop should be 1 not 2

n = int(input())

while n != 0:
    most_string = ""
    most_count = -1

    # find best string
    for i in range(n):
        current = input()
        j = 0

        # count consecutive vowels in string
        count = 0
        while j < len(current)-1:
            if current[j] in vowels and current[j]==current[j+1]:
                count+=1
                j+=1
            j+=1
        
        if most_count < count:
            most_count = count
            most_string = current

    print(most_string)
            
    n = int(input())

