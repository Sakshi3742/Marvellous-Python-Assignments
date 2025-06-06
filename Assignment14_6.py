class Calculator:
    def add(self,A,B):
        return A + B
    
    def substract(self,A,B):
        return A - B
    
    def multiply(self,A,B):
        return A * B
    
    def divide(self,A,B):
        if B != 0:
          return A/B
        
calc = Calculator()

No1 = int(input("Enter first number :"))
No2 = int(input("Enter second number :"))

print("Addition:", calc.add(No1,No2))
print("Substraction:", calc.substract(No1,No2))
print("Multiplication:", calc.multiply(No1,No2))
print("Division:", calc.divide(No1,No2))