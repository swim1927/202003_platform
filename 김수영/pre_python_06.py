"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""

a = int(input("숫자를 입력하시오:"))

for i in range(1, a + 1):
    print(' ' * (a - i) + '★' * i)
for j in range(1, a):
    print(' ' * (j) + '★' * (a - j))