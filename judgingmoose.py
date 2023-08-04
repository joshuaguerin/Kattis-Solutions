# easy, arithmetic, logic

(l, r) = list(map(int, input().split()))

if not l and not r:
    print("Not a moose")
elif l==r:
    print("Even", l+r)
else:
    print("Odd", 2*(l if l > r else r))
