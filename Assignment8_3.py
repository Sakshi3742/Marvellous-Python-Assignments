import threading

def evenList(num_list):

         even_sum = 0
         for num in num_list:
             if num % 2 == 0:
              even_sum += num
         print(f"The sum of even numbers is : {even_sum}")

def oddList(num_list):

       odd_sum = 0
       for num in num_list:
          if num % 2 != 0:
            odd_sum += num
       print(f"The sum of odd numbers is : {odd_sum}")

def main():

    num_list = [2,4,12,45,32,10,5,11]

    t1 = threading.Thread(target=evenList, args=(num_list,))
    t2 = threading.Thread(target=oddList, args=(num_list,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()