def Seperation(n):
    ''' Calculate ways to seperate n into 1 and 2 '''
    return (n//2) + 1

def Factorial(n, result = 1):
    if n < 2:
        return result 
    else:
        result *= n
        return Factorial(n -1, result)

def ClimbStairs(n: int, z: int) -> int:
    ''' Calculate ways to organise 1s and 2s based on their seperation z '''
    sum = 0
    # if n is even
    if not n & 1 == 1:
        for i in range(0, z):
            if i == 0 or 2*i == n:
                sum += 1
            else:
                x = n - 2*i
                slots = x + i
                sum += Factorial(slots) / (Factorial(x) * Factorial(i))
    else:
        for i in range(0, z):
            if i == 0:
                sum += 1
            else:
                x = n - 2*i
                slots = x + i
                sum += Factorial(slots) / (Factorial(x) * Factorial(i))
    return sum



if __name__ == "__main__":
    n = int(input("Please enter number of stairs: "))
    z = Seperation(n)
    result = ClimbStairs(n, z)
    print(f"Ways to climb stairs: {result}")
