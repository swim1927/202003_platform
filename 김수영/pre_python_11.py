"""11. 최대공약수를 구하는 함수를 구현하시오"""


def gcd(m, n):
    divisor = []

    for i in range(1, m):
        if (m % i == 0) and (n % i == 0):
            divisor.append(i)

    return max(divisor)

print(gcd(1040, 540))