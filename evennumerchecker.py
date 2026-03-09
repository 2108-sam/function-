def evenchecker():
    """This checks if a number is even"""
    number=int(input("Enter a number: "))
    if number%2==0:
        print("You have entered an even number.")
    else:
        print("Number not an even number")
evenchecker()