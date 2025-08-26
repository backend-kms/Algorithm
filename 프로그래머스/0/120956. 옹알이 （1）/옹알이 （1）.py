def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        word = i
        for p in possible:
            word = word.replace(p, " ")
        if word.strip() == "":
            answer += 1
    
    return answer