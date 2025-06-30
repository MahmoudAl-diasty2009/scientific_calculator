import math

def scientific_calculator():
    while True:
        print("*** The operations ***")
        print("1) + for addition")
        print("2) - for subtraction")
        print("3) * for multiplication")
        print("4) / for division")
        print("5) sqrt for square root")
        print("6) pow for power")
        print("7) sin for sine (degrees)")
        print("8) cos for cosine (degrees)")
        print("9) tan for tangent (degrees)")
        print("Type 'quit' to exit")

        the_operation = input("Choose the operation: ")

        if the_operation == "quit":
            print("Goodbye!")
            break

        if the_operation in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if the_operation == "1":
                print("Answer:", num1 + num2)

            elif the_operation == "2":
                print("Answer:", num1 - num2)

            elif the_operation == "3":
                print("Answer:", num1 * num2)

            elif the_operation == "4":
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print("Answer:", num1 / num2)

        elif the_operation == "5":
            num = float(input("Enter the number: "))
            if num < 0:
                print("Error: Negative number!")
            else:
                print("Answer:", math.sqrt(num))

        elif the_operation == "6":
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print("Answer:", math.pow(base, exponent))


        elif the_operation == "7":
            angle = float(input("Enter the angle in degrees: "))
            print("Answer:", math.sin(math.radians(angle)))

        elif the_operation == "8":
            angle = float(input("Enter the angle in degrees: "))
            print("Answer:", math.cos(math.radians(angle)))

        elif the_operation == "9":
            angle = float(input("Enter the angle in degrees: "))
            print("Answer:", math.tan(math.radians(angle)))

        else:
            print("Invalid operation. Please try again.")

scientific_calculator()
