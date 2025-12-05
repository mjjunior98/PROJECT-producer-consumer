# itstudent.py
import random
from xml.etree import ElementTree as ET
from xml.dom import minidom
import os

class ITstudent:
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona", "Grace", "Henry", "Ivy", "Jack"]
    programmes = ["BSc IT", "BSc Computer Science", "BIT", "BSc Data Science"]
    courses = ["Programming", "Networking", "Database", "Web Development", "Operating Systems", "Algorithms"]

    def __init__(self):
        self.name = random.choice(self.names) + " " + random.choice(["Smith", "Johnson", "Lee", "Brown"])
        self.student_id = f"{random.randint(10000000, 99999999)}"
        self.programme = random.choice(self.programmes)
        self.course_marks = {}
        num_courses = random.randint(4, 6)
        selected_courses = random.sample(self.courses, num_courses)
        for course in selected_courses:
            self.course_marks[course] = random.randint(0, 100)

    def to_xml(self, filename):
        student = ET.Element("Student")
        ET.SubElement(student, "Name").text = self.name
        ET.SubElement(student, "StudentID").text = self.student_id
        ET.SubElement(student, "Programme").text = self.programme

        courses_elem = ET.SubElement(student, "Courses")
        for course, mark in self.course_marks.items():
            course_elem = ET.SubElement(courses_elem, "Course")
            ET.SubElement(course_elem, "Name").text = course
            ET.SubElement(course_elem, "Mark").text = str(mark)

        rough_string = ET.tostring(student, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)

    @staticmethod
    def from_xml(filename):
        if not os.path.exists(filename):
            return None
        tree = ET.parse(filename)
        root = tree.getroot()

        student = ITstudent()
        student.name = root.find("Name").text
        student.student_id = root.find("StudentID").text
        student.programme = root.find("Programme").text
        student.course_marks = {}

        for course_elem in root.find("Courses").findall("Course"):
            name = course_elem.find("Name").text
            mark = int(course_elem.find("Mark").text)
            student.course_marks[name] = mark

        return student

    def calculate_average(self):
        if not self.course_marks:
            return 0
        return sum(self.course_marks.values()) / len(self.course_marks)

    def passed(self):
        return self.calculate_average() >= 50

    def display(self):
        avg = self.calculate_average()
        status = "PASS" if self.passed() else "FAIL"
        print("\n" + "="*50)
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Programme: {self.programme}")
        print("Courses and Marks:")
        for course, mark in self.course_marks.items():
            print(f"  - {course}: {mark}")
        print(f"Average Mark: {avg:.2f}")
        print(f"Result: {status}")
        print("="*50 + "\n")