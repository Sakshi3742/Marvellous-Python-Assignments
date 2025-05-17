def sum_of_factors(n):
  total = 0
 
  for i in range(1, n):
     if n % i == 0:
       total += i
  return total
      
print("Enter a number :")
num = int(input())
result = sum_of_factors(num)

print("Answer :",result)