num = int(input("enter a three-digit number: "))
a = num // 100
b = num % 100 // 10
c = num % 10
print(f"sum of values: {a+b+c}")
print(f"multiplication of values: {a*b*c}")

