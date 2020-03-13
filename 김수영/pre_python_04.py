"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""

def triangle_area():
    width = int(input('삼각형의 가로 길이를 입력하세요:'))
    height = int(input('삼각형의 세로 길이를 입력하세요:'))
    area = width * height / 2
    return print(area)

triangle_area()