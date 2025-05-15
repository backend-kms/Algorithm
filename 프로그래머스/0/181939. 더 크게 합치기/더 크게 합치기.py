def solution(a, b):
    front = str(a) + str(b)
    back = str(b) + str(a)
    return int(front) if int(front) > int(back) else int(back)