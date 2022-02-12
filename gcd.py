# The greatest common divisor GCD
# if a % b = r then gcd(a, b) = gcd(b, r)

a = int(input('Enter a: '))
b = int(input('Enter b: '))

def gcd(a, b):
    if a % b == 0:
        return b
    if a < b:
        return gcd(b, a)
    else:
        return gcd(b, a%b)


n = gcd(a, b)
print('GDC of',a, 'and', b, 'is', n)