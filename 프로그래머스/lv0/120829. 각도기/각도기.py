def solution(angle):
    if 0 < angle < 90:
        answer = 1
    elif 90 == angle:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    else :
        answer = 4
    return answer