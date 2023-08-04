# easy, arithemtic, mod

# info hard-coded for 2009
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

(d, m) = list(map(int, input().split()))

print(name[(sum(days[:m]) + d) % 7])

