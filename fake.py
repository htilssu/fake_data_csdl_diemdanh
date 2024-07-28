from datetime import datetime
from pydoc import stripid

from faker import Faker
from faker.generator import random
from faker.providers import DynamicProvider

from db import (class_section_list, class_session_list, clazz_list, conn, insert_class,
                insert_class_section,
                insert_lecturer,
                insert_student,
                lecturer_list,
                major_list, \
                room_list, specialized_list, student_list, subject_list, )
from model.attendance import Attendance
from model.class_ import Class
from model.class_section import ClassSection
from model.class_session import ClassSession
from model.Lecturer import Lecturer
from model.room import Room
from model.student import Student
from model.study import Study
from model.subject import Subject
from name_provider import cities_provider, districts_provider, female_name_provider, \
    last_name_provider, \
    male_name_provider, \
    street_provider

major_provider = DynamicProvider(
    provider_name="major_htilssu",
    elements=major_list,
)

spec_provider = DynamicProvider(
    provider_name="spec_htilssu",
    elements=specialized_list,
)

lec_provider = DynamicProvider(
    provider_name="lec_htilssu",
    elements=lecturer_list,
)

clzz_provider = DynamicProvider(
    provider_name="class_htilssu",
    elements=clazz_list,
)

subject_provider = DynamicProvider(
    provider_name="subject_htilssu",
    elements=subject_list,
)

room_provider = DynamicProvider(
    provider_name="room_htilssu",
    elements=room_list,
)

class_section_provider = DynamicProvider(
    provider_name="class_section_htilssu",
    elements=class_section_list,
)
class_session_provider = DynamicProvider(
    provider_name="class_session_htilssu",
    elements=class_session_list,
)

student_provider = DynamicProvider(
    provider_name="student_htilssu",
    elements=student_list,
)

fake = Faker('it_IT')
fake.add_provider(last_name_provider)
fake.add_provider(female_name_provider)
fake.add_provider(male_name_provider)
fake.add_provider(street_provider)
fake.add_provider(districts_provider)
fake.add_provider(cities_provider)
fake.add_provider(major_provider)
fake.add_provider(spec_provider)
fake.add_provider(lec_provider)
fake.add_provider(clzz_provider)
fake.add_provider(subject_provider)
fake.add_provider(room_provider)
fake.add_provider(class_section_provider)
fake.add_provider(class_session_provider)
fake.add_provider(student_provider)


def gen_address():
    return (
            fake.building_number() + ", " + fake.street_provider_htilssu() + ", "
                                                                             "" +
            fake.districts_provider_htilssu()
            + ", " + fake.cities_provider_htilssu())


# conn = db.conn

student_mail = "st.edu.vn"
lecturer_mail = "edu.vn"

current_year = 24


def gen_sex():
    return random.choice([0, 1])


def gen_first_name(gender):
    if gender == 0:
        return fake.male_name_htilssu() + " " + fake.male_name_htilssu()
    else:
        return fake.female_name_htilssu() + " " + fake.female_name_htilssu()


def gen_phone_number():
    phone = fake.phone_number()
    phone_num = len(phone.split(" ")) == 1 and phone.split(" ")[0] or phone.split(" ")[1]
    if len(phone_num) == 9:
        phone_num = "0" + phone_num
    elif len(phone_num) < 10:
        phone_num = "0" + phone_num[1:]

    return phone_num


def random_year_prefix():
    return fake.random_int(min=22, max=24)


def gen_student():
    clazz: Class = fake.class_htilssu()
    school_year = random_year_prefix()
    clazz_id = stripid(clazz.name)
    s = clazz_id.replace(clazz.spec_id, "")[:2]
    if s != str(school_year):
        return None
    idd = fake.numerify(text=f'{school_year}DH######')

    last_name = fake.last_name_htilssu()
    sex = gen_sex()
    first_name = gen_first_name(sex)
    name = last_name + " " + first_name
    email_st = idd + "@" + student_mail
    fake.phone_number()
    phone = gen_phone_number()
    address = gen_address()
    birthday = fake.date_of_birth(minimum_age=18 + current_year - school_year,
                                  maximum_age=18 + current_year - school_year)
    return Student(idd, name, email_st, phone, address, birthday, sex, clazz_id)


def fake_lecturer(number):
    list_lec = []
    for i in range(number):
        id = fake.numerify(text=f'######')
        sex = gen_sex()
        name = fake.last_name_htilssu() + " " + gen_first_name(sex)
        email = fake.email(domain=lecturer_mail)
        phone = gen_phone_number()
        address = gen_address()
        birthday = fake.date_of_birth(minimum_age=27, maximum_age=50)
        major = fake.major_htilssu()
        list_lec.append(Lecturer(id, name, email, phone, address, birthday, sex, major.id))

    return list_lec


def fake_lecturer_and_insert(number):
    list_lec = fake_lecturer(number)
    for lec in list_lec:
        insert_lecturer(lec)


def fake_class(number):
    class_l = []
    for i in range(number):
        spec = fake.spec_htilssu()
        lec = fake.lec_htilssu()
        num_id = fake.numerify(text=f'#')
        class_l.append(Class(spec.id + str(random_year_prefix()) + num_id, spec.id, lec.id))

    return class_l


def fake_class_and_insert(number):
    cl_list = fake_class(number)
    for cl in cl_list:
        insert_class(cl)


def fake_student_and_insert(number):
    for i in range(number):
        student = gen_student()
        if student is None:
            continue
        insert_student(student)


def fake_class_session(number):
    class_section: ClassSection = fake.class_section_htilssu()
    class_section_id = class_section.id
    for i in range(number):
        time = fake.date_time_ad(start_datetime=datetime(2023, 1, 1),
                                 end_datetime=datetime(2024, 9, 9))
        room: Room = fake.room_htilssu()
        id_room = room.name
        lecturer: Lecturer = fake.lec_htilssu()
        id_lecturer = lecturer.id
        cl_session: ClassSession = ClassSession(class_section_id, time, id_room, id_lecturer, None)
        cl_session.save_to_db(connection=conn)


def fake_class_section(number):
    class_section_list = []
    for i in range(number):
        subject: Subject = fake.subject_htilssu()
        room: Room = fake.room_htilssu()
        lecturer: Lecturer = fake.lec_htilssu()
        id = fake.numerify(text=f'##########')
        class_section_list.append(
            ClassSection(id, subject.id, room.name, lecturer.id, fake.time(), fake.time(),
                         fake.random_int(min=2, max=7)))

    return class_section_list


def fake_class_section_and_insert(number):
    list_class = fake_class_section(number)
    for list_class in list_class:
        insert_class_section(list_class)


def fake_attendance_and_insert(number):
    cl = [1158838259, 1477550316, 2918588227, 2455089225, 7519467958, 8569663081, 9656631159]
    classss = random.choice(cl)
    for i in range(number):
        class_session: [] = ClassSession.get_by_class_section(conn, classss)
        for ass in class_session:
            stud_list = Study.get_students_by_class_section(conn, ass.id_class_section)
            for st in stud_list:
                att = Attendance(None, ass.id, st, ass.time,
                                 random.choice([0, 1, 2, 3]))
                att.save_to_db(conn)


def fake_study_and_insert(number):
    # class_section: ClassSection = fake.class_section_htilssu()
    cl = [1158838259, 1477550316, 2918588227, 2455089225, 7519467958, 8569663081, 9656631159]
    classss = random.choice(cl)
    for i in range(number):
        student: Student = fake.student_htilssu()
        sty = Study(student.Id, classss)
        sty.save_to_db(conn)
