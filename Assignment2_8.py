def main():
  
 print("Enter a number :")
 no = int(input())
 print("Output :")

 for i in range(1,no + 1):
   for j in range(1, i + 1):
    print(j, end=" ")
   print()

if __name__ == "__main__":
 main()