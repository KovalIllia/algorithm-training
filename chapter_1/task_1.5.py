"""variant_1"""
a=int(input("Input value a: "))
b=int(input("Input value b: "))
c=int(input("Input value c: "))
max_value=a
if max_value<b:
    max_value=b
if max_value<c:
    max_value=c
print(f"max_value: {max_value}")

"""variant_2"""
a=int(input("Input value a: "))
b=int(input("Input value b: "))
c=int(input("Input value c: "))
if a>b:
    if a>c:
        print(f"max_value: {a}")
    else:
        print(f"max_value: {c}")
if a<b:
    if b>c:
        print(f"max_value: {b}")
    else:
        print(f"max_value: {c}")