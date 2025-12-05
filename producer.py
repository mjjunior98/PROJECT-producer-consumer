# producer.py
import os
import time
import random
from threading import Thread, Semaphore
from itstudent import ITstudent

shared_dir = "shared_folder"
os.makedirs(shared_dir, exist_ok=True)

buffer_size = 10
buffer = []  # stores integers 1 to 10
mutex = Semaphore(1)
empty = Semaphore(buffer_size)
full = Semaphore(0)

def producer():
    file_counter = 1
    while True:
        time.sleep(random.uniform(1, 3))  # Simulate production time

        empty.acquire()      # Wait if buffer full
        mutex.acquire()      # Enter critical section

        # Produce student and save as XML
        student = ITstudent()
        filename = f"{shared_dir}/student{file_counter}.xml"
        student.to_xml(filename)
        print(f"[PRODUCER] Produced {filename}")

        # Add file number to buffer
        buffer.append(file_counter)
        print(f"[PRODUCER] Buffer now: {buffer}")

        mutex.release()
        full.release()

        file_counter = file_counter % 10 + 1  # Cycle 1 to 10

if __name__ == "__main__":
    producer_thread = Thread(target=producer, daemon=True)
    producer_thread.start()
    producer_thread.join()