"""
Connects to a SQL database using pyodbc
"""
from typing import List

import pyodbc

from model.class_ import Class
from model.class_section import ClassSection
from model.class_session import ClassSession
from model.Lecturer import Lecturer
from model.major_class import Major
from model.room import Room
from model.specialized import Specialized
from model.student import Student
from model.subject import Subject

SERVER = 'localhost'
DATABASE = 'QL_DiemDanh'
USERNAME = 'htilssu'
PASSWORD = 'Shuu@2004'

connectionString = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};'
    f'PWD={PASSWORD};Encrypt=yes;TrustServerCertificate=yes;Connection_Timeout=30;')

conn = pyodbc.connect(connectionString)

if conn is None:
    print("Error: Connection to database failed")

else:
    print("Connection to database successful")

insert_student_query = ("INSERT INTO Student (Id, Name, Email, Phone, Address, Birthday, Id_Class) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)")

insert_subject_query = "INSERT INTO Subject (Id,Name,Credit) VALUES (?,?,?)"

insert_major_query = "INSERT INTO Major (Id,Name) VALUES (?,?)"

insert_class_query = "INSERT INTO Class (Id,Name,Id_Major) VALUES (?,?,?)"


def insert_major(major: Major):
    try:
        cursor = conn.cursor()
        cursor.execute(insert_major_query, major.id, major.name)
        cursor.commit()
        cursor.close()
    except:
        print(f"Lỗi khi thêm major: {major.name}")


def insert_student(student: Student):
    try:
        cursor = conn.cursor()
        cursor.execute(insert_student_query, student.Id, student.Name, student.Email, student.Phone,
                       student.Address,
                       student.Birthday, student.Clazz_id)
        cursor.commit()
        cursor.close()
    except Exception as e:
        print(f"Lỗi khi thêm student")


def insert_lecturer(lecturer: Lecturer):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Lecturer (Id, Email, Name, Phone,Address,Birthday,Sex, Id_Major) VALUES "
            "(?,?,?,?,?,?,?,?)",
            lecturer.id, lecturer.email, lecturer.name, lecturer.phone, lecturer.address,
            lecturer.birthday, lecturer.sex, lecturer.id_major)
        cursor.commit()
        cursor.close()
    except:
        pass


def get_all_major():
    major_l = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Major")
    rows = cursor.fetchall()
    for row in rows:
        major = Major(row.Id, row.Name, row.Id_Dean)
        major_l.append(major)
    cursor.close()
    return major_l


def get_all_specialization():
    spec_l = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Specialized")
    rows = cursor.fetchall()
    for row in rows:
        spec = Specialized(row.Id, row.Name, row.Id_Major)
        spec_l.append(spec)
    cursor.close()
    return spec_l


def get_all_lecturer():
    lec_l = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Lecturer")
    rows = cursor.fetchall()
    for row in rows:
        lec = Lecturer(row.Id, row.Name, row.Email, row.Phone, row.Address, row.Birthday, row.Sex,
                       row.Id_Major)
        lec_l.append(lec)
    cursor.close()
    return lec_l


def insert_class(clazz: Class):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Class (Name, Id_Specialized, Id_FacultyAdvisor) VALUES (?,?,?)",
                       clazz.name, clazz.spec_id, clazz.fal_advisor_id)
        cursor.commit()
        cursor.close()
    except Exception as e:
        print(f"Lỗi khi thêm class")


def insert_class_section(class_section: ClassSection):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ClassSection (Id,Id_Subject, Id_Room, Id_Lecturer, LessionStart, "
            "LessionEnd, DayOfWeek) "
            "VALUES (?,?,?,?,?,?,?)", class_section.id,
            class_section.id_subject, class_section.id_room, class_section.id_lecturer,
            class_section.start, class_section.end, class_section.day_of_week)
        cursor.commit()
        cursor.close()
    except Exception as e:
        print(e)


def get_all_class():
    clazz_l = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Class")
    rows = cursor.fetchall()
    for row in rows:
        clazz = Class(row.Name, row.Id_Specialized, row.Id_FacultyAdvisor)
        clazz_l.append(clazz)
    cursor.close()
    return clazz_l


def get_all_student():
    student_l = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    for row in rows:
        student = Student(row.Id, row.Name, row.Email, row.Phone, row.Address, row.Birthday,
                          row.Sex, row.Id_Class)
        student_l.append(student)
    cursor.close()
    return student_l


def get_all_room():
    room_l = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Room")
    rows = cursor.fetchall()
    for row in rows:
        room = Room(row.Name, row.Id_Campus)
        room_l.append(room)
    cursor.close()
    return room_l


def get_all_subject():
    subject_l = []
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Subject")
    rows = cursor.fetchall()
    for row in rows:
        subject = Subject(row.Id, row.Name, row.Credit)
        subject_l.append(subject)
    cursor.close()
    return subject_l


def get_all_class_section():
    class_section_list: List['ClassSection'] = []
    cursor = conn.cursor()
    cursor.execute("select * from ClassSection")
    rows = cursor.fetchall()
    for row in rows:
        class_session: ClassSection = ClassSection(row.Id, row.Id_Subject, row.Id_Room,
                                                   row.Id_Lecturer, row.LessionStart,
                                                   row.LessionEnd, row.DayOfWeek)
        class_section_list.append(class_session)
    return class_section_list


def get_all_class_session():
    class_session_list: List['ClassSession'] = []
    cursor = conn.cursor()
    cursor.execute("select * from ClassSession")
    rows = cursor.fetchall()
    for row in rows:
        classe_session: ClassSession = ClassSession(row.Id_ClassSection, row.Time, row.Id_Room,
                                                    row.Id_Lecturer, row.Id)
        class_session_list.append(classe_session)
    return class_session_list

def get_student_list_study_at(class_session):
    sql = 'select * from ClassSection, ClassSection, Study where ClassSection.Id = ClassSession.Id_ClassSection'


student_list = get_all_student()
major_list = get_all_major()
specialized_list = get_all_specialization()
lecturer_list = get_all_lecturer()
clazz_list = get_all_class()
room_list = get_all_room()
subject_list = get_all_subject()
class_section_list = get_all_class_section()
class_session_list = get_all_class_session()
