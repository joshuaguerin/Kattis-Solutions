# easy, strings, palindromes, slicing

s = input()
(a, b) = s[:len(s)//2], s[len(s)//2:]

if len(s)%2 == 1:
    b = b[1:]

if a == b[::-1]:
    print("Palindrome!")
else:
    print("Nothing special about this string :(")
