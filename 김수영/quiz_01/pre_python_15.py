"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """

identification = input("주민등록번호를 입력하세요: ")

if len(identification) == 13:
    if identification[6] == str(1):
        print('남성')
    elif identification[6] == str(2):
        print('여성')
    else:
        print('잘못입력하셨습니다.')
elif len(identification) == 14:
    if identification[7] == str(1):
        print('남성')
    elif identification[7] == str(2):
        print('여성')
    else:
        print('잘못입력하셨습니다.')
elif len(identification) == 16:
    if identification[9] == str(1):
        print('남성')
    elif identification[9] == str(2):
        print('여성')
    else:
        print('잘못입력하셨습니다.')
else:
    print("다시 입력해주세요.")