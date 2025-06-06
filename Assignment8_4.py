import threading

def count_chars(text, char_type):
    thread_id = threading.get_ident()
    thread_name = threading.Thread().name
    count = 0

    if char_type == "small":
        count = sum(1 for char in text if char.islower())
    elif char_type == "capital":
        count = sum(1 for char in text if char.isupper())
    elif char_type == "digits":
        count = sum(1 for char in text if char.isdigit())

    print(f"Thread ID : {thread_id}, Thread Name : {thread_name}, {char_type} count : {count}")

if __name__ == "__main__":

    input_string = "HelloWorld123"

    print(input("Enter string :"))

    small_thread = threading.Thread(target=count_chars, args=(input_string, "small"), name="SmallThread")
    capital_thread = threading.Thread(target=count_chars, args=(input_string, "capital"), name="CapitalThread")
    digits_thread = threading.Thread(target=count_chars, args=(input_string, "digits"), name="DigitsThread")

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()