# easy, simulation, list, functional

(n, m) = list(map(int, input().split()))

left = sum(map(int, input().split()))

right = sum(map(int, input().split()))

if left == right:
    print("either")
elif left < right:
    print("left")
else:
    print("right")

