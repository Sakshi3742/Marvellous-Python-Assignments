import threading

def display_ascending():
    for i in range(1,51):
        print(f"Thread1  : {i}")

def display_descending():
    for i in range(50,0,-1):
        print(f"Thread2 : {i}")

if __name__ == "__main__":

    thread1 = threading.Thread(target=display_ascending)
    thread2 = threading.Thread(target=display_descending)

    thread1.start()
    thread1.join()

    thread2.start()