# Hello, Name!
def main():
    name = input("Enter your name: ")

    if name == "":
        name = "User"
    
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

   # Area Calculator
def main():
    print("Welcome to the awesome area calculator!")
    print()
    
    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print()
    
    area = length * width
    
    print(f"The area is {area} units squared")

if __name__ == "__main__":
    main()
    
# Area Calculator greet() Function
def main():
    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print()
    
    area = length * width
    
    print(f"The area is {area} units squared")

def greet():
    print("Welcome to the awesome area calculator!")
    print()

if __name__ == "__main__":
    greet()
    main()

# Ticket Prices
PRICE_PER_TICKET = 13.95

def main():
    many_tickets = int(input("How many tickets would you like? "))

    total = many_tickets * PRICE_PER_TICKET

    print(f"The total for {many_tickets} tickets is ${(round)(total, 2)}")

if __name__ == "__main__":
    main()
