"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

a = input("첫번째 사람이 주사위를 던지세요:")
a_num = random.choice([1,2,3,4,5,6])
print("{}이 나왔습니다.".format(a_num))
b = input("두번째 사람이 주사위를 던지세요:")
b_num = random.choice([1,2,3,4,5,6])
print("{}이 나왔습니다.".format(b_num))

if a_num > b_num:
    print("첫번째 사람이 승리했습니다.")
if a_num == b_num:
    print("무승부입니다.")
if a_num < b_num:
    print("두번째 사람이 승리했습니다.")