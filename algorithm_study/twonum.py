def solution(numbers):
    answer = []
    for x in range(0, len(numbers)):
        for y in range(0, len(numbers)):
            if x != y:
                answer.append(numbers[x] + numbers[y])
    return  sorted(list(set(answer)))


numbers = [2,1,3,4,1]

solution(numbers)