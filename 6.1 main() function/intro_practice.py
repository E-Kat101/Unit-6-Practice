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
