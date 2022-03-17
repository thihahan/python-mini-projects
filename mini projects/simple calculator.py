def calculator():
    print("Choose operation")
    print("1: Add")
    print('2: Minus')
    print('3: multiply')
    print("4: Division")

    operation = input()
    if operation == '1':
        num1 = input("Enter the first number: ")
        num2 = input("Enter the first number: ")
        while not (num1.isnumeric() and num2.isnumeric()):
            num1 = input("Enter the first number: ")
            num2 = input("Enter the first number: ")
        num1 = int(num1)
        num2 = int(num2)
        print(f"The sum is {num1 + num2}")
    elif operation == '2':
        num1 = input("Enter the first number: ")
        num2 = input("Enter the first number: ")
        while not (num1.isnumeric() and num2.isnumeric()):
            num1 = input("Enter the first number: ")
            num2 = input("Enter the first number: ")
        num1 = int(num1)
        num2 = int(num2)
        print(f"The sum is {num1 - num2}")
    elif operation == '3':
        num1 = input("Enter the first number: ")
        num2 = input("Enter the first number: ")
        while not (num1.isnumeric() and num2.isnumeric()):
            num1 = input("Enter the first number: ")
            num2 = input("Enter the first number: ")
        num1 = int(num1)
        num2 = int(num2)
        print(f"The sum is {num1 * num2}")
    elif operation == '4':
        num1 = input("Enter the first number: ")
        num2 = input("Enter the first number: ")
        while not (num1.isnumeric() and num2.isnumeric()):
            num1 = input("Enter the first number: ")
            num2 = input("Enter the first number: ")
        num1 = int(num1)
        num2 = int(num2)
        print(f"The sum is {num1 / num2}")
    else:
        print("Invalid key")


if __name__ == '__main__':
    calculator()

