"""variant_1"""
# def binary(num):
#     s=''
#     while num>0:
#         s=f'{num%2}{s}'
#         num//=2
#     return s
# print(binary(255))


"""variant_2"""
def binary(num):
    s=''
    while num>0:
        s=f'{num%2}{s}'
        num//=2
    return s

while True:
    n=int(input("Input N value: "))
    if n!=0:
        print(binary(n))
    else:
        break

print(binary(255))