#aFibonacci v1.0
#by Kamp

def genFib(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return genFib(n-1) + genFib(n-2)

def Fibonacci(x):
    for i in range(x):
        print(genFib(i+1))

print("Fibonacci Generator")
uInput = int(input("How many numbers would you generate?\n"))
if not uInput == 0:
    Fibonacci(uInput)
