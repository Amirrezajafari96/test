# #
# a = 5
# b = 3
# print (a + b)

# #1. Sum of Two Numbers
#number1 = int(input("enter number1: "))
# number2 = int(input("enter number2: "))
# print("Sum:", number1 + number2)


#Check Even or Odd
# number = int(input("Enter Nmuber: "))
# if number %2 == 0:
#     print("Even")
# else:
#     print("Odd")

#3. Find the Largest Number
# number1 = int(input("Enter number1: "))
# number2 = int(input("Enter number2: "))
# number3 = int(input("Enter number3: "))
# print("Largest one: ", max(number1, number2, number3))

#4-Factorial of a Number
# num = int(input("type a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
#     print("factorial:", factorial)

#5 add sum of 1-10
# jam = 1
# for i in range(1, 999):
#     jam *= i
# print("sum: ",jam)

# name = input("Type your name: ")
# print("Hello",name,"! Good to see you.")

# a = int(input("type a number: "))
# b = int(input("type another number: "))

# print("sum = ",a + b)
# print("Difference = ",a - b)
# print("Multiplication = ",a * b)
# print("Division = ",a / b)

# num = int(input("type a number: "))
# if num % 2 == 0:
#     print(num,"is even.")
# else:
#     print(num,"is odd.")

# jam = 1
# for i in range(1, 999):
#     print(i)

#حلقه‌ی while:
# num = int(input("type a number: "))
# if num > 0:
#     i = 1
#     while i <= num:
#         print(i)
#         i += 1
# else:
#     print("not 0!")

# numbers = [1, 2, 3, 4, 5]
# jam = sum(numbers)
# print("Majmoesh: ", jam)

# num = int(input("type a number: "))
# factoriel = 1
# for i in range (1, num + 1):
#  factoriel *= i
#  print (factoriel)

# def factoriel(n):
#     if n < 0:
#         return "factoriel tarif nashude"
#     if n==0 or n==1:
#         return 1
    
#     result = 1
#     for i in range(2,n+1):
#         result *= i
    
#     return result

# num = int(input("type a nnumber: "))
# print("factoriel", num,"=", factoriel(num))

# text = input("type a word: ")
# length = len(text)
# print("count: ", length)

# people = {}
# people["amir"] = 28
# people["ali"] = 32
# people["sara"] = 24
# for name, age in people.items():
#    print(f"name:{name}, age:{age}")

def fibonacci(n):
    # حالت پایه: اگر n برابر ۰ یا ۱ باشد، همان n را برمی‌گردانیم
    if n == 0 or n == 1:
        return n
    
    # حالت بازگشتی: جمع دو عدد قبلی در دنباله فیبوناچی
    return fibonacci(n - 1) + fibonacci(n - 2)
# دریافت عدد از کاربر
n = int(input("type a number: "))
# فراخوانی تابع و چاپ نتیجه
print(f"{n}th Fibonacci number: {fibonacci(n)}")