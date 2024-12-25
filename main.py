from src.lib.calculator import add,substract, multiply, divide
from src.lib.statistics import mean, standard_deviation
import logging


# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():

    logging.info("Starting the Math Tools CLI")

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
            logging.info(f"Performing addition: {a} + {b}")
            print(f"Result: {add(x = a, y = b)}")
        elif choice == 2:
            logging.info(f"Performing subtraction: {a} - {b}")
            print(f"Result: {substract(a,b)}")
        elif choice == 3:
            logging.info(f"Performing multiplication: {a} * {b}")
            print(f"Result: {multiply(a,b)}")
        elif choice == 4:
            try:
                logging.info(f"Performing division: {a} / {b}")
                print(f"Result: {divide(a,b)}")
            except ValueError as e:
                logging.info(f"Error during division: {e}")
                print(f"Error: {e}")
    elif choice in [5,6]:
        data = list(map(float,input("Enter list of numbers (comma-separated): ").split(",")))
        if choice == 5:
            logging.info(f"Calculating mean of data: {data}")
            print(f"Result: {mean(data)}")
        elif choice == 6:
            logging.info(f"Calculating sd of data: {data}")
            print(f"Result: {standard_deviation(data)}")
    else:
        logging.warning("Invalid choice entered")
        print("Invalid choice.")

if __name__ == "__main__":
    main()
