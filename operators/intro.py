a = "hello"
print(a)

# types operator
# 1.Arithmatic operator
# addition
num1 = 2
num2 = 3
num3 = num1+num2
print(num3)

# subration
num1 = 2
num2 = 3
num3 = num1-num2
print(num3)

# multiple
num1 = 2
num2 = 3
num3 = num1*num2
print(num3)

# division
num1 = 2
num2 = 3
num3 = num1/num2
print(num3)

# modulo
num1 = 2
num2 = 3
num3 = num1 % num2
print(num3)

# exponential
num1 = 2
num2 = 3
num3 = num1**num2
print(num3)


# 2.Assignment operator
print("Assignment operator")

num1 = 2
num2 = 3
num1 += num2
print(num1)

num1 = 2
num2 = 3
num1 -= num2
print(num1)

num1 = 2
num2 = 3
num1 *= num2
print(num1)

num1 = 2
num2 = 3
num1 /= num2
print(num1)

num1 = 2
num2 = 3
num1 %= num2
print(num1)

num1 = 2
num2 = 3
num1 **= num2
print(num1)

# Comparation oprator
print("Comparasion operator")
num1 = 2
num2 = 3
if num1 == num2:
    print("True")
elif num1 != num2:
    print("False")

num1 = 2
num2 = 3
if num1 <= num2:
    print("True")
elif num1 != num2:
    print("False")        

# Logical operator
print("Logical operator")

num1 = 2
num2 = 2
num3 = 4
if num1 == num2 and num1==num3:
    print("All are equal")
elif num1 == num2 or num1==num3:
    print("num1 and num2 are equal")
