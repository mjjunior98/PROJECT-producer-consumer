# main.py - Run this file
import os
import time
from threading import Thread, Semaphore
from itstudent import ITstudent

shared_dir = "shared_folder"
os.makedirs(shared_dir, exist_ok=True)

buffer = []
mutex = Semaphore(1)
empty = Semaphore(10)
full = Semaphore(0)

def producer():
    file_counter = 1
    while True:
        time.sleep(random.uniform(1, 4))
        empty.acquire()
        mutex.acquire()

        student = ITstudent()
        filename = f"{shared_dir}/student{file_counter}.xml"
        student.to_xml(filename)
        print(f"[PRODUCER] Created {filename}")

        buffer.append(file_counter)
        print(f"[BUFFER] -> {buffer}")

        mutex.release()
        full.release()

        file_counter = file_counter % 10 + 1

def consumer():
    while True:
        full.acquire()
        mutex.acquire()

        if not buffer:
            mutex.release()
            full.release()
            continue

        file_num = buffer.pop(0)
        filename = f"{shared_dir}/student{file_num}.xml"
        print(f"[CONSUMER] Consuming {filename}")

        mutex.release()

        # Read and parse XML
        student = ITstudent.from_xml(filename)
        if student:
            student.display()
            # Clear file after consumption
            os.remove(filename)
            print(f"[CONSUMER] Deleted {filename}")
        else:
            print(f"[CONSUMER] File {filename} not found!")

        time.sleep(2)

if __name__ == "__main__":
    import random
    random.seed()

    prod_thread = Thread(target=producer, daemon=True)
    cons_thread = Thread(target=consumer, daemon=True)

    prod_thread.start()
    cons_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")