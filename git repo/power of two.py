# question three : power of two

def poweroftwo(num):
   return (num & (num - 1)) == 0


user_input = int(input("Enter an integer: "))
result = poweroftwo(user_input)

print(f" {result}")
