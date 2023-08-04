(n, m) = list(map(int, input().split()))

if n < m and m-n == 1:
    print("Dr. Chaz will have", m-n ,"piece of chicken left over!")
elif n < m and m-n != 1:
    print("Dr. Chaz will have", m-n ,"pieces of chicken left over!")
elif m < n and n-m == 1:
    print("Dr. Chaz needs", n-m ,"more piece of chicken!")
else:
    print("Dr. Chaz needs", n-m ,"more pieces of chicken!")
