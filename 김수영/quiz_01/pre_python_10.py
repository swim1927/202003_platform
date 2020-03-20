"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""

def factorial(n):
    m = 1
    for i in range(1, n + 1):
        m *= i
    return m

print(factorial(5))