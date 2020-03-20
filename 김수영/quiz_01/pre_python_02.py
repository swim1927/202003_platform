""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""


first = int(input("첫번째 수를 입력하세요:"))
second = int(input("두번째 수를 입력하세요:"))
cal = input("연산기호를 입력하세요:")
if cal == '+':
   result = first + second
if cal == '-':
    result = first - second
if cal == '*':
    result = first * second
if cal == '/':
    result = first / second

print(result)