# Heron's Formula
import math


def main():
    area = triangle_area(3, 3, 3)
    print(f"A triangle with sides 3, 3, 3 has an area of {area}")

    area = triangle_area(3, 4, 5)
    print(f"A triangle with sides 3, 4, 5 has an area of {area}")

    area = triangle_area(7, 8, 9)
    print(f"A triangle with sides 7, 8, 9 has an area of {area}")

    area = triangle_area(5, 12, 13)
    print(f"A triangle with sides 5, 12, 13 has an area of {area}")

    area = triangle_area(10, 9, 11)
    print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
    area = triangle_area(8, 15, 17)
    print(f"A triangle with sides 8, 15, 17 has an area of {area}")

    area = triangle_area(9, 9, 9)
    print(f"A triangle with sides 9, 9, 9, has an area of {area}")
    # No, it was not difficult to add to the file that used a function, since all I needed to do was change the arguments in the brackets. The rules have already been defined by the parameters created in the function triangle_area, so I didn't have to write all the steps to using the formula over again, like I did in the file with no functions.

def triangle_area(a: int, b: int, c: int) -> float:
    """Calculates a triangles area.
    
    Args:
        a: length of side a
        b: length of side b
        c: length of side c
    
    Returns:
        The area of the triangle
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area
    # ^ after computing the area, "return" it


if __name__ == "__main__":
    main()

# Heron's Formula - No Function
def main():
    a = 3
    b = 3
    c = 3
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 3, 3, 3 has an area of {area}")

    a = 3
    b = 4
    c = 5
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 3, 4, 5 has an area of {area}")

    a = 7
    b = 8
    c = 9
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 7, 8, 9 has an area of {area}")

    a = 5
    b = 12
    c = 13
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 5, 12, 13 has an area of {area}")

    a = 10
    b = 9
    c = 11
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
    a = 8
    b = 15
    c = 17
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 8, 15, 17 has an area of {area}")

    a = 9
    b = 9
    c = 9
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 9, 9, 9 has an area of {area}")

if __name__ == "__main__":
    main()

"""
1. Run both files (herons_formula.py and herons_formula_no_function.py). Do they both produce the same output?
Yes, they produce the same output.

2. How many lines long is herons_formula_no_function.py? How many lines long is herons_formula.py if you don’t count the 10 lines of comments inside the triangle_area() function?
herons_formula_no_function.py is 48 lines long. herons_formula.py is 32 lines long.

3. There is a bug in the formula for both files. When (a+b+c) is an odd number, floor-dividing by 2 throws away the .5. Fix both files so that instead of (a+b+c) // 2 you have (a+b+c) / 2 everywhere it occurs. Was it easier to fix the file that used a function, or the one that didn’t use a function? Answer in a comment.
It was easier to fix the file that used a function than the file that didn't use a function since, with the function, I only had to change one line of code. However, for the file without a function, I had to change multiple lines.

4. Add one more test to both files: find the area of a triangle with sides 9, 9, and 9. Was it difficult to add to the file that used a function? Answer in a comment on the line below where you added the new function call.
"""
