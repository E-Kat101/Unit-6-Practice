def month_name(n: int) -> str:
    if n == 1:
        return "January"
    elif n == 2:
        return "February"
    elif n == 3:
        return "March"
    elif n == 4:
        return "April"
    elif n == 5:
        return "May"
    elif n == 6:
        return "June"
    elif n == 7:
        return "July"
    elif n == 8:
        return "August"
    elif n == 9:
        return "September"
    elif n == 10:
        return "October"
    elif n == 11:
        return "November"
    elif n == 12:
        return "December"
    elif n < 1 or n > 12:
        return "Error"

def main():
    n = int(input("Number of the month: "))
    
    name = month_name(n)
    print(f"Month {n}: {name}")

if __name__ == "__main__":
    main()
