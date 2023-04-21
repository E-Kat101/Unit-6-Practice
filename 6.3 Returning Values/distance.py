import math

def main():
    # test the formula a bit
    dist = distance(-2, 1, 1, 5)
    print(f"(-2,1) to (1,5) => {dist}")

    dist = distance(-2, -3, -4, 4)
    print(f"(-2,-3) to (-4,4) => {dist}")

    print(f"(2,-3) to (-1,-2) => {distance(2, -3, -1, -2)}")

    print(f"(4,5) to (4,5) => {distance(4, 5, 4, 5)}" )


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    # put your code in here, remove "pass"
    a = x2 - x1
    b = y2 - y1

    dist = math.sqrt(a**2 + b**2)
    
    return dist


if __name__ == "__main__":
    main()
