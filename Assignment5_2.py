def main():

 char = input("Enter a Character :")

 if char in "a,e,i,o,u":
     print(char, "Is a Vowel.")
 else:
    print(char, "Is a Consonant.")

if __name__ == "__main__":
    main()