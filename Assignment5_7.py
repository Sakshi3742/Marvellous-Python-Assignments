def main():
    length = float(input("Enter length of Rectangle :"))
    width = float(input("Enter width of Rectangle :"))

    Area = length * width
    perimeter = 2 * (length + width)

    print("Area :",Area)
    print("Perimeter :",perimeter)

if __name__ == "__main__":
    main()