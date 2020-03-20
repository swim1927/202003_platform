"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오"""


for year in range(1988, 2061):
    if (year - 1990) % 4 == 0:
        print(year, end = ' ')