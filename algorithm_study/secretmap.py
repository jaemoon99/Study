def solution(n, arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        print(f'{bin(arr1[x] | arr2[x])},   {bin(arr1[x] | arr2[x]).split("b")[1]}')
        value = bin(arr1[x] | arr2[x]).split("b")[1].replace("0", " ").replace("1", "#")
        answer.append(" "*(n - len(value)) + value)
    return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))