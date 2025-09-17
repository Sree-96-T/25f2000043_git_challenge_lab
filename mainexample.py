from sum_module import add
from diff_module import difference
from multiply_module import multiply
from divide_module import divide

def main():
    print("Simple arithmetic demo (sum, difference, product, quotient)")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print(f"Sum: {add(a, b)}")
    print(f"Difference: {difference(a, b)}")
    print(f"Product: {multiply(a, b)}")
    q = divide(a, b)
    if q is None:
        print("Quotient: Error - division by zero")
    else:
        print(f"Quotient: {q}")

if __name__ == "__main__":
    main()
