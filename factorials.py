def fack():
    """Prints factorial of a number"""
    message = int(input("Enter a number: "))

    total = 1
    numbers = []

    for number in range(1, message + 1):
        total = total * number
        numbers.append(str(number))

    print(" x ".join(numbers) + f" = {total}")


fack()