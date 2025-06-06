import threading

def even_factors_sum(no):
    sum_even = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            sum_even += i
    print(f"Sum of even factors : {sum_even}")

def odd_factors_sum(no):
    sum_odd = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            sum_odd += i
    print(f"Sum of odd factors : {sum_odd}")

if __name__ == "__main__":
    num = int(input("Enter a number :"))

t1 = threading.Thread(target=even_factors_sum, args=(num,))
t2 = threading.Thread(target=odd_factors_sum, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main.")