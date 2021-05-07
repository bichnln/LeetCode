from typing import List, Optional
def PascalTriangle(n: int) -> List[List[int]]:
    result = []
    result.append([1])
    result.append([1, 1])
    for i in range(2,n):
        arr = [1]
        for j in range(1, i):
            arr.append(result[i-1][j]+result[i-1][j-1])
        arr.append(1)
        result.append(arr)
    return result

def combinatorial(n: int, k: int) -> int:
    if k == 1 or n - k == 1:
        return n
    result = 1/factorial(n-k)
    while n > k:
        result *= (n)
        n -= 1
    print(result)
    return result


def factorial(x: int)  -> int:
    result = x
    while x > 1:
        result *= x-1
        x -= 1
    return result
if __name__ == "__main__":
    print(combinatorial(6,4))
