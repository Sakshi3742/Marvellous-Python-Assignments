def main():

 print("Enter a number :")
 num = int(input())

 if num < 2:
   print("It is not a Prime number")
 else:
   is_prime = True
   for i in range(2,num):
     if num % i == 0:
       is_prime = False

 if is_prime:
  print("It is a prime number")
 else:
  print("It is not a prime number")

if __name__ == "__main__":
   main()