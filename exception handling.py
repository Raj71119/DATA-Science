# try except
print ("Enter a number")
num1 = input()
print ("Enter another number")
num2 = input()
try:
    print ("The sum of these two numbers is ",
       int(num1)+int(num2))
except Exception as e:
    print (e)

print ("This line is importasnt")