class Calculator:
    def add(self,x, y):
        return x + y

    def subtract(self,x, y):
        return x - y

    def multiply(self,x, y):
        return x * y

    def divide(self,x, y):
        if y == 0:
            return "Error! Division by zero."
        else:
            return x / y

    def modulo(self,x,y):
        return x % y

    def power(self,x,y):
        return x ** y

    def square(self,x):
        return x ** 2

    def cube(self,x):
        return x ** 3

    def square_root(self,x):
        return x ** (1/2)

    def cube_root(self,x):
        return x ** (1/3)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
print("6. Power")
print("7. Square")
print("8. Cube")
print("9. Square_Root")
print("10. Cube_Root")

calculator=Calculator()
while True:
    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))

        if choice == '1':
            print("Result:", calculator.add(num1,num2))
        elif choice == '2':
            print("Result:", calculator.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calculator.multiply(num1, num2))
        elif choice == '4':
            print("Result:", calculator.divide(num1, num2))
        elif choice == '5':
            print("Result:", calculator.modulo(num1, num2))
        elif choice == '6':
            print("Result:", calculator.power(num1, num2))
    elif choice in ('7', '8', '9', '10'):
        num1=float(input("Enter the Number: "))

        if choice == '7':
            print("Result:", calculator.square(num1))
        elif choice == '8':
            print("Result:", calculator.cube(num1))
        elif choice == '9':
            print("Result:", calculator.square_root(num1))
        elif choice == '10':
            print("Result:", calculator.cube_root(num1))
    else:
        print("Invalid input")
    
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        break