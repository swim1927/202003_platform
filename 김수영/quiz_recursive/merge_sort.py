
#병합정렬

#리스트 분할
def divide_and_merge(a):
    if len(a) <= 1:
        return a
    k = len(a) // 2
    fh = a[:k]
    sh = a[k:]
    #재귀호출
    fh = divide_and_merge(fh)
    sh = divide_and_merge(sh)
    sorted_list = merge_sort(fh, sh)
    return sorted_list

#병합정렬하는 부분
def merge_sort(a,b):
    ans = []
    while len(a) > 0 or len(b) > 0:
        if len(a) > 0 and len(b) > 0:
            if a[0] <= b[0]:
                ans.append(a[0])
                a = a[1:]
            else:
                ans.append(b[0])
                b = b[1:]
        elif len(a) > 0:
            ans.append(a[0])
            a = a[1:]
        elif len(b) > 0:
            ans.append(b[0])
            b = b[1:]
    return ans