def superDigit(n, k) -> int:
    n = digitSum(n)
    if k > 1:
        n *= k
    return digitSum(n)
    

def digitSum(n) -> int:
    while n > 9:
        n = n//10 + n%10
    return n


if __name__ == "__main__":
    print(superDigit(9875, 3))