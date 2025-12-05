# socket_consumer.py
import socket
import xml.etree.ElementTree as ET
from itstudent import ITstudent

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[SOCKET CONSUMER] Connected to producer")

    while True:
        # Receive message length
        length_bytes = s.recv(4)
        if not length_bytes:
            break
        length = int.from_bytes(length_bytes, 'big')

        # Receive XML data
        xml_data = b""
        while len(xml_data) < length:
            packet = s.recv(length - len(xml_data))
            if not packet:
                break
            xml_data += packet

        root = ET.fromstring(xml_data)
        temp_file = "received_student.xml"
        with open(temp_file, "wb") as f:
            f.write(xml_data)

        student = ITstudent.from_xml(temp_file)
        if student:
            student.display()
        else:
            print("Failed to parse student")