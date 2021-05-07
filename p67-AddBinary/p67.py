import math
def addBinary(a: str, b: str) -> str:
    carry = 0
    i = len(a) - 1
    k = len(b) - 1
    result = ""
    while i > -1 or k > -1:
        if a[i] == '1' and b[k] == '1':
            carry = 1
            result = '0' + result
        elif not (a[i] == '0' and b[k] == '0'):
            if carry != 1:
                result = '1' + result
            else:
                result = '0' + result
                carry = 0
        else:
            if carry == 1:
                result = '1' + result
                carry = 0
            else:
                result = '0' + result
        i -= 1
        k -= 1
      
    return result

def convertToTitle(n: int) -> str:
    if n <= 26:
        return chr(n + 64)
    else:
        m = n % 26
        if m > 0:
            return convertToTitle(n//26) + convertToTitle(m)
        else:
            return convertToTitle(n//26 - 1) + 'Z'


def majorityElement(nums: [int]) -> int:
    temp_dict = {nums[0]: 1}

    maxTime = 1
    maxNum = nums[0]
    for i in nums[1:]:
        if i in temp_dict:
            temp_dict[i] += 1
            if temp_dict[i] < maxTime:
                maxNum = i
                maxTime = temp_dict[i]
        else:
            temp_dict[i] = 1
    return maxNum
def titleToNumber(s: str) -> int:
    if len(s) < 2:
        return ord(s) - 64
    else:
        return titleToNumber(s[:len(s)-1])*26 + titleToNumber(s[len(s) - 1])

def trailingZeros(n: int) -> int:
    if (n < 5):
        return 0
    if n == 5:
        return 1
    else:
        return int(n//5 + trailingZeros(n/5))

def rotate(n: [int], step: int) -> None:
    i = len(n) - 1
    while i >= step:
        temp = n[i]
        n[i] = n[i-step]
        n[i-step] = temp 
        i -= 1
    rotate1(n, i)

def rotate1(n: [int], lim) -> None:
    temp = n[lim]
    for i in range(lim, 0, -1):
        n[i] = n[i-1]
    n[0] = temp

def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n //= 10
    return count

def isHappy(n: int) -> bool:
    temp = sumSquareDigits(n)
    v = {n}
    while temp not in v:
        if temp == 1:
            return True 
        else:
            v.add(temp)
            temp = sumSquareDigits(temp)
    return False
def sumSquareDigits(n: int) -> int:
    if n < 10:
        return n*n
    else:
        return sumSquareDigits(n//10) + sumSquareDigits(n%10)
def countPrimes(n: int) -> int:
    count = 0
    for i in range(2, n + 1):
        
        if isPrime(i): 
            count += 1
    return count 

def isPrime(x : int) -> bool:
    if x == 2 or x == 3 or x == 5 or x == 7:
        return True 
    else:
        i = 2
        lim = math.sqrt(x)
        while i * i <= x:
            if x % i == 0:
                return False 
            i += 1
        print(f"i: {i} x: {x}")
        return True

def siev(n: int) -> int:
    temp = {}
    count = 0
    for i in range(2, n+1):
        temp[i] = True 

    print(f"length: {len(temp)}")
    
    i = 2
    while i*i <= n:
        if temp.get(i) == True:
            for j in range (i * i, n+1, i):
                temp[j] = False
        i += 1
            
    for k in temp:
        if temp[k] == True: count += 1
    return count

def isPowerOfTwo(n: int) -> bool:
    if n < 2 or n & 1 == 1:
        return False 
    elif n == 2:
        return True 
    else:
        return isPowerOfTwo(n//2)

def sumSet(n: [int]) -> int:
    return sum(n)
if __name__ == "__main__":
    n = 'abc'

    n = "AZ"

    n = [1, 2, 3, 4, 5, 6, 7]

    # print(n)
    # rotate(n, 3)

    # print(n)

    print(countPrimes(10))

    n = siev(20)
    n = 1024
    print(isPowerOfTwo(n))

    temp = [3, 0 ,1]
    
    n = len(temp)
    m = (n + 1)*n//2 

    x = m - sumSet(temp)
    print(x)
    
    
 
