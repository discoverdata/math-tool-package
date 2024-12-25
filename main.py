from src.lib.calculator import add,substract, multiply, divide
from src.lib.statistics import mean, standard_deviation

def main():
    print("Welcome to maths tools!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Mean")
    print("6. Standard Deviation")
    
    choice = float(input("Choose an operation: "))
    if choice in [1,2,3,4]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == 1:
            print(f"Result: {add(x = a, y = b)}")
        elif choice == 2:
            print(f"Result: {substract(a,b)}")
        elif choice == 3:
            print(f"Result: {multiply(a,b)}")
        elif choice == 4:
            print(f"Result: {divide(a,b)}")
    elif choice in [5,6]:
        data = list(map(float,input("Enter list of numbers (comma-separated): ").split(",")))
        if choice == 5:
            print(f"Result: {mean(data)}")
        elif choice == 6:
            print(f"Result: {standard_deviation(data)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
