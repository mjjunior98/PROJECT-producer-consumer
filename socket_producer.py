# socket_producer.py
import socket
import time
import random
from itstudent import ITstudent
import xml.etree.ElementTree as ET

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[SOCKET PRODUCER] Waiting for consumer...")
    conn, addr = s.accept()
    with conn:
        print(f"[SOCKET PRODUCER] Connected by {addr}")
        counter = 1
        while True:
            time.sleep(random.uniform(2, 5))
            student = ITstudent()
            student.to_xml(f"temp_student{counter}.xml")

            tree = ET.parse(f"temp_student{counter}.xml")
            xml_data = ET.tostring(tree.getroot(), encoding='utf-8')

            # Send length first, then data
            conn.sendall(len(xml_data).to_bytes(4, 'big'))
            conn.sendall(xml_data)

            print(f"[SOCKET PRODUCER] Sent student{counter}.xml")
            counter = counter % 10 + 1