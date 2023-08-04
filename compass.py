current = int(input())
correct = int(input())

plus = 0
minus = 0

# Yes, there is probably a better solution
# In a competition this is probably how I would go because:
# a. complexity shouldn't get to us
# b. no scratch work necessary
# c. took about 30 seconds to code correctly

while (current + plus)%360 != correct:
    plus += 1
while (current + minus)%360 != correct:
    minus -= 1
if plus == 0:
    print(0)
elif plus == minus:
    print(180)
elif abs(minus) < plus:
    print(minus)
else:
    print(plus)

