a=int(input("please enter the first value "))
b=int(input("please enter the second value "))
operator=input("please enter the operator ")

# applying if statements
if operator=='+':
    result=a+b
elif operator=='-':
    result=a-b
elif operator=='*':
    result=a*b
elif operator=='/':
    result=a/b
else:
    print("invalid operator")

print(result)

