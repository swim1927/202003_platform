"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']
"""

file = ['exit.py', 'hi.py', 'playdata.hwp', 'intro.jpg']

filename = []
for name in file:
    n_list = name.split('.')
    filename.append(n_list[0])

print(filename)