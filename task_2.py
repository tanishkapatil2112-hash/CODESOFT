Number_1=int(input("Enter the first number:"))
number_2=int(input("Enter the second number:"))

print("Enter your choice")
print("1. Addition")
print("2. subtraction")
print("3.multiplication")
print("4.Division")
print("5.modulus")

choice=input("Enter your choice")

if choice=='1':
    operation=Number_1+number_2
    print("Result:",operation)

elif choice=='2':
    operation=Number_1-number_2
    print("Result:",operation)

elif choice=='3':
    operation=Number_1*number_2
    print("Result:",operation)

elif choice=='4':
    operation=Number_1/number_2
    print("Result:",operation)

elif choice=='5':
    operation=Number_1%number_2
    print("Result:",operation)


