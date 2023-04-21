import math

def area_circle(radius: int) -> float:
    # Calculates area of a circle
    return math.pi * radius**2

def area_rectangle(length: float, width: float) -> float:
    # Calculates area of a rectangle
    return length * width

def area_square(side: float) -> float:
    # Calculates area of a square
    return side**2

def area_triangle(base: float, height: float) -> float:
    # Calculates area of a triangle
    return 0.5 * (base * height)

def main():
    print("Welcome to the Shape Area Calculator")
    print()

    while True:
        print("1) Circle   2) Rectangle   3) Square   4) Triangle   5) Quit")
        shape = int(input("Which shape: "))
        if shape == 1:
            radius = int(input("Radius: "))

            area = area_circle(radius)
            print(f"The area is {area}.")
        elif shape == 2:
            length = float(input("Length: "))
            width = float(input("Width: "))

            area = area_rectangle(length, width)
            print(f"The area is {area}.")
        elif shape == 3:
            side = float(input("Side: "))

            area = area_square(side)
            print(f"The area is {area}.")
        elif shape == 4:
            base = float(input("Base: "))
            height = float(input("Height: "))

            area = area_triangle(base, height)
            print(f"The area is {area}.")
        elif shape == 5:
            print("Goodbye.")
            break
        else:
            print("Looks like your input is invalid! Try again.")
        print()
            

if __name__ == "__main__":
    main()
