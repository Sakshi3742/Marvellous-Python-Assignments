def main():

   a = int(input("Enter first number :"))
   b = int(input("Enter second number :"))
   c = int(input("Enter third number :"))

   if a > b:
      if a > c:
        print("The largest number is :",a)
      else:
        print("The largest number is :",c)
   else:
      if b > c:
        print("The largest number is :",b)
      else:
        print("The largest number is :",c)

if __name__ == "__main__":
  main()
