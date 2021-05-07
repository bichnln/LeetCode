def ComplementOfInt(n: int) -> int:
   result = 0
   t = 0
   if n == 0 or n == 2:
      return 1 
   elif n == 1:
      return 0
   else:
      while n >= 2:
         if n % 2 == 0:
            result += pow(2, t)
         t += 1 
         n = n//2 
      return result 

if __name__ == "__main__":
   n = int(input("Please enter an integer: "))
   result = ComplementOfInt(n)
   print(f"Complement of {n} is: {result}")
