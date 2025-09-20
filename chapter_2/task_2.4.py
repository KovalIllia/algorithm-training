"""variant_1"""
# def gcd(m,n):
#     while m!=n:
#         if m>n:
#             m-=n
#         else:
#             n-=m
#     return m
# print(gcd(54,24))


"""variant_2"""
# def gcd(m,n):
#     if n==0:
#         return m
#     return gcd(n,m%n)
#
# print(gcd(54,24))


"""variant_3"""


def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


print(gcd(54, 24))
