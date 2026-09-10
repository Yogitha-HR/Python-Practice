n = int(input("Enter a number: "))

s = 0

for i in range(n):
    digit = n % 10
    s = s + digit
    n = n // 10

print("Sum =", s)