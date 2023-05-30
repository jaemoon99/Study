from itertools import combinations

def solution(nums):
    num = set(combinations(sorted(nums), len(nums) // 2))
    return num

print(solution([3,3,3,2,2,4]))