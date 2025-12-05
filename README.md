# Producer-Consumer Problem with XML and Socket Programming  
Course: Concurrent Programming / Operating Systems  
Language: Python 3  
Authors: MBONGENI MASUKU & MKHONTA CEBSILE  
GitHub Profiles:  
- https://github.com/mjjunior98 
- https://github.com/mkhontacebsilesebulelo-cmd 


Project Overview  
This project is a complete implementation of the classic Producer-Consumer Problem using multi-threading, semaphores for synchronization, XML serialization, and TCP socket programming.

- Producer generates random IT student records and saves them as nicely formatted XML files (`student1.xml` – `student10.xml`).  
- A bounded buffer (size = 10) holds the file numbers (1–10).  
- Consumer reads the corresponding XML file, parses it, calculates the average mark, determines Pass/Fail (≥50%), displays results, then deletes the file.  
- Mutual exclusion and proper synchronization are enforced using Semaphores.  
- An alternative version using TCP sockets directly transmits XML data between producer and consumer (no shared folder).

---

 Folder Structure
 it-producer-consumer/
├── shared_folder/              # Created at runtime – holds XML files
├── itstudent.py                # ITstudent class + XML (un)marshalling
├── main.py                     # Threaded version (Producer + Consumer in one process)
├── producer.py                 # Standalone producer (for separate testing)
├── consumer.py                 # standalone consumer
├── socket_producer.py          # Part 3 – Socket-based producer
├── socket_consumer.py          # Part 3 – Socket-based consumer
├── README.md                   # This file

Sample Output (Consumer)
text==================================================
Student Name: Eve Johnson
Student ID: 48392017
Programme: BSc IT
Courses and Marks:
  - Programming: 78
  - Database: 92
  - Networking: 65
  - Web Development: 88
  - Algorithms: 54
Average Mark: 75.40
Result: PASS
==================================================             
