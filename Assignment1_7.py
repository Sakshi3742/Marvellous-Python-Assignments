def is_divisible_by_5(no):
    if no % 5 == 0:
        return True
    else:
        return False
    
no = int(input("Enter a number :"))
print("Result :", is_divisible_by_5(no))