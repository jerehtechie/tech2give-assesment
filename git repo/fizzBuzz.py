# Question 1: FizzBuzz

for num in range(1, 101):
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("fizzBuzz")
    else:
        print(num)
